class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
        let count = new Map();
        let res = 0;
        let l = 0;

        for (let r = 0; r < s.length; r++) {
            // Use Map .set() and .get() instead of []
            let charCount = (count.get(s[r]) || 0) + 1;
            count.set(s[r], charCount);

            // Spread Map values into Math.max
            while ((r - l + 1) - Math.max(...count.values(), 0) > k) {
                count.set(s[l], count.get(s[l]) - 1);
                l += 1;
            }

            res = Math.max(res, r - l + 1);
        }

        return res;
    }
}
