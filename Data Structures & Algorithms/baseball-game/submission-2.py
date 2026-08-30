class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "+":
                a, b = stack[-2], stack[-1]
                stack.append(a + b)
            
            elif op == "C":
                stack.pop()
            
            elif op == "D":
                a = stack[-1]
                stack.append(a * 2)
            else:
                stack.append(int(op))

        
        return sum(stack)
                
            
