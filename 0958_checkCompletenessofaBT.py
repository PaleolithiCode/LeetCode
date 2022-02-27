'''
Runtime: 28 ms, faster than 98.65% of Python3 online submissions for Check Completeness of a Binary Tree.
Memory Usage: 14 MB, less than 66.65% of Python3 online submissions for Check Completeness of a Binary Tree.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
            
def isCompleteTree(root: TreeNode) -> bool:
    preorder_traversal = [root]
    idx = 0
    while preorder_traversal[idx]:
        preorder_traversal.append(preorder_traversal[idx].left)
        preorder_traversal.append(preorder_traversal[idx].right)
        idx += 1
    return not any(preorder_traversal[idx:])
    
root = TreeNode(
    1,
    TreeNode(2, TreeNode(5)),
    TreeNode(3, TreeNode(7), TreeNode(8))
)

print(isCompleteTree(root))