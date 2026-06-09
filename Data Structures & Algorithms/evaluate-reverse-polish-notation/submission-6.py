class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {'+', '-', '*', '/'}
        for i in tokens:
            if i in ops:
                x = int(stack.pop(-1))
                print(x)
                y = int(stack.pop(-1))
                print(y)
                if i == '+':
                    stack.append(str(x + y))
                elif i == '*':
                    stack.append(str(x * y))
                elif i == '-':
                    stack.append(str(y - x))
                else:
                    print(y /x)
                    print(int(y /x))
                    stack.append(str(int(y / x)))
            else:
                stack.append(i)
        return int(stack[0])
                
