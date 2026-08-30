class ListNode:

    def __init__(self, val) -> None:
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        cur = self.head.next

        while cur and index > 0:
            cur = cur.next
            index -= 1

        if cur and cur != self.tail and index == 0:
            return cur.val

        return -1 

    def addAtHead(self, val: int) -> None:
        tmp = self.head.next
        node = ListNode(val)
        self.head.next = node
        node.prev = self.head
        node.next = tmp
        tmp.prev = node
        
    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        tmp = self.tail.prev
        tmp.next = node
        node.next = self.tail
        node.prev = tmp
        self.tail.prev = node
        
    def addAtIndex(self, index: int, val: int) -> None:
        

        cur = self.head.next

        while cur and index > 0:
            cur = cur.next
            index -= 1
        
        if index == 0:
            node = ListNode(val)
            tmp = cur.prev

            cur.prev = node
            node.prev = tmp
            node.next = cur
            tmp.next = node

        

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head.next

        while cur and index > 0:
            cur = cur.next
            index -= 1
        
        if cur and cur != self.tail and index == 0:
            next, prev = cur.next, cur.prev
            next.prev = prev
            prev.next = next
            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)