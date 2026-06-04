class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        toReturn = []
        for i in range(0, len(nums) - k + 1):
            window = nums[i:i+k]
            toReturn.append(max(window))
        return toReturn
