class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = [0] * len(boxes) 
        

        for i in range(len(boxes)):
            move = 0
            for j in range(0, len(boxes)):
                if boxes[j] == "1":
                    move += abs(i - j)
                res[i] = move

        return res