class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack=[]
        for asteroid in asteroids:
            if asteroid>0:
                stack.append(asteroid)
            else:
                while stack and stack[-1]>0 and stack[-1]<abs(asteroid):
                    stack.pop()
                if stack and stack[-1]==abs(asteroid):
                    stack.pop()
                elif not stack or stack[-1]<0:
                    stack.append(asteroid)
        return stack