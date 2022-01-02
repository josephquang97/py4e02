import pytest


FILE = "./main.py"
def test_accept():
    assert 1==1

def test_hours():
    astval = False
    fh = open(FILE,'r',encoding='utf-8')
    content = fh.read().split('\n')
    for line in content:
        if line.startswith("hours"):
            if 'input' in line: astval = True
    assert astval

def test_rate():
    astval = False
    fh = open(FILE,'r',encoding='utf-8')
    content = fh.read().split('\n')
    for line in content:
        if line.startswith("rate"):
            if 'input' in line: astval = True
    assert astval


@pytest.mark.parametrize(
    "hours, rate, expected",
    [
        # ("39", "3", 117.0),
        # ("40", "3", 120.0),
        ("41", "3", 124.5),
    ],
)
def test_price(hours, rate, expected, monkeypatch):
    import io
    monkeypatch.setattr('sys.stdin', io.StringIO(f'{hours}\n{rate}'))
    import main
    result = main.price
    assert result==expected
