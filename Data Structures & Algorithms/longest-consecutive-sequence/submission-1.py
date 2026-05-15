class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        max_length = 0

        for num in nums:
            if (num - 1) not in my_set:
                curr_num = num
                curr_len = 1
            
                while (curr_num + 1) in my_set:
                    curr_num += 1
                    curr_len += 1
            
                max_length = max(max_length, curr_len)

        return max_length
        
    