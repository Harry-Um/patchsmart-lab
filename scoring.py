from datetime import datetime

def cvss_points(cvss_score):
    if cvss_score is None:
        return 0
    return cvss_score * 10

def severity_bonus(severity):
    if severity == "CRITICAL":
        return 10
    elif severity == "HIGH":
        return 5
    elif severity == "MEDIUM":
        return 2
    elif severity == "LOW":
        return 0
    else:
        return 0

def kev_bonus(is_kev):
    if is_kev:
        return 30
    else:
        return 0

def days_bonus(published, now=None):
    if now is None:
        now = datetime.now()
    if published is None:
        return 0
    days = (now - datetime.fromisoformat(published)).days
    if days <= 30:
        return 20
    elif days <= 365:
        return 15
    elif days <= 730:
        return 10
    elif days <= 3650:
        return 0
    else:
        return -15

def v2_penalty(cvss_version):
     if cvss_version == "2.0":
         return -5
     elif cvss_version == "3.1":
         return 0
     elif cvss_version == "4.0":
         return 0
     else:
         return 0

