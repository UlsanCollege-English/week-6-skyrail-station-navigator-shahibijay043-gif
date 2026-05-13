"""Weekly Coding — Royal Tree Archive."""

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


def preorder_values(
    root: TreeNode | None,
) -> list[Any]:

    if root is None:
        return []

    traversal_result = [root.value]

    traversal_result += preorder_values(root.left)

    traversal_result += preorder_values(root.right)

    return traversal_result


def inorder_values(
    root: TreeNode | None,
) -> list[Any]:

    if root is None:
        return []

    traversal_result: list[Any] = []

    traversal_result += inorder_values(root.left)

    traversal_result.append(root.value)

    traversal_result += inorder_values(root.right)

    return traversal_result


def postorder_values(
    root: TreeNode | None,
) -> list[Any]:

    if root is None:
        return []

    traversal_result: list[Any] = []

    traversal_result += postorder_values(root.left)

    traversal_result += postorder_values(root.right)

    traversal_result.append(root.value)

    return traversal_result


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