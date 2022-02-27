'''
Runtime: 713 ms, faster than 47.93% of Python3 online submissions for Subarrays with K Different Integers.
Memory Usage: 17.4 MB, less than 30.23% of Python3 online submissions for Subarrays with K Different Integers.
'''
import collections

def subarraysAtMostKDistinct(nums, k):
    count = collections.Counter()
    res = i = 0
    
    # take j as the right pointer (boundary on the right)
    for j in range(len(nums)):
        # first time seen: count it as one of k
        if count[nums[j]] == 0: 
            k -= 1
        
        # count it
        count[nums[j]] += 1
        
        # constraint is broken, adjust i, the left pointer (boundary on the left)
        while k < 0:
            count[nums[i]] -= 1
            # make sure that only at most k distinct in the interval
            if count[nums[i]] == 0:
                k += 1
                
            # in any case, i must be move forward because of broken constraint
            i += 1
        res += j - i + 1
    return res

def subarraysWithKDistinct(nums: list, k: int) -> int:
    return subarraysAtMostKDistinct(nums, k) - subarraysAtMostKDistinct(nums, k - 1)

        
nums = [1, 2, 1, 2, 3]
k = 2
subarraysWithKDistinct(nums, k)