class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        #constraints, can be any order, all integers -10-.10
        #base case if path sum = target save, else stop if it exceeds target
        #back track step: add number - recurse- pop last number added

        res = []
        #AT MOST N recursive calls and path hodls at most n elements
        def backtrack(path, visited):
            if len(path) == len(nums): #base case
                res.append(path.copy())
                return
            


            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    path.append(nums[i])
                    backtrack(path, visited)
                    visited[i] = False
                    path.pop()
        
        path = []
        visited = [False] * len(nums)
        backtrack(path, visited)
        return res



        