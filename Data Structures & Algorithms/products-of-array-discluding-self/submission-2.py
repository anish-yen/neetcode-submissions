class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1,2,4,6]
        #prefix: start with 1: [1, 1, 2, 8]
        #suffix: [48, 24, 6, 1] #mult elemebnts beore and after and get evertying except tha tnumber

        #prefix
        pre = [1] * len(nums)
        suf = [1] * len(nums)
        for i in range(1, len(pre)):
            pre[i] = pre[i-1] * nums[i-1]
        #print(f" pre {pre}")
        for i in range(len(pre)-2, -1,-1):
            suf[i] = suf[i+1] * nums[i+1]
        #print(f" suf {suf}")

        res = []
        for i in range(len(nums)):
            res.append(pre[i]*suf[i])
        return res

        