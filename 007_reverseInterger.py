'''
Runtime: 54 ms, faster than 29.32% of Python3 online submissions for Reverse Integer.
Memory Usage: 13.9 MB, less than 90.13% of Python3 online submissions for Reverse Integer.
'''
def reverse(x: int) -> int:
    holder = str(x)
    if holder[0] == '-': 
        num = holder[1:][::-1]
        result = -1 * int(num)
        if result < -(2**31): return 0
        else: return result
    else:
        result = int(holder[::-1])
        if result > 2**31 - 1: return 0
        else: return int(holder[::-1])
    