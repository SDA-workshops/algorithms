from typing import List, Optional


class Node:
    def __init__(
        self,
        key: Optional[int],
        left: "Node" = None,
        right: "Node" = None
    ):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"Node({self.key})"

    def append(self, key: int) -> None:
        if self.key is None:
            self.key = key
            return
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


def create_binsearch_tree(root: Node, data: List[int]) -> Node:
    size = len(data)
    if size != 0:
        items = sorted(data)
        middle = size // 2
        root.append(items[middle])
        create_binsearch_tree(root, items[:middle])
        create_binsearch_tree(root, items[middle + 1:])
    return root


if __name__ == "__main__":
    data = [1, 2, 10, 9, 4, 10, 11, 100, -1]
    root = create_binsearch_tree(Node(key=None), data)
    root.traverse()
