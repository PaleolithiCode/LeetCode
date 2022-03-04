'''
Runtime: 204 ms, faster than 39.31% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
Memory Usage: 88.7 MB, less than 22.61% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(inorder: list, postorder: list) -> TreeNode:
    '''
    inorder: LDR
    postorder: LRD
    '''
    if not postorder or not inorder:
        return None
    root = postorder.pop()
    idx = inorder.index(root)
    return TreeNode(root, buildTree(inorder[:idx], postorder[:idx]), buildTree(inorder[idx + 1:], postorder[idx:]))

    '''
    How to optimize it?
    '''
    # map_inorder = {}
    # for i, val in enumerate(inorder): map_inorder[val] = i
    # def recur(low, high):
    #     if low > high: return None
    #     x = TreeNode(postorder.pop())
    #     mid = map_inorder[x.val]
    #     x.right = recur(mid+1, high)
    #     x.left = recur(low, mid-1)
    #     return x
    # return recur(0, len(inorder)-1)


inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
buildTree(inorder, postorder)
