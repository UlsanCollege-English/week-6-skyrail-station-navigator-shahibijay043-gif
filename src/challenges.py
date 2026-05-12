from __future__ import annotations

from typing import Any


class TreeNode:
    def __init__(
        self,
        value: Any,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ) -> None:
        self.value = value
        self.left = left
        self.right = right


def preorder_values(root: TreeNode | None) -> list[Any]:

    if root is None:
        return []

    result = [root.value]

    result += preorder_values(root.left)

    result += preorder_values(root.right)

    return result


def inorder_values(root: TreeNode | None) -> list[Any]:

    if root is None:
        return []

    result = []

    result += inorder_values(root.left)

    result.append(root.value)

    result += inorder_values(root.right)

    return result


def postorder_values(root: TreeNode | None) -> list[Any]:

    if root is None:
        return []

    result = []

    result += postorder_values(root.left)

    result += postorder_values(root.right)

    result.append(root.value)

    return result


def bst_contains(
    root: TreeNode | None,
    target: Any,
) -> bool:

    current = root

    while current is not None:

        if current.value == target:
            return True

        if target < current.value:
            current = current.left

        else:
            current = current.right

    return False


def bst_insert(
    root: TreeNode | None,
    value: Any,
) -> TreeNode:

    if root is None:
        return TreeNode(value)

    current = root

    while True:

        if value < current.value:

            if current.left is None:
                current.left = TreeNode(value)
                break

            current = current.left

        elif value > current.value:

            if current.right is None:
                current.right = TreeNode(value)
                break

            current = current.right

        else:
            break

    return root