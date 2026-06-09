class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        if temperatures == []:
            return []
        stack.append((temperatures[0], 0))
        for i in range(1, len(temperatures)):
            t = temperatures[i]
            while stack:
                x = stack.pop(-1)
                if x[0] < t:
                    result[x[1]] = i - x[1]
                else:
                    stack.append(x)
                    break
            stack.append((t,i))
        return result
                






        