class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        curr = 0

        for i in range(len(nums)):
            curr = max(nums[i], curr+nums[i])
            max_so_far = max(max_so_far, curr)
        return max_so_far
        