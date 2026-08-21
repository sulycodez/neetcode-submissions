class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()
        for i,n in enumerate(nums):
            dif = target - n 
            if dif in seen:
                return [nums.index(dif), i]
            seen.add(n)