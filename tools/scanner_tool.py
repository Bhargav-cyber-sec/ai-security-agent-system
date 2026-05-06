import re

def scan_code_with_lines(code: str):
    issues = []
    lines = code.split("\n")

    for i, line in enumerate(lines, start=1):

        # SQL Injection
        if re.search(r"(SELECT|INSERT|UPDATE|DELETE).*[\+].*", line, re.IGNORECASE):
            issues.append({
                "line": i,
                "severity": "HIGH",
                "issue": "Possible SQL Injection",
                "code": line.strip()
            })

        # Hardcoded credentials
        if re.search(r"(password|api_key|secret)\s*=\s*['\"].{4,}['\"]", line, re.IGNORECASE):
            issues.append({
                "line": i,
                "severity": "HIGH",
                "issue": "Hardcoded credentials",
                "code": line.strip()
            })

        # XSS
        if re.search(r"innerHTML\s*=", line):
            issues.append({
                "line": i,
                "severity": "MEDIUM",
                "issue": "Potential XSS",
                "code": line.strip()
            })

    return issues if issues else [{"message": "No vulnerabilities found"}]