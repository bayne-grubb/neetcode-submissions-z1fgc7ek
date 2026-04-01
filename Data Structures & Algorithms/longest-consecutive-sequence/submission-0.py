class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        max_len_so_far = 0
        for num in unique_nums:
            if num - 1 not in unique_nums:
                temp_num = num + 1
                temp_len = 1
                while temp_num in unique_nums:
                    temp_num += 1
                    temp_len += 1
                max_len_so_far = max(temp_len, max_len_so_far)
        return max_len_so_far
