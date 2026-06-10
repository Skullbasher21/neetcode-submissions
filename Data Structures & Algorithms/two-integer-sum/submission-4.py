class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            x = nums[i]
            if target - x in d:
                return [d[target - x], i]
            else:
                d[x] = i
        return []

        