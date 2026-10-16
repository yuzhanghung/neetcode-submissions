class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0] * n

        prefix_count = [0] * (n + 1)
        index_sum = [0] * (n + 1)
        for i in range(n):
            prefix_count[i + 1] = prefix_count[i] + (boxes[i] == "1")
            index_sum[i + 1] = index_sum[i] + (i if boxes[i] == "1" else 0)


        for i in range(n):
            left = prefix_count[i]
            left_sum = index_sum[i]

            right = prefix_count[n] - prefix_count[i + 1]
            right_sum = index_sum[n] - index_sum[i + 1]

            res[i] = (i * left - left_sum) + (right_sum - i * right)
        
        return res
            


