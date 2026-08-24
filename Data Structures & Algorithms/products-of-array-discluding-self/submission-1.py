class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        # 1. Left-to-Right Pass (Prefix)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix  # Set the current index to the product of all previous numbers
            
            # Update the prefix by multiplying it by nums[i] for the next iteration
            prefix *= nums[i]

        # 2. Right-to-Left Pass (Postfix)
        postfix = 1
        # range walks backwards: start at last index, stop before -1, step by -1
        for i in range(len(nums) - 1, -1, -1):
            # Update res[i] by multiplying its current value by the postfix
            res[i] *= postfix

            # Update the postfix by multiplying it by nums[i] for the next iteration
            postfix *= nums[i]

        return res
