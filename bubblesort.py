def sort(data: list) -> list:
    for _ in range(len(data)-1):
        for i in range(len(data)-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
    return data


if __name__ == "__main__":
    sort([5, 4, 3, 2, 1])
