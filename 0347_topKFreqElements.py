'''
Runtime: 134 ms, faster than 59.94% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 18.8 MB, less than 51.93% of Python3 online submissions for Top K Frequent Elements.
'''
import collections
def topKFrequent(nums: list, k: int) -> list:
    c = collections.Counter()
    ans = []
    if len(nums) == 0:
        return ans
    for idx in range(len(nums)):
        c[nums[idx]] += 1
    tmp = [[k, v] for k, v in c.items()]
    tmp.sort(key = lambda x: x[1])
    
    while len(ans) < k:
        ans.append(tmp.pop()[0])
    return ans

nums = [1, 1, 1, 2, 2, 3]
k = 2

print(topKFrequent(nums, k))