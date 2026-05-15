class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = Counter(nums)

        nums_sorted_items = sorted(nums_dict.items(), key=lambda item:item[1], reverse=True) 
        sorted_nums_dict = dict(nums_sorted_items)

        return list(sorted_nums_dict.keys())[:k]

                