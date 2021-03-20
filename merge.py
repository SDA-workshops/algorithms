from typing import Tuple


def merge(left: list, right: list) -> list:
    print(f"Merging {left} {right}")
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    result = []
    size1, size2 = len(left), len(right)
    i, j = 0, 0
    while i < size1 and j < size2:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        elif left[i] > right[j]:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def partition(data: list) -> Tuple[list, list]:
    middle = len(data) // 2
    left, right = data[:middle], data[middle:]
    print(f"Partitioning of {data} to {left} {right}")
    return left, right


def sort(data: list) -> list:
    if len(data) in [0, 1]:
        return data
    left, right = partition(data)
    return merge(sort(left), sort(right))


if __name__ == "__main__":
    result = sort([10, 13, 11, 22, 4])
    print(result)
