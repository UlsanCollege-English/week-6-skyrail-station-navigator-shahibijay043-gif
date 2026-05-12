[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/mHMwxQwH)
# Weekly Coding #5: Skyrail Station Navigator

## Summary
This program uses binary trees and binary search trees (BSTs) to manage station data.  
The assignment includes recursive tree traversals using preorder, inorder, and postorder methods.  
It also includes BST operations for searching and inserting values into the tree.  
The program practices recursion, tree navigation, and BST rules for storing data correctly.

---

## Approach

- For preorder traversal, I visited the root node first, then recursively visited the left subtree and right subtree.

- For inorder traversal, I first visited the left subtree, then the root node, and finally the right subtree.

- For postorder traversal, I recursively visited the left subtree and right subtree before visiting the root node.

- For BST search, I compared the target value with the current node value and moved left or right depending on the comparison.

- For BST insert, I followed BST rules by inserting smaller values to the left and larger values to the right. Duplicate values were ignored.

---

## Complexity

### `preorder_values`
- **Time:** O(n)
- **Space:** O(n)
- **Why:** Every node is visited once and recursion uses stack space.

### `inorder_values`
- **Time:** O(n)
- **Space:** O(n)
- **Why:** Each node is visited once during traversal.

### `postorder_values`
- **Time:** O(n)
- **Space:** O(n)
- **Why:** The traversal processes every node recursively.

### `bst_contains`
- **Time:** O(h)
- **Space:** O(1)
- **Why:** The search only follows one path through the tree.

### `bst_insert`
- **Time:** O(h)
- **Space:** O(1)
- **Why:** The insert operation follows one path until an empty position is found.

---

## Edge-Case Checklist

- [x] Empty tree traversal returns `[]`
- Traversal functions return an empty list when the tree is empty.

- [x] Single-node traversal works correctly
- Traversals correctly return the single value in the tree.

- [x] `bst_contains` returns `False` for an empty tree
- The search loop ends immediately when the tree is empty.

- [x] `bst_contains` returns `False` when the target is missing
- The function checks nodes until it reaches `None`.

- [x] `bst_insert` creates a root when the tree is empty
- A new `TreeNode` is created and returned as the root.

- [x] `bst_insert` ignores duplicate values
- Duplicate values are skipped and not inserted again.

- [x] I tested at least one deeper insert case
- Tested inserting values multiple levels deep into the BST.

---

## Assistance & Sources

- **AI used? (Y/N):** Yes

- **What AI helped with:**
  - Reviewing recursion logic
  - Checking BST insert and search logic
  - Improving formatting and explanations

- **Other sources used:**
  - Python documentation
  - Class lecture notes

---

## Test Results

All pytest tests passed successfully.

Example:

```bash
pytest -q
15 passed