# 112

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution in recurrsive way
class Solution1:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: return False

        def dfsFindPath(node, prevSum):
            newSum = prevSum + node.val

            if node.left is None and node.right is None: return newSum == targetSum
            if node.left is not None and dfsFindPath(node.left, newSum): return True
            if node.right is not None and dfsFindPath(node.right, newSum): return True
            return False

        return dfsFindPath(root, 0)

# Soluition in iterative way
class Solution2:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: return False

        stack = [(root, 0), ]
        while stack:
            node, prevSum = stack.pop()
            newSum = prevSum + node.val

            if node.left is None and node.right is None and newSum == targetSum: return True
            if node.left is not None: stack.append((node.left, newSum))
            if node.right is not None: stack.append((node.right, newSum))

        return False

