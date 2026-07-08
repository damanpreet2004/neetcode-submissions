class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        i = 0
        j = len(heights) - 1
        while(i < j):
            current_area = min(heights[i],heights[j]) * (j-i)
            if current_area > area:
                area = current_area
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

 
                
        return area
                