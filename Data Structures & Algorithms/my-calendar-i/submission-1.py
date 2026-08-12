class Tree:
    
    def __init__(self, start, end) -> None:
        self.left = None
        self.right = None
        self.start = start
        self.end = end


class MyCalendar:
    
    def __init__(self):
        self.root = None
    
    def _insert(self, node: Tree, start: int, end: int):
        if end <= node.start:
            if not node.left:
                node.left = Tree(start, end)
                return True
            return self._insert(node.left, start, end)
        elif start >= node.end:
            if not node.right:
                node.right = Tree(start, end)
                return True
            return self._insert(node.right, start, end)
        else:
            return False

        
    def book(self, startTime: int, endTime: int) -> bool:
        if not self.root:
            self.root = Tree(startTime, endTime)
            return True
        return self._insert(self.root, startTime, endTime)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)