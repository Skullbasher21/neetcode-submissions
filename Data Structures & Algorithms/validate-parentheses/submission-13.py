class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {'(':')','[':']','{':'}'}
        first = ['[', '{', '(']
        for i in range(len(s)):
            print(stack)
            if s[i] in first:
                stack.append(d[s[i]])
            elif s[i] in d.values() and stack != []:
                if s[i] != stack[-1]:
                    return False
                stack.pop(-1)
            else:
                return False
        if stack != []:
            return False 
        print(stack)
        return True

        