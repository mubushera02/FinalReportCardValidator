from report_validator.agent import validate_reports
import sys
import json

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python run.py <file1.json> <file2.json>")
        sys.exit(1)

    file1, file2 = sys.argv[1], sys.argv[2]
    result = validate_reports(file1, file2)
    print(json.dumps(result, indent=4))
