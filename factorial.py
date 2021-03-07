def factorial(n: int) -> int:
    if n in [0, 1]:
        return 1
    p = 1
    for i in range(2, n + 1):
        p *= i
    return p


def factorial2(n: int) -> int:
    if n in [0, 1]:
        return 1
    return n * factorial2(n - 1)


if __name__ == "__main__":
    print(factorial2(5))
