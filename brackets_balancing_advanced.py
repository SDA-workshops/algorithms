def validate(sequence: str) -> bool:
    stack = []
    openers = {"(", "[", "{"}
    closers = {")", "]", "}"}
    mapping = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    for ch in sequence:
        if ch in openers:
            stack.append(ch)
        elif ch in closers:
            if len(stack) == 0:
                return False
            last_ch = stack.pop()
            if last_ch != mapping[ch]:
                return False
        else:
            if len(stack) == 0 or stack[-1] != ch:
                stack.append(ch)
            else:
                stack.pop()
    return len(stack) == 0


if __name__ == "__main__":
    assert validate("[({||})||||]") is True
