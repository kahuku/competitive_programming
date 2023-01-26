class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if asteroid > 0 or not stack:
                stack.append(asteroid)
            else:
                while stack and stack[-1] > 0 and stack[-1] < -1 * asteroid:
                    stack.pop()
                if stack and stack[-1] == -1 * asteroid:
                    stack.pop()
                else:
                    if not stack or stack[-1] < 0:
                        stack.append(asteroid)
        return stack