class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        final=[]
        self.helper(0, candidates, target, [], final)
        return final

    def helper(self, ind, candidates, target, res, final):
        if target==0:
            final.append(res[:])
            return 
        if target<0:
            return
        for i in range(ind, len(candidates)):
            if i>ind and candidates[i]==candidates[i-1]:
                continue
            res.append(candidates[i])
            self.helper(i+1, candidates, target-candidates[i], res, final)
            res.pop()            