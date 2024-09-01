class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        maxsum=0
        leftsum=0
        rightsum=0
        for i in range(k):
            leftsum+=cardPoints[i]
        maxsum=leftsum
        right=len(cardPoints)-1
        for i in range(k-1,-1,-1):
            leftsum-=cardPoints[i]
            rightsum+=cardPoints[right]
            maxsum=max(maxsum,leftsum+rightsum)
            right-=1
        return maxsum
        