# AI Agent Test API (Multi-language)

This project demonstrates a simple HTTP API for running Python-based AI agent tests.
It is designed to integrate easily with external test frameworks written in various languages.

---

## Supported Languages

Call the endpoint `/run-test/{client_lang}` using any of the following values:

- `java`
- `python`
- `js`
- `go`
- `c++`

The response will include the requested client language.

---

## How to Use

1. Open PowerShell and go to the project folder

```powershell
cd path\to\your\project
```

2. Create a virtual environment (only once)

```powershell
python -m venv venv
```

3. Activate the environment

```powershell
venv\Scripts\Activate.ps1
```

4. Install dependencies

```powershell
pip install -r requirements.txt
```

5. Start the server manually:

```powershell
uvicorn main:app --reload
```

Or double-click `start_api.bat`

---

## Example API Call

**Request:**
```
GET /run-test/java
```

**Response:**
```json
{
  "agent_id": "agent_001",
  "result": "passed",
  "metrics": {
    "accuracy": 0.95
  },
  "client": "java"
}
```

---

## Scripts

- `start_api.bat` — launches the server in a new window and opens Swagger
- `stop_api.bat` — stops the Uvicorn server
- `reset_venv.bat` — removes and recreates the virtual environment with dependencies---

## API Documentation (Swagger UI)

Once the server is running, you can access the interactive documentation by opening the following link in your browser:

🔗 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

This page is auto-generated using [Swagger UI](https://swagger.io/tools/swagger-ui/).  
It allows you to:
- View available endpoints
- See example requests and responses
- Test the API directly from the browser without writing any code

> ✅ Useful for developers, testers, and even non-technical stakeholders to explore the API in a user-friendly interface.