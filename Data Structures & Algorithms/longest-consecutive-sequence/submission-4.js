class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        let maxLen = 0;
        let mySet = new Set(nums);

        for (let num of nums) {
            // Start of the sequence
            if (!mySet.has(num - 1)) {
                let curr_len = 1;
                let curr_num = num;

                while (mySet.has(curr_num + 1)) {
                    curr_num += 1;
                    curr_len += 1;
                }

                maxLen = Math.max(maxLen, curr_len);
            }
        }

        return maxLen;
    }
}
