class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        toReturn = []
        for j in range(len(nums)):
            if j > 0 and nums[j] == nums[j-1]: continue
            t = -nums[j]
            d = {}
            for i in range(j + 1, len(nums)):
                x = nums[i]
                if t - x in d:
                    toReturn.append([-t, t - x, x])
                    while i + 1 < len(nums) and nums[i+1] == x: i += 1
                    del d[t-x]
                else:
                    d[x] = i
        return toReturn