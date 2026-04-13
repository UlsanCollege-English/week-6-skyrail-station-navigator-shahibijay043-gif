

from __future__ import annotations
from typing import Any


class TreeNode:
    def __init__(self, value: Any, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def preorder_values(root):
    if root is None:
        return []

    result = [root.value]

  
    result += preorder_values(root.left)

    result += preorder_values(root.right)

    return result


def inorder_values(root):
    if root is None:
        return []

    result = []

   
    result += inorder_values(root.left)

   
    result.append(root.value)

  
    result += inorder_values(root.right)

    return result



def postorder_values(root):
    if root is None:
        return []

    result = []

  
    result += postorder_values(root.left)
    result += postorder_values(root.right)

  
    result.append(root.value)

    return result



def bst_contains(root, target):
    current = root

    while current is not None:
        if current.value == target:
            return True

        if target < current.value:
            current = current.left
        else:
            current = current.right

    return False


def bst_insert(root, value):
 
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
      
            break

    return root