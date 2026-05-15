class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let maxArea = 0;
        let l = 0;
        let r = heights.length - 1;

        while (l < r) {
            let currArea = (r - l) * Math.min(heights[l], heights[r]);
            maxArea = Math.max(maxArea, currArea);

            if (heights[l] < heights[r]) {
                l += 1;
            }
            else {
                r -= 1;
            }
        }
        return maxArea;
    }
}
