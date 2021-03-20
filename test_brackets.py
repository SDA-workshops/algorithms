import pytest


def validate(sequence: str) -> bool:
    counter = 0
    for ch in sequence:
        if ch == "(":
            counter += 1
        else:
            counter -= 1
        if counter < 0:
            return False
    return counter == 0


@pytest.mark.parametrize(
    "case,expected",
    [
        ("(())", True),
        ("(()())", True),
        ("()()", True),
        ("))((", False),
        ("())", False),
        ("((()", False)
    ]
)
def test_validate(case: str, expected: bool) -> None:
    assert validate(case) == expected
