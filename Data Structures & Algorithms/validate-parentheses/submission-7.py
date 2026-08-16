class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            "]" : "[",
            ")" : "(",
            "}" : "{"
        }

        stack = []

        for b in s:
            if b in closeToOpen:
                if not stack or stack.pop() != closeToOpen[b]:
                    return False
            else:
                stack.append(b)

        return not stack
