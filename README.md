# FinalReportCardValidator

This project provides an AI-powered agent to validate academic report cards by checking:

- Student identity consistency  
- Pagination correctness  
- Content anomalies  
- Duplicate documents  
- Document type classification

---

## Features

- Compare two report card JSON files  
- Verify student details and pagination  
- Detect anomalies and duplicates  
- Output detailed JSON validation report

---

## Setup

1. Clone the repository  
   ```bash
   git clone https://github.com/mubushera02/FinalReportCardValidator.git
   cd FinalReportCardValidator
   
2. Create and activate a Python virtual environment
   ```bash
   python -m venv venv
   # Linux/macOS
   source venv/bin/activate
   # Windows
   venv\Scripts\activate
   
3. Install dependencies
   ```bash
   pip install -r requirements.txt

4. Running the agent with CLI
   ```bash
   adk run report_validator
   
5. launches the interactive Dev UI accessible in your browser
   ```bash
   adk web

### ADK Web (Web Interface)

The ADK framework provides a built-in web UI to interact with your agent easily.

- After running `adk run report_validator`, open your browser and go to: http://127.0.0.1:8000/dev-ui/


- This web interface lets you chat with the agent, send JSON inputs, and view responses in real time.

- It is especially useful for testing, debugging, and demonstrating the agent without writing code.

- You can upload or paste report card data directly in the UI to get validation results.

---




