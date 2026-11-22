class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:



        #choices: all nums in nums- once each times
        #constraints, no duplicat subsets
        #base case if path sum = target save, else stop if it exceeds target
        #back track step: add number - recurse- pop last number added

        res = []

        def backtrack(path, start):
            res.append(path.copy())
            if start == len(nums):
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(path, i+1)
                path.pop()


        backtrack([], 0)
        return res
            
        