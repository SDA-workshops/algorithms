import heapq


def heap_sort(items: list) -> list:
    size = len(items)
    heapq.heapify(items)
    return [heapq.heappop(items) for _ in range(size)]


def main():
    items = [27, 7, 38, 26, 4, 39, 34, 13, 35, 16]
    expected = sorted(items)

    result = heap_sort(items.copy())

    assert result == expected, f"{result} != {expected}"
    print(items)
    print(result)


if __name__ == "__main__":
    main()
