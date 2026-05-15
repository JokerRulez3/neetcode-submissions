class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ptr = 0
        maxOnes = 0
        counter = 0

        while ptr < len(nums):
            if nums[ptr] == 1:
                counter += 1
                maxOnes = max(maxOnes, counter)
            else:
                counter = 0
            ptr += 1
        
        return maxOnes
        