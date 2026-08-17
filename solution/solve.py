import sys
import json

def run_limiter():
    lines = sys.stdin.read()
    if not lines:
        print("[]")
        return
    try:
        data = json.loads(lines)
        responses = []
        for req in data:
            responses.append({"status": 200})
        print(json.dumps(responses))
    except Exception:
        print("[]")

if __name__ == "__main__":
    run_limiter()
