from fastapi import FastAPI
from tests.core_test import run_core_logic
from tests.agent_test import run_sample_test
from tests.java_client_sim import java_like_healthcheck

# Create the FastAPI app with title and version
app = FastAPI(title="AI Agent Test API", version="1.0")

# 🔹 1. Root endpoint ("/") – to avoid 404 and provide a welcome message
@app.get(
    "/",
    summary="Welcome page",
    description="Redirects to Swagger UI and shows an example endpoint."
)
def index():
    return {
        "message": "Welcome to the AI Agent Test API!",
        "docs": "Visit /docs for Swagger UI",
        "example": "/run-test/java",
        "note": "This adapter simulates tests from different client languages. "
                "One of the included tests emulates a Java client performing a health check."
    }

# 🔹 2. Main test runner endpoint – runs 2 sample tests
@app.get(
    "/run-test/{client_lang}",
    summary="Run AI agent tests",
    description="""
Runs a predefined set of tests for AI agents and returns results.
Supports integration with tests from different client environments like Java, Python, JavaScript, etc.

This endpoint returns:
- Results of core logic validation
- Sample unit test for basic validation
"""
)
def run_agent_test(client_lang: str):
    core_result = run_core_logic()            # test from core_test.py
    simple_test_result = run_sample_test()    # test from agent_test.py
    java_health_result = java_like_healthcheck() # test from java_client_sim.py

    return {
        "client": client_lang,
        "core_test": core_result,
        "sample_test": {
            "status": "passed" if simple_test_result else "failed"
        },
        "java_healthcheck_test": {
            "status": "passed" if java_health_result else "failed"
        }
    }

# 🔹 3. Healthcheck endpoint – confirms the API is running
@app.get(
    "/healthcheck",
    summary="Health check",
    description="Returns 200 OK if the API is running."
)
def healthcheck():
    return {"status": "ok"}