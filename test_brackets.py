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


if __name__ == "__main__":
    assert validate("(()())") is True
    assert validate("()()") is True
    assert validate("(())") is True
    assert validate("(()))") is False
    assert validate("((())") is False
    assert validate("))((") is False
    assert validate("((((") is False
    assert validate("))))") is False
