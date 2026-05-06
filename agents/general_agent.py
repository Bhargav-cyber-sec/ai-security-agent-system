def general_agent_handler(query: str):
    # Simple safe responses (no external API needed)
    
    if "sql injection" in query.lower():
        return (
            "SQL Injection is a vulnerability where attackers insert malicious SQL "
            "into queries. It happens when user input is directly concatenated into SQL queries.\n\n"
            "Example:\n"
            "query = \"SELECT * FROM users WHERE id=\" + user_input\n\n"
            "Prevention:\n"
            "- Use parameterized queries\n"
            "- Validate user input\n"
        )

    if "xss" in query.lower():
        return (
            "Cross-Site Scripting (XSS) allows attackers to inject malicious scripts "
            "into web pages.\n\n"
            "Example:\n"
            "element.innerHTML = userInput\n\n"
            "Prevention:\n"
            "- Escape output\n"
            "- Use safe DOM methods\n"
        )

    return "General query received. No security risk detected."