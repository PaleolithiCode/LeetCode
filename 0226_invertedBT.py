'''
Runtime: 32 ms, faster than 84.48% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 13.9 MB, less than 84.76% of Python3 online submissions for Invert Binary Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree( self, root: TreeNode) -> TreeNode:
    if not root:
        return root
    if not root.left and not root.right:
        return root
    
    def invert(root):
        tmp = root.left
        root.left = root.right
        root.right = tmp
        return root
    
    root.left = invertTree(root.left)
    root.right = invertTree(root.right)
    return invert(root)
    
root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
invertTree(root)