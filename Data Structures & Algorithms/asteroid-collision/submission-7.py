class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            alive = True

            while a < 0 and len(stack) > 0 and stack[-1] > 0:
                if abs(a) > stack[-1]:
                    stack.pop()

                elif abs(a) == stack[-1]:
                    stack.pop()
                    alive = False
                    break

                else:
                    alive = False
                    break

            if alive:
                stack.append(a)

        return stack