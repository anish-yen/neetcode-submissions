from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        prereqs = defaultdict(list)

        for course, pre in prerequisites:
            prereqs[course].append(pre)

        cycle, visit = set(), set()


        def dfs(course):
            if course in cycle:
                return False
            
            if course in visit: 
                return True

            cycle.add(course)

            #go through prereqs each course
            for pre in prereqs[course]:
                if not dfs(pre):
                    return False
            
            cycle.remove(course)
            visit.add(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i): # go through each course
                return False

        return True
        