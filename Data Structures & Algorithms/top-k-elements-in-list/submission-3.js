class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let countMap = new Map();

        for (let num of nums) {
            countMap.set(num, (countMap.get(num) || 0) + 1); 
        }

        const countMap1 = new Map([...countMap.entries()].sort((a, b) => b[1] - a[1]));

        const res = [];
        let i = 0;
        for (let key of countMap1.keys()) {
            if (i < k) {
                res.push(key);
                i++;
            }
            else {
                break;
            }   
        }

        return res
    }
}
