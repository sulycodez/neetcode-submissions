import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = re.sub(r'[^a-z0-9]', "", s.lower()) # remove all the space in the string and make it lowercase. 
        l = 0 #set left pointer to 1st elemet
        r = len(res) - 1 # set right pointer to right element 
        while l < r :
            if res[l] != res[r] :
                return False 
            l += 1 
            r -= 1 
        return True  