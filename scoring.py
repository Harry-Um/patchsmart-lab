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
