class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for key, val in counter.items():
            if val > 1:
                return True
        
        return False
        