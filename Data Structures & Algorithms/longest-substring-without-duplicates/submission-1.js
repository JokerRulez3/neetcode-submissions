class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        let charSet = new Set();
        let maxLen = 0;
        let l = 0;

        for (let r = 0; r<s.length;r++) {
            while (charSet.has(s[r])) {
                let firstValue = charSet.values().next().value;
                charSet.delete(firstValue);
                l += 1;
            }
            charSet.add(s[r]);
            maxLen = Math.max(maxLen, (r - l + 1));
        }

        return maxLen;
    }
}
