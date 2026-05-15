class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        if (!nums || nums.length === 0) {
            return [];
        }

        const res = new Array(nums.length).fill(1);

        let prefix = 1;
        for (let i = 0; i < res.length; i++) {
            res[i] = prefix;
            prefix = prefix * nums[i];
        }

        let postfix = 1;
        for (let i = res.length - 1; i >= 0; i--) {
            res[i] = res[i] * postfix;
            postfix = postfix * nums[i];
        }

        return res
    }
}
