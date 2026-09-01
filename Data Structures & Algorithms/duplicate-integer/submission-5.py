class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # tracks numbers we have seen
        for num in nums :
            if num in seen: #checks if number in our set 
                return True #duplicate value found 
            seen.add(num) # add number to our set 
        return False #duplicate not found 