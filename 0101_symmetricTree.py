'''
Runtime: 56 ms, faster than 34.59% of Python3 online submissions for Symmetric Tree.
Memory Usage: 14 MB, less than 77.50% of Python3 online submissions for Symmetric Tree.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def equivalent(r1, r2):
            if not r1 and not r2:
                return True
            if not r1 or not r2:
                return False
            return r1.val == r2.val and equivalent(r1.right, r2.left) and equivalent(r1.left, r2.right)
        if not root.left and not root.right:
            return True
        
        return equivalent(root.left, root.right)
