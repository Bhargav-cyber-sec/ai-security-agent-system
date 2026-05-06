from tools.virustotal_tool import check_ip_reputation

def ip_agent_handler(query: str):
    # Extract IP safely
    import re
    match = re.search(r"(\\d+\\.\\d+\\.\\d+\\.\\d+)", query)

    if not match:
        return "No valid IP found in query."

    ip = match.group(1)

    result = check_ip_reputation(ip)

    return f"IP Analysis:\n{result}"