from typing import List


class Node:
    def __init__(
        self,
        key: int,
        left: "Node" = None,
        right: "Node" = None
    ):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"Node({self.key})"

    def append(self, key: int) -> None:
        if key < self.key:  # go to left subtree
            if self.left is None:
                self.left = Node(key=key)
            else:
                self.left.append(key)
        else:
            if self.right is None:
                self.right = Node(key=key)
            else:
                self.right.append(key)

    def traverse(self) -> None:
        print(self)
        if self.left is not None:
            self.left.traverse()
        if self.right is not None:
            self.right.traverse()


def traverse(root: Node) -> List[Node]:
    stack = [root]
    while stack:
        node = stack.pop()
        yield node
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)


if __name__ == "__main__":
    root = Node(key=42)

    root.append(40)
    root.append(50)
    root.append(30)
    root.append(60)
    root.append(70)

    for node in traverse(root):
        print(node)
