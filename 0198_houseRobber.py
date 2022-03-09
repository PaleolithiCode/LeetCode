'''
Runtime: 41 ms, faster than 62.11% of Python3 online submissions for House Robber.
Memory Usage: 13.9 MB, less than 81.31% of Python3 online submissions for House Robber.
'''
class Solution:
    def rob(self, nums):
        if len(nums) == 1: return nums[0]
        dp = [*nums]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        return dp[-1]