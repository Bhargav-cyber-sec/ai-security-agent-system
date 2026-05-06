import re
from agents.ip_agent import ip_agent_handler
from agents.code_agent import code_agent_handler
from agents.general_agent import general_agent_handler


def route_query(user_input: str):
    text = user_input.lower()

    # IP detection
    if re.search(r"\b\d{1,3}(\.\d{1,3}){3}\b", text):
        return ip_agent_handler(user_input)

    # Code detection
    code_indicators = [
        "=", "select", "insert", "update", "delete",
        "function", "const", "let", "{", "}"
    ]

    if any(ind in text for ind in code_indicators):
        return code_agent_handler(user_input)

    # ✅ NEW: fallback to general agent
    return general_agent_handler(user_input)
