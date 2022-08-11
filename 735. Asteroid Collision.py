class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        while asteroids:
            if not ans:
                ans.append(asteroids.pop())
            elif ans[-1] > 0:
                ans.append(asteroids.pop())
            else:
                if asteroids[-1] < 0:
                    ans.append(asteroids.pop())
                elif -ans[-1] > asteroids[-1]:
                    asteroids.pop()
                elif -ans[-1] == asteroids[-1]:
                    asteroids.pop()
                    ans.pop()
                elif -ans[-1] < asteroids[-1]:
                    ans.pop()
        return ans[::-1]