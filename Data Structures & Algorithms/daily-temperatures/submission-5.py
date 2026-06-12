class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [(0,temperatures[0])]
        for i in range(1, len(temperatures)):
            while stack:
                x = stack.pop()
                y = temperatures[i]
                if x[1] >= y:
                    stack.append(x)
                    break
                else: 
                    result[x[0]] = i - x[0]
            stack.append((i, y))
            print(stack)
        return result


            
            
        