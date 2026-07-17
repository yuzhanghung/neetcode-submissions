class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openToClose = {'}': '{', ']': '[', ')': '('}

        for c in s:
            if c in openToClose:
                if stack and openToClose[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:

                stack.append(c)

        return True if len(stack) == 0 else False