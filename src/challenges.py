"""Weekly Coding #5"""

from __future__ import annotations
from typing import Any


class TreeNode:
    def __init__(self, value: Any, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# preorder: root -> left -> right
def preorder_values(root):
    if root is None:
        return []

    result = [root.value]

    # go left first
    result += preorder_values(root.left)

    # then go right
    result += preorder_values(root.right)

    return result


# inorder: left -> root -> right
def inorder_values(root):
    if root is None:
        return []

    result = []

    # left side
    result += inorder_values(root.left)

    # current node
    result.append(root.value)

    # right side
    result += inorder_values(root.right)

    return result


# postorder: left -> right -> root
def postorder_values(root):
    if root is None:
        return []

    result = []

    # visit children first
    result += postorder_values(root.left)
    result += postorder_values(root.right)

    # then add root
    result.append(root.value)

    return result


# search value in BST
def bst_contains(root, target):
    current = root

    while current is not None:
        if current.value == target:
            return True

        # decide direction
        if target < current.value:
            current = current.left
        else:
            current = current.right

    return False


# insert value into BST
def bst_insert(root, value):
    # if tree empty
    if root is None:
        return TreeNode(value)

    current = root

    while True:
        if value < current.value:
            if current.left is None:
                current.left = TreeNode(value)
                break
            else:
                current = current.left

        elif value > current.value:
            if current.right is None:
                current.right = TreeNode(value)
                break
            else:
                current = current.right

        else:
            # already exists, ignore
            break

    return root