from scoring import cvss_points, severity_bonus, kev_bonus

def test_cvss_points():
    assert cvss_points(9.8) == 98.0
    assert cvss_points(None) == 0

def test_severity_bonus():
    assert severity_bonus("CRITICAL") == 10
    assert severity_bonus("HIGH") == 5
    assert severity_bonus("MEDIUM") == 2
    assert severity_bonus("LOW") == 0
    assert severity_bonus(None) == 0

def test_kev_bonus():
    assert kev_bonus(True) == 30
    assert kev_bonus(False) == 0