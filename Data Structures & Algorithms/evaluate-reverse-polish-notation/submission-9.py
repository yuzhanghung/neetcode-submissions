class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0

        for op in tokens:
            if op not in "+-*/":
                stack.append(int(op))
            else:
                a, b = stack.pop(), stack.pop()
                if op == "+":
                    res = (a + b)
                elif op == "-":
                    res = (b - a)
                elif op == "*":
                    res = (b * a)
                else:
                    res = int(b / a)
                stack.append(res)
        return int(stack[0])