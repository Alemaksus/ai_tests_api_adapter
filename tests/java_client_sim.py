import requests

def java_like_healthcheck():
    """
    Simulates a Java-style client calling the /healthcheck endpoint.
    In real Java code, this could be done using HttpURLConnection or HttpClient.
    """
    try:
        response = requests.get("http://127.0.0.1:8000/healthcheck", timeout=5)
        return response.status_code == 200 and response.json().get("status") == "ok"
    except Exception as e:
        print("Simulated Java client failed:", e)
        return False