from analysis.trend import get_trend

def test_trend_up():
    assert get_trend([100, 120]) == "Up 📈"
