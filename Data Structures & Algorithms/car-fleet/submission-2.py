class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        #car list position and speed

        for i in range(len(position)):
            cars.append([position[i], speed[i]]) #match cars position speed

        stack = []

        #1,3, 2,4
        #2 (closer to end), 3(farther)
        #3, 10, 4.5, 3

        #reverse order, check speed farther vs closer

        for p, s in sorted(cars)[::-1]: # Reverse sorted order position
            stack.append((target - p) / s) #get the time reached if time less-> catchup- then ppop
            #removing faster car because collide- slow speed as fleet

            #start of stack closer target, end of stack farther target- pop values farher
            #if farther less time-> merges, then pop merge into fleet

            if len(stack) >= 2 and stack[-1] <= stack[-2]: #if it reaches in less time-> collide then fleet
                stack.pop()

        return len(stack)
        #keep the one ahead because speed of one ahead bc slow down after colide

        #car can only join fleet thats ahead- sort
        #The time initially added to the stack is the car's hypothetical arrival time, assuming it never slows down or encounters another car
        #helps to calculate merge