# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        res = 0

        while l1 != None and l2 != None:
            val = l1.val + l2.val
            if res == 1:
                val += 1

            if val >= 10:
                res = 1
                val -= 10
            else:
                res = 0

            cur.next = ListNode(val)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        while l1 != None:
            val = l1.val
            if res == 1:
                val += 1
            
            if val >= 10:
                res = 1
                val -= 10
            else:
                res = 0
            cur.next = ListNode(val)
            cur = cur.next

            l1 = l1.next
        
        while l2 != None:
            val = l2.val
            if res == 1:
                val += 1
            
            if val >= 10:
                res = 1
                val -= 10
            else:
                res = 0
            cur.next = ListNode(val)
            cur = cur.next

            l2 = l2.next

        if res == 1:
            cur.next = ListNode(1)

        return dummy.next
        


            
            
            




        