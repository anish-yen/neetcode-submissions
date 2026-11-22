from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:

        #build adjacency list

        prereqs = defaultdict(list)

        for course, pre in prerequisites:
            prereqs[course].append(pre)
        
        res = []

        visit = set()
        cycle = set()

        def dfs(course):

            if course in visit:
                return True

            if course in cycle:
                return False

            
            cycle.add(course)
            

            for pre in prereqs[course]:
                if dfs(pre) == False:
                    return False
            res.append(course)    
            visit.add(course)
            cycle.remove(course)
            return True
        # FIX: process all courses
        for course in range(numCourses):
            if dfs(course) == False:
                return []

        return res  # FIX    

#approach
#initialize dict if empty list no prereq
# map course to prereq
#make sure isnt cycle so set- 
#make sure not to repeat visited
#visit for fully processed courses while cycle is for 


        