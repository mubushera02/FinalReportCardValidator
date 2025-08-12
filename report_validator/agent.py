from google.adk.agents.llm_agent import Agent
import json
import os

root_agent = Agent(
    model="gemini-2.5-flash",
    name="ReportCardValidator",
    description="Validates academic report cards for identity, pagination, anomalies, duplicates, and document type.",
    instruction="You validate student report cards for identity consistency, correct pagination, content anomalies, duplicate documents, and confirm document type."
)

def load_report(filepath: str):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    with open(filepath, "r") as f:
        return json.load(f)

def check_student_identity(data):
    return {"student_name": data.get("name"), "roll_number": data.get("roll_number")}

def check_pagination(data):
    pages = data.get("pages", [])
    if not pages:
        return {"pagination_correct": False, "error": "No page information"}
    total_pages = pages[-1].get("page_number")
    errors = []
    page_numbers = [p.get("page_number") for p in pages]
    expected = list(range(1, total_pages + 1))
    if page_numbers != expected:
        errors.append(f"Pagination Error: Expected pages {expected}, found {page_numbers}")
    return {"pagination_correct": len(errors) == 0, "errors": "; ".join(errors) if errors else None}

def check_content_consistency(data):
    pages = data.get("pages", [])
    if not pages:
        return {"content_consistent": False, "error": "No pages found"}
    first_name = pages[0].get("student_name")
    for i, page in enumerate(pages):
        if page.get("student_name") != first_name:
            return {
                "content_consistent": False,
                "error": f"Anomaly Detected: Page {i+1} has different student name '{page.get('student_name')}'."
            }
    return {"content_consistent": True, "error": None}

def check_duplicate(data1, data2):
    return data1 == data2

def classify_document(data):
    doc_type = data.get("document_type", "").lower()
    return doc_type in ["report card", "progress report", "scorecard"]


def validate_reports(file1: str, file2: str):
    try:
        data1 = load_report(file1)
        data2 = load_report(file2)
    except Exception as e:
        return {"error": f"Failed to load files: {str(e)}"}

    id1 = check_student_identity(data1)
    id2 = check_student_identity(data2)
    student_identity_match = (id1 == id2)

    pag1 = check_pagination(data1)
    pag2 = check_pagination(data2)

    cont1 = check_content_consistency(data1)
    cont2 = check_content_consistency(data2)

    files_are_duplicates = check_duplicate(data1, data2)

    is_report_card_1 = classify_document(data1)
    is_report_card_2 = classify_document(data2)

    return {
        "file_1": os.path.basename(file1),
        "file_2": os.path.basename(file2),
        "validation_summary": {
            "student_identity_match": student_identity_match,
            "files_are_duplicates": files_are_duplicates,
            "file_1_validation": {
                "is_report_card": is_report_card_1,
                "pagination_correct": pag1.get("pagination_correct", False),
                "content_consistent": cont1.get("content_consistent", False),
                "errors": pag1.get("errors") or cont1.get("error")
            },
            "file_2_validation": {
                "is_report_card": is_report_card_2,
                "pagination_correct": pag2.get("pagination_correct", False),
                "content_consistent": cont2.get("content_consistent", False),
                "errors": pag2.get("errors") or cont2.get("error")
            }
        }
    }
