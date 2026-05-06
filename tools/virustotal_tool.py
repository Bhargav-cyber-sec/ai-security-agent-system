import requests
import re
from config.settings import VIRUSTOTAL_API_KEY

BASE_URL = "https://www.virustotal.com/api/v3/ip_addresses/"

def is_valid_ip(ip):
    return re.match(r"^\d{1,3}(\.\d{1,3}){3}$", ip)

def check_ip_reputation(ip: str):
    if not is_valid_ip(ip):
        return {"error": "Invalid IP format"}

    try:
        response = requests.get(
            BASE_URL + ip,
            headers={"x-apikey": VIRUSTOTAL_API_KEY},
            timeout=5
        )

        if response.status_code != 200:
            return {"error": "API request failed"}

        data = response.json()
        attr = data.get("data", {}).get("attributes", {})

        return {
            "ip": ip,
            "malicious": attr.get("last_analysis_stats", {}).get("malicious", 0),
            "owner": attr.get("as_owner")
        }

    except Exception as e:
        return {"error": str(e)}