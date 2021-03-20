import random


def sort(data: list, left: int, right: int) -> list:
    print(f"Initial state {data}")
    if left >= right:
        return data

    pivot = data[random.randint(left, right)]
    i, j = left, right
    while i <= j:
        while data[i] < pivot:
            i += 1
        while data[j] > pivot:
            j -= 1
        if i <= j:
            data[i], data[j] = data[j], data[i]
            i += 1
            j -= 1

    print(f"pivot = {pivot} {data}")
    sort(data, left, j)
    sort(data, i, right)

    return data


def quick_sort(data: list) -> list:
    return sort(data, 0, len(data)-1)


if __name__ == "__main__":
    data = [11, 6, 1]
    result = quick_sort(data)
    print(result)
