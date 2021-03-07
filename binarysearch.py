from typing import List, Optional


def search(items: List[int], target: int) -> Optional[int]:
    left, right = 0, len(items) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if items[middle] == target:
            return middle
        if items[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return None


if __name__ == "__main__":
    data = list(range(1_000_000))
    assert search(data, 2_000_000) is None
    assert search(data, 10) == 10
    print("Success")
