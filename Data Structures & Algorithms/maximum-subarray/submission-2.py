class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        l = 0

        curr = 0
        best = float('inf')

        #running sum-> look at if ecah invidivudal element improves total or no
        #greedy 

        while l<len(nums):
            curr= max(nums[l], curr + nums[l]) #running sum
            best = max(best, curr) #best sum
            l+=1
        return best