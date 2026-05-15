class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """ 2Sum - Given a target, find the indices matching
        with curr index value, see if adding the remaining two leads to
        opp of curr index value resulting in 0 """
        res = []

        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return res




        