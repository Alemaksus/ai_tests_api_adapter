from fastapi import FastAPI
from tests.core_test import run_ai_agent_test

app = FastAPI(title="AI Agent Test API", version="1.0")

@app.get("/run-test/{client_lang}", summary="Run AI agent test", description="Runs an example AI agent test and returns the result with client language")
def run_test(client_lang: str):
    result = run_ai_agent_test()
    result["client"] = client_lang
    return result