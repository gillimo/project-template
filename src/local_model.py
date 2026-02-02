import time

LAST_REQUEST_AT = 0.0
MIN_INTERVAL_S = 2.0


def build_prompt(state, user_message):
    account = state.get("account", {})
    name = account.get("name", "Unknown")
    return f"You are an <project_name>. Account: {name}. User says: {user_message}"


def run_local_model(prompt, timeout_s=10):
    # Placeholder for local model integration with basic rate limit.
    global LAST_REQUEST_AT
    now = time.time()
    if now - LAST_REQUEST_AT < MIN_INTERVAL_S:
        return "Rate limit: wait a moment before asking again."
    LAST_REQUEST_AT = now
    time.sleep(0.1)
    return "Local model not configured. Update src/local_model.py."

