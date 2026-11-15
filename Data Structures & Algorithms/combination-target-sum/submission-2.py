

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        #choices: all nums in nums- unleited times
        #constraints, can be any orderbut combinations are seem if freq same
        #base case if path sum = target save, else stop if it exceeds target
        #back track step: add number - recurse- pop last number added

        res = []

        def backtrack(path, start):
            if sum(path) > target:
                return
            if sum(path) == target:
                res.append(path.copy()) # need the copy part because later modify and pop
                return
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(path, i)
                path.pop()

        backtrack([], 0)
        return res
            
        