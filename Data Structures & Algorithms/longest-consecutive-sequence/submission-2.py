class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cons = set(nums)
        longest = 0
        for n in cons: 
           if (n - 1) not in cons: 
            curr_longest = 1
            while (n+curr_longest) in cons: 
                curr_longest += 1  
            longest = max(longest,curr_longest)
        return longest 