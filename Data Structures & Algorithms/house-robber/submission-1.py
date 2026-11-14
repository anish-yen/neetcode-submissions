class Solution:
    def rob(self, nums: List[int]) -> int:
        
        prefix = [0] * (len(nums) +2)

        for i in range(len(nums)):
            prefix[i+2] = nums[i] + prefix[i]
        
        return prefix[-1]
