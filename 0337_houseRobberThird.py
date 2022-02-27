'''
'''
import collections
'''
https://leetcode.com/problems/house-robber-iii/discuss/79330/Step-by-step-tackling-of-the-problem
** Fine problem tearing down process
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:       
    '''
    Runtime: 52 ms, faster than 86.59% of Python3 online submissions for House Robber III.
    Memory Usage: 16.7 MB, less than 31.89% of Python3 online submissions for House Robber III.
    '''
    # def rob(self, root: TreeNode) -> int:
    #     self.dp = collections.defaultdict(int)
    #     return self.robby(root)
    
    # def robby(self, root: TreeNode) -> int:
    #     if not root:
    #         return 0
    #     if root in self.dp.keys():
    #         return self.dp[root]

    #     val = root.val
    #     if root.left:
    #         val += self.robby(root.left.left) + self.robby(root.left.right)
    #     if root.right:
    #         val += self.robby(root.right.left) + self.robby(root.right.right)
    #     val = max(val, self.robby(root.left) + self.robby(root.right))
    #     self.dp[root] = val
    #     return val
    
    '''
    Runtime: 79 ms, faster than 41.26% of Python3 online submissions for House Robber III.
    Memory Usage: 16.2 MB, less than 50.54% of Python3 online submissions for House Robber III.
    '''
    def rob(self, root: TreeNode) -> int:
        return max(self.robby(root))
    
    def robby(self, root: TreeNode) -> int:
        if not root:
            return [0, 0]
        
        val = root.val
        rob_left = self.robby(root.left)
        rob_right = self.robby(root.right)
        
        return [max(rob_left) + max(rob_right), val + rob_left[0] + rob_right[0]]

root = TreeNode(3, TreeNode(2, None, TreeNode(3)), TreeNode(3, None, TreeNode(1)))
s = Solution()
print(s.rob(root))