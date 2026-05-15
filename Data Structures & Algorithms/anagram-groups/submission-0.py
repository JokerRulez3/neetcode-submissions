class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret_list = []
        temp_map = {}

        for value in strs:
            sorted_str_list = sorted(value)
            sorted_str = "".join(sorted_str_list)
            if sorted_str in temp_map:
                temp_map[sorted_str].append(value)
            else:
                temp_map[sorted_str] = [value]
        
        for key, value in temp_map.items():
            ret_list.append(value)
        
        return ret_list
        