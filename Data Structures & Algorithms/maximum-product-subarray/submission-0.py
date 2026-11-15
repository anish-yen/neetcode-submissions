class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prevMax = nums[0]
        prevMin = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            currMax = max(nums[i], nums[i] * prevMax, nums[i] * prevMin)
            currMin = min(nums[i], nums[i] * prevMax, nums[i] * prevMin)

            prevMax = currMax
            prevMin = currMin

            result = max(result, currMax) #running max vs curr max kadane, have to keep track of num, prevmin and prev max
            #if neg* neg greater need to update that 

        return result