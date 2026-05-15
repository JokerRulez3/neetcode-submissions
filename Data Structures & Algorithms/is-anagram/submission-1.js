class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (!s || !t) return false;
        if (s.length != t.length) return false;
        let counterMapS = {};
        let counterMapT = {};

        s.split("").forEach(item => {
            // Get the current count (or 0 if it doesn't exist) and set the new count
            counterMapS[item] = (counterMapS[item] || 0) + 1;
        });

        t.split("").forEach(item => {
            // Get the current count (or 0 if it doesn't exist) and set the new count
            counterMapT[item] = (counterMapT[item] || 0) + 1;
        });

        for (let key in counterMapS) {
            if (counterMapS[key] !== counterMapT[key]) {
                return false;
            }
        }

        return true;
    }
}
