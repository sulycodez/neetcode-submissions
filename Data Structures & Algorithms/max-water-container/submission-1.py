class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0 
        l,r = 0, len(heights) - 1 
        while l < r : 
            h = min(heights[l],heights[r])
            w = r - l
            curr_area = h * w 
            if area < curr_area :
                area = curr_area
            if heights[l] > heights[r] :
                r -= 1 
            else :
                l += 1
        return area 
            
