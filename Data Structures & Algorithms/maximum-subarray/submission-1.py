class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        left = 0
        #right = 0
        curSum = 0
        globMax = float('-inf')

        while left < len(nums):
            #curSum += nums[left]
            curSum = max(nums[left], curSum +nums[left])
            if curSum > globMax:
                globMax = curSum
            left+=1
        
        return globMax
