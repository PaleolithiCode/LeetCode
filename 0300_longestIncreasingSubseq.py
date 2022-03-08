def lengthOfLIS(nums: list) -> int:
    '''
    Runtime: 120 ms, faster than 81.41% of Python3 online submissions for Longest Increasing Subsequence.
    Memory Usage: 14.1 MB, less than 91.65% of Python3 online submissions for Longest Increasing Subsequence.
    '''
    # ans = []
    # for num in nums:
    #     if len(ans) == 0 or ans[-1] < num:
    #         ans.append(num)
    #     else: 
    #         for idx in range(len(ans)):
    #             if ans[idx] >= num:
    #                 ans[idx] = num
    #                 break
    #     print(ans)
    # return len(ans)
    '''
    Runtime: 3746 ms, faster than 60.39% of Python3 online submissions for Longest Increasing Subsequence.
    Memory Usage: 14.2 MB, less than 91.65% of Python3 online submissions for Longest Increasing Subsequence.
    '''
    dp = [1 for _ in range(len(nums))]
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    return max(dp)

nums = [0,1,0,3,2,3]
print(lengthOfLIS(nums))