class Solution:
    def rob(self, nums: List[int]) -> int:

        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))   #if only one element edge case 
    
    def helper(self, nums):
            rob1, rob2 =0,0
            for n in nums:
                newrob = max(rob1+n, rob2)
                rob1 =rob2
                rob2 = newrob
            return rob2

    #same as house robber like prefix but circle so skip first and last run on subarrays