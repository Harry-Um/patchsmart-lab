def cvss_points(cvss_score):
    if cvss_score is None:
        return 0
    return cvss_score * 10

print(cvss_points(9.8))
print(cvss_points(None))