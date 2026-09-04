class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0 , len(height) - 1 
        sum = 0 
        leftMax, rightMax = height[l], height[r]
        while l < r : 
            if leftMax < rightMax : 
                l += 1 
                leftMax = max(leftMax,height[l])
                sum += leftMax - height[l]
            else:
                r-=1 
                rightMax = max(rightMax,height[r])
                sum += rightMax - height[r]
        return sum 
                
            
            

