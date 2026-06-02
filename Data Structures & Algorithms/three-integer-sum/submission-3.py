class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        toReturn = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            x = i + 1
            y = len(nums) - 1
            while x < y:
                if nums[x] + nums[y] > target:
                    y -= 1
                elif nums[x] + nums[y] < target:
                    x += 1
                elif nums[x] + nums[y] == target:
                    toReturn.append([nums[i], nums[x], nums[y]])
                    x += 1
            
        for i in range(len(toReturn)):
            toReturn[i] = sorted(toReturn[i])
        seen = []
        toReturn2 = []
        for i in range(len(toReturn)):
            if toReturn[i] in seen:
                continue
            seen.append(toReturn[i])
            toReturn2.append(toReturn[i])
        return toReturn2