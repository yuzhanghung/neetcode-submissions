class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        balls = 0
        moves = 0
        n = len(boxes)

        res = [0] * n

        for i in range(n):
            res[i] = balls + moves
            moves += balls
            if boxes[i] == "1":
                balls += 1
        
        balls = 0
        moves = 0
        
        for i in range(n - 1, -1, -1):
            res[i] += balls + moves
            moves += balls
            if boxes[i] == "1":
                balls += 1
           
        
        return res
        