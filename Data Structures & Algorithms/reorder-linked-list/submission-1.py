# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next


        stack = []
        cur = slow.next

        while cur:
            stack.append(cur)
            cur = cur.next

        slow.next = None

        cur = head
        while stack:
            node = stack.pop()

            nxt = cur.next
            cur.next = node
            node.next = nxt

            cur = nxt
        
         


        