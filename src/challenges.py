"""Weekly Coding #5 starter code: Trees, traversals, and BST basics."""

from __future__ import annotations

from typing import Any


class TreeNode:
    """A simple binary tree node."""

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
    """Return the tree values in preorder: node, left, right."""
    raise NotImplementedError("Implement preorder_values.")



def inorder_values(root: TreeNode | None) -> list[Any]:
    """Return the tree values in inorder: left, node, right."""
    raise NotImplementedError("Implement inorder_values.")



def postorder_values(root: TreeNode | None) -> list[Any]:
    """Return the tree values in postorder: left, right, node."""
    raise NotImplementedError("Implement postorder_values.")



def bst_contains(root: TreeNode | None, target: int) -> bool:
    """Return True if target exists in the BST. Otherwise return False."""
    raise NotImplementedError("Implement bst_contains.")



def bst_insert(root: TreeNode | None, value: int) -> TreeNode:
    """Insert value into the BST and return the root node.

    Duplicate values should be ignored.
    """
    raise NotImplementedError("Implement bst_insert.")
