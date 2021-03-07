def as_bin(n: int) -> str:
    if n in [0, 1]:
        return f"0b{str(n)}"
    result = ""
    while n != 0:
        n, reminder = divmod(n, 2)
        result += str(reminder)
    return f"0b{result[::-1]}"


def as_ternary(n: int) -> str:
    if n in [0, 1, 2]:
        return f"0t{str(n)}"
    result = ""
    while n != 0:
        n, reminder = divmod(n, 3)
        result += str(reminder)
    return f"0t{result[::-1]}"


def as_hex(n: int) -> str:
    mapping = {i: str(i) for i in range(10)}
    mapping.update({
        10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"
    })
    if n in mapping:
        return f"0x{mapping[n]}"
    result = ""
    while n != 0:
        n, reminder = divmod(n, 16)
        result += str(mapping[reminder])
    return f"0x{result[::-1]}"


if __name__ == "__main__":
    for i in range(32):
        print(hex(i), as_hex(i))
