class Stack:
    def __init__(self):
        self._stack = []

    def push(self, key: int) -> None:
        self._stack.append(key)

    def pop(self) -> int:
        if not self._stack:
            raise Exception("Stack is empty")
        return self._stack.pop()

    def peek(self) -> int:
        if not self._stack:
            raise Exception("Stack is empty")
        return self._stack[-1]


if __name__ == "__main__":
    stack = Stack()
    for key in range(3):
        stack.push(key)

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
