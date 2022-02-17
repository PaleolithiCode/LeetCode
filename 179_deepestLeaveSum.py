'''
Runtime: 256 ms, faster than 63.84% of Python3 online submissions for Deepest Leaves Sum.
Memory Usage: 17.9 MB, less than 43.28% of Python3 online submissions for Deepest Leaves Sum.
'''
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def deepestLeavesSum(root : TreeNode) -> int:
    # value in the same depth
    depth2val = {}
    
    def dfs(root, self_depth = 1):
        l_depth = 0
        r_depth = 0
        if root.left != None:
            l_depth = 1 + dfs(root.left, self_depth + 1)
        else: l_depth = 1
        if root.right != None: 
            r_depth = 1 + dfs(root.right, self_depth + 1)
        else: r_depth = 1
        if self_depth not in depth2val.keys():
            depth2val[self_depth] = []
        depth2val[self_depth].append(root.val)
        return max(l_depth, r_depth)

    return sum(depth2val[dfs(root)])
    
root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(7)), TreeNode(5)), TreeNode(3, None, TreeNode(6, None, TreeNode(8))))

print(deepestLeavesSum(root))