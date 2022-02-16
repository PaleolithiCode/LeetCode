'''
Runtime: 79 ms, faster than 62.40% of Python3 online submissions for Add Two Numbers.
Memory Usage: 13.9 MB, less than 96.98% of Python3 online submissions for Add Two Numbers.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = ListNode()
        ans = ListNode(next = cur)
        remain = 0
        while(l1 or l2):
            if l1:
                remain += l1.val
                l1 = l1.next
            if l2:
                remain += l2.val
                l2 = l2.next
            cur.val = remain % 10
            if remain >= 10: remain = 1
            else: remain = 0
                
            if(l1 or l2 or remain != 0):
                newNode = ListNode()
                cur.next = newNode
                cur = cur.next
                
        if remain != 0:
            cur.val = remain
        return ans.next
            