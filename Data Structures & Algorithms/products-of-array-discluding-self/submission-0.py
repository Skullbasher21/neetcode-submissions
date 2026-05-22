class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        toReturn = []
        total = 1
        nonzero = 1
        countzero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nonzero = nonzero * nums[i]
        for i in range(len(nums)):
            total = total * nums[i]
            if nums[i] == 0:
                countzero += 1
        if countzero > 1:
            return [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] != 0:
                toReturn.append(int(total / nums[i]))
            else:
                toReturn.append(int(nonzero))
        return toReturn
                
                
        
        