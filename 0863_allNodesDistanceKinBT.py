'''
Runtime: 36 ms, faster than 92.95% of Python3 online submissions for All Nodes Distance K in Binary Tree.
Memory Usage: 14.5 MB, less than 62.33% of Python3 online submissions for All Nodes Distance K in Binary Tree.
'''
import collections
class TreeNode:
    def __init__(self, x=0, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
        
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list:
        edge_lst = collections.defaultdict(list)
        self.parent = None
        def dfs(root):
            if not root.left and not root.right:
                return
            if root.left:
                edge_lst[root.val].append(root.left.val)
                edge_lst[root.left.val].append(root.val)
                dfs(root.left)
            if root.right:
                edge_lst[root.val].append(root.right.val)
                edge_lst[root.right.val].append(root.val)
                dfs(root.right)
            return
        seen = set()
        dfs(root)
        cur = [target.val]
        while k > 0:
            next_cur = []
            for node in cur:
                for n in edge_lst[node]:
                    # Must be remembered : can't trace back during traversal
                    if n != target.val and ((n, node) not in seen):
                        next_cur.append(n)
                        seen.add((n, node))
                        seen.add((node, n))
            cur = next_cur
            k -= 1
        return cur
    
root = TreeNode(
    3,
    TreeNode(5,TreeNode(6),TreeNode(2, TreeNode(7), TreeNode(4))),
    TreeNode(1, TreeNode(0), TreeNode(8))
)

root = TreeNode(
    0,
    TreeNode(2),
    TreeNode(1, TreeNode(3))
)

target = TreeNode(5,TreeNode(6),TreeNode(2, TreeNode(7), TreeNode(4)))
target = TreeNode(3)
k = 3
s = Solution()
print(s.distanceK(root, target, k))