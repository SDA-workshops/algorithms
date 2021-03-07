from collections import deque


class Queue:
    def __init__(self):
        self._queue = deque()

    def enqueue(self, key: int) -> None:
        self._queue.append(key)

    def dequeue(self) -> int:
        if not self._queue:
            raise Exception("Queue is empty")
        return self._queue.popleft()


if __name__ == "__main__":
    queue = Queue()
    for key in range(10):
        queue.enqueue(key)

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
