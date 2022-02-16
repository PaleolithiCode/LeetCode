'''
Runtime: 56 ms, faster than 95.46% of Python3 online submissions for Two Sum.
Memory Usage: 15.2 MB, less than 46.75% of Python3 online submissions for Two Sum.
'''
def twoSum(nums: list, target: int) -> list:
    num2idx = {}
    for idx, num in enumerate(nums):
        comp = target - num
        if comp in num2idx.keys():
            result = [idx, num2idx[comp]]
            break
        num2idx[num] = idx
        
    return result