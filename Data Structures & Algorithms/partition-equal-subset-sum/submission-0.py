class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        
        #target = sum//2
        #brute force checks e ery possible subset and if it equals number dfs
        #onlu even should be possible 
        #running sum 
        #can only have even if can partition two sums

        dp = {0}

        if not nums:
            return False
        
        if sum(nums)%2 !=0:
            return False
        
        target = sum(nums)//2

        for num in nums:
            newDp = dp.copy() #dont modify dp as u go bc has new subsets so need copy of dp
            for s in dp:
                if s+ num == target:
                    return True
                elif s+ num<= target:
                    newDp.add(s+num)

            dp = newDp
        return False