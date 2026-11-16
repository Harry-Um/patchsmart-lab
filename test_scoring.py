from scoring import cvss_points, severity_bonus, kev_bonus, days_bonus
from datetime import datetime
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

def test_days_bonus():
    now = datetime(2026, 7, 16, 0, 0, 0)
    assert days_bonus("2026-07-16T00:00:00.000", now) == 20
    assert days_bonus("2026-06-16T00:00:00.000", now) == 20
    assert days_bonus("2026-06-15T00:00:00.000", now) == 15
    assert days_bonus("2025-07-16T00:00:00.000", now) == 15
    assert days_bonus("2025-07-15T00:00:00.000", now) == 10
    assert days_bonus("2024-07-16T00:00:00.0000", now) == 10
    assert days_bonus("2024-07-15T00:00:00.000", now) == 0
    assert days_bonus("2016-07-18T00:00:00.000", now) == 0
    assert days_bonus(None, now) == 0
    assert days_bonus("2016-07-17T00:00:00.000", now) == -15
