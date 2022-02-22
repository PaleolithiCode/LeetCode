'''
Runtime: 183 ms, faster than 14.54% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.2 MB, less than 90.98% of Python3 online submissions for Median of Two Sorted Arrays.
'''
def findMedianSortedArrays(nums1: list, nums2: list) -> float:
    def notNull(num):
        if num == None: return False
        return True
    
    boundary = int((len(nums1) + len(nums2)) / 2)
    if len(nums1) + len(nums2) == 0:
        return 0
    mergedList = []
    idx_1 = 0
    idx_2 = 0
    while(1):
        num1 = nums1[idx_1] if idx_1 < len(nums1) else None
        num2 = nums2[idx_2] if idx_2 < len(nums2) else None
        if notNull(num1) and notNull(num2) and num1 >= num2:
            mergedList.append(num2)
            idx_2 += 1
        elif notNull(num1) and num2 and num2 > num1:
            mergedList.append(num1)
            idx_1 += 1
        elif notNull(num1) and not num2:
            mergedList.append(num1)
            idx_1 += 1
        elif notNull(num2) and not num1:
            mergedList.append(num2)
            idx_2 += 1
        if len(mergedList) == boundary + 1: break

    if (len(nums1) + len(nums2)) % 2 == 0:
        return (mergedList[boundary] + mergedList[boundary - 1]) / 2
    else:
        return mergedList[boundary]