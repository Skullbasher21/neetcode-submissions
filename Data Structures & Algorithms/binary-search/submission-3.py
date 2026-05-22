class Solution:
    def search(self, nums: List[int], target: int) -> int:
        print(nums)
        if target not in nums:
            return -1
        mid = int(len(nums) / 2)
        print(mid)
        if len(nums) == 1 and nums[0] != target:
            return -1
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            return self.search(nums[0:mid], target)
        if nums[mid] < target:
            return mid + 1 +self.search(nums[mid + 1:len(nums)], target)
        return -1
        