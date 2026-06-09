class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        times = []
        count = 0
        for i in range(len(position)):
            times.append((position[i],(target - position[i]) / speed[i]))
        times = sorted(times, reverse=True)
        print(times)
        
        stack.append(times.pop(-1))
        while times:
            
            if stack:
                y = times.pop(-1)
                seen = []
                while stack:
                    x = stack.pop(-1)
                    if y[1] < x[1]:
                        stack.append(x)
                        break
                stack.append(y)
        return len(stack)


        