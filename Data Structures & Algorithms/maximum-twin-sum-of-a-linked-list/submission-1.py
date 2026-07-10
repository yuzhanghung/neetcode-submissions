# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head

        # find the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        #reverse the second half
        curr = slow
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        #compare
        res = 0
        first, second = head, prev
        while second:
            res = max(res, first.val + second.val)
            first = first.next
            second = second.next

        return res
