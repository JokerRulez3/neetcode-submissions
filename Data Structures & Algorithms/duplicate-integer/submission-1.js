class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let map = {};
        for (let i = 0; i<nums.length; i++) {
            if (map[nums[i]] && map[nums[i]] === 1) {
                // Found duplicate
                    return true;
            }
            else {
                map[nums[i]] = 1
            }
        }

        return false;
    }
}
