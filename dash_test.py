from dash import to_usd

def test_to_usd():
    assert to_usd(5) == "$5.00"

    assert to_usd(3.889) == "$3.89"

    assert to_usd(3.8) =="$3.80"