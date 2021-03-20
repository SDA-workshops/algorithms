class Heap:
    def __init__(self):
        self._data = []

    @property
    def data(self) -> list:
        return self._data

    @data.setter
    def data(self, new_data: list) -> None:
        self._data = new_data

    @property
    def size(self):
        return len(self._data)

    def append(self, value: int) -> None:
        self._data.append(value)
        self._siftup(self.size - 1)

    def _siftup(self, n: int) -> None:
        while n > 0 and self._data[n] < self._data[n // 2]:
            self._data[n], self._data[n // 2] = self._data[n // 2], self._data[n]
            n //= 2

    def peak(self) -> int:
        return self._data[0]

    def pop(self) -> int:
        if self.size > 1:
            result = self.peak()
            self._data[0] = self._data.pop()
            self._siftdown(0)
            return result
        return self.data.pop()

    def _siftdown(self, n: int) -> None:
        size = self.size
        while 2 * n + 1 < size:
            j = n
            if self._data[2 * n + 1] < self._data[j]:
                j = 2 * n + 1
            if 2 * n + 2 < size and self._data[2 * n + 2] < self._data[j]:
                j = 2 * n + 2
            if j == n:
                break
            self._data[n], self._data[j] = self._data[j], self._data[n]
            n = j

    def heapify(self, data: list) -> None:
        self.data = data
        for i in reversed(range(self.size)):
            self._siftup(i)


def heapify(data: list) -> list:
    h = Heap()
    for item in data:
        h.append(item)
    return h.data


def heap_sort(items: list) -> list:
    heap = Heap()
    for item in items:
        heap.append(item)
    return [heap.pop() for _ in range(heap.size)]


def main():
    items = [27, 7, 38, 26, 4, 39, 34, 13, 35, 16]
    expected = sorted(items)

    result = heap_sort(items.copy())

    assert result == expected, f"{result} != {expected}"
    print(items)
    print(result)


if __name__ == "__main__":
    main()
