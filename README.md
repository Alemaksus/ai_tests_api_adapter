# AI Agent Test API Adapter

This is a lightweight FastAPI-based adapter that exposes a unified REST API interface for triggering automated tests for AI agents. It is designed to be portable, easy to launch, and compatible with multiple client environments such as Python, Java, JavaScript, Go, and C++.

## 🚀 Features

- Run AI-related tests via simple API calls
- Supports multiple test types (core logic, unit tests, data analysis, etc.)
- Swagger UI included for interactive testing
- Works with any client (Postman, curl, browser, Java, etc.)
- Portable via `.bat` scripts for Windows systems

## 🔧 Requirements

- Python 3.11+
- Dependencies listed in `requirements.txt`

## ▶ How to Start

### Step 1: Create and activate virtual environment

```bash
python -m venv venv
.env\Scriptsctivate      # For Windows
```

### Step 2: Install requirements

```bash
pip install -r requirements.txt
```

### Step 3: Run the server

```bash
uvicorn main:app --reload
```

---

## 🌐 Available Endpoints

### 🔹 Swagger UI (Main Interface)
**URL:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
Use this interface to interactively test all available endpoints.

### 🔹 Root Page
**GET /**  
Returns a welcome message and useful links.

### 🔹 Health Check
**GET /healthcheck**  
Checks if the API is running. Returns: `{ "status": "ok" }`

### 🔹 Run AI Tests
**GET /run-test/{client_lang}**  
Run tests and get results.

**Example:**  
`http://127.0.0.1:8000/run-test/python`

`client_lang` can be:
- `python`
- `java`
- `js`
- `go`
- `c++`

---

## 🧪 Example curl Request

```bash
curl -X GET "http://127.0.0.1:8000/run-test/python" -H "accept: application/json"
```

---

## 📁 Project Structure

```
ai_tests_api_adapter/
│
├── main.py                 # Main FastAPI app
├── requirements.txt        # Dependencies
├── start_api.bat           # Starts server (Windows)
├── stop_api.bat            # Stops server (Windows)
├── tests/
│   ├── core_test.py        # Core logic test
│   └── agent_test.py       # Sample unit test
└── README.md               # This file
```

---

## 🧩 License

This project is currently shared for demonstration and review purposes only.
License terms will be defined later if the project is to be reused or published.