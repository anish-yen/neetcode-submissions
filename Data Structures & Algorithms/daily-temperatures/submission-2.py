class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
            res = [0] * len(temperatures)
            stack = []

            # stack 6
            #res 1 4 1 2 1 0 0
            for i, temp in enumerate(temperatures):
                while stack and temp > temperatures[stack[-1]]:
                    previous_day = stack.pop()
                    res[previous_day] = i - previous_day
                stack.append(i)
            return res

            #stack doesnt need to be empty
            # store the indeces in stack
            # find a new temp greater than old temp-> update res for old temp 
            # i - previous day (stack.pop)
            #return res
                    