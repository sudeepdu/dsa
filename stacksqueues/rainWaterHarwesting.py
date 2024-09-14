#Actually it is two pointers approach
#Try to solve using stacks and queues
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        left, right = 0, n-1
        leftmax, rightmax = 0, 0
        result=0
        while left<=right:
            if height[left]<height[right]:
                if height[left]<leftmax:
                    result+=leftmax-height[left]
                else:
                    leftmax=height[left]
                left+=1
            else:
                if height[right]<rightmax:
                    result+=rightmax-height[right]
                else:
                    rightmax=height[right]
                right-=1
        return result