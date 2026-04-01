class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0]*len(nums)
        prefix = 1
        for i, num in enumerate(nums):
            output[i] = prefix
            prefix = num*prefix
        
        # had to look up a solution for this one, learned somehtin new!

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix 
            postfix = nums[i]*postfix
        
        return output