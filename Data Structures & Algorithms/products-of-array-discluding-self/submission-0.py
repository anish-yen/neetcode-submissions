class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res =[]
        prefix = []
        suffix =[]
        n = len(nums)
        # prefix
        prefix = [1]
        for i in range(1, n):
            prefix.append(prefix[-1] * nums[i - 1])

        #nums=1,2,4,6
        #prefix=[1,1,2,8]
        
        # suffix (built backwards)
        suffix = [1]
        for i in range(n - 2, -1, -1):
            suffix.append(suffix[-1] * nums[i + 1])

        suffix = suffix[::-1]

        for i in range(len(nums)):
            res.append(prefix[i]*suffix[i])

        #nums=1,2,4,6
        #suffix=[1,6,24,48]-> [48,24,6,1]


        return res


       






