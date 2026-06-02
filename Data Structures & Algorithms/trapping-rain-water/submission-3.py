class Solution:
    def trap(self, height: List[int]) -> int:
        x = 0 
        y = len(height) - 1
        total = 0
        leftmax = x
        rightmax = y
        while x < y:
            if height[leftmax] < height[rightmax]:
                x += 1
                if height[leftmax] < height[x]:
                    leftmax = x
                total += height[leftmax] - height[x]
            else: 
                y -= 1
                if height[rightmax] < height[y]:
                    rightmax = y
                total += height[rightmax] - height[y]
        return total
            
        