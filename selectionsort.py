def sort(data: list) -> list:
    for pos in range(len(data)):
        min_idx = pos
        for i in range(pos + 1, len(data)):
            if data[i] <= data[min_idx]:
                min_idx = i
        data[pos], data[min_idx] = data[min_idx], data[pos]
    return data


def sort2(data: list) -> list:
    items = [item for item in data]
    result = []
    while len(items) != 0:
        element = min(items)
        result.append(element)
        items.remove(element)
    return result


if __name__ == "__main__":
    result = sort2([10, 1, 4, 9, 20, 15])
    print(result)
