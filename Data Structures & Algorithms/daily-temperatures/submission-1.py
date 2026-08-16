class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                prev_temp, prev_i = stack.pop()
                res[prev_i] = idx - prev_i

                    
            stack.append((temp, idx))
        return res
            




        