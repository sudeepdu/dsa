class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        final=[]
        self.helper(0, candidates, target, [], final)
        return final
    
    def helper(self, i, candidates, target, res, final):
        if i==len(candidates):
            if target==0:
                final.append(res[:])
            return
        if candidates[i]<=target:
            res.append(candidates[i])
            self.helper(i, candidates, target-candidates[i], res, final)
            res.pop()
        self.helper(i+1, candidates, target, res, final)