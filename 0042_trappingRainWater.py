'''
Runtime: 76 ms, faster than 86.58% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 15.8 MB, less than 38.18% of Python3 online submissions for Trapping Rain Water.
'''
def trap(height: list):
    start, end = 0, len(height) - 1
    maxLeft = 0
    maxRight = 0
    ans = 0
    while start < end:
        if height[start] <= height[end]:
            if height[start] > maxLeft:
                maxLeft = height[start]
            else:
                ans += maxLeft - height[start]
            start += 1
        else:
            if height[end] > maxRight:
                maxRight = height[end]
            else:
                ans += maxRight - height[end]
            end -= 1
    return ans

height = [4,2,0,3,2,5]
print(trap(height))