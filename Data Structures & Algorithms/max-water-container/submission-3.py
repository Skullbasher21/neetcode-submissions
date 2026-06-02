class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        x = 0
        y = len(heights) - 1
        while x < y:
            best = max(best, min(heights[y], heights[x]) * (y - x))
            if heights[x] >= heights[x+1] and heights[x] > heights[y]:
                y -= 1
            elif heights[y] >= heights[y-1] and heights[x] < heights[y]:
                x += 1
            else: 
                if heights[x] < heights[y]:
                    x += 1
                else: 
                    y -= 1
            
        return best


        