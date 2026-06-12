class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)): 
            cars.append((position[i],(target - position[i]) / speed[i]))
        cars.sort(reverse = True)
        stack = [cars.pop()]
        
        print(cars)
        print(stack)
        for i in range(0, len(cars)):
            y = cars.pop()
            while stack:
                x = stack.pop()
                if y[1] < x[1]:
                    stack.append(x)
                    break
            stack.append(y)
        

        return len(stack)


        