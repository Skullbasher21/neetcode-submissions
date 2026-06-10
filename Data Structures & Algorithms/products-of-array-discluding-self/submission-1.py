class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from collections import Counter
        c = Counter(nums)
        if c[0] >= 2:
            return [0] * len(nums)
        elif c[0] == 1:
            total = 1
            for i in nums:
                if i != 0:
                    total *= i
            toReturn = [0] * len(nums)
            toReturn[nums.index(0)] = total
            return toReturn
        else:
            total = 1
            for i in nums:
                if i != 0:
                    total *= i
            toReturn = []
            for i in nums:
                toReturn.append(int(total / i))
            return toReturn
        return []

        