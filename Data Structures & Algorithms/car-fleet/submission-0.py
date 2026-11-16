class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for i in range(len(position)):
            cars.append([position[i], speed[i]]) #match cars position speed

        stack = []

        for p, s in sorted(cars)[::-1]: # Reverse sorted order
            stack.append((target - p) / s) #get the time reached

            if len(stack) >= 2 and stack[-1] <= stack[-2]: #if it reaches in less time-> collide then fleet
                stack.pop()

        return len(stack)
        #keep the one ahead because speed of one ahead bc slow down after colide

        #car can only join fleet thats ahead- sort