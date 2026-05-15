class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMin(nums) {
       let l = 0;
        let r = nums.length - 1;

        let res = Infinity

        while (l <= r) {
            if (nums[l] < nums[r]) {
                res = res < nums[l] ? res : nums[l];
                break;
            }
            let mid = parseInt((l + r) / 2);
            res = res < nums[mid] ? res : nums[mid];

            if (nums[l] <= nums[mid]) {
                l = mid + 1;
            }
            else {
                r = mid - 1;
            }
        }

        return res;

    }
}
