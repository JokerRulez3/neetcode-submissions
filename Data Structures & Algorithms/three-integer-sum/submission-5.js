class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        let res = [];

        nums.sort((a,b) => a-b);

        for (let i = 0; i<nums.length;i++) {
            if (nums[i] > 0) {
                break;
            }
            else if(i > 0 && nums[i-1] === nums[i]){
                continue;
            }

            let l = i + 1;
            let r = nums.length - 1;

            while (l < r) {
                let total = nums[i] + nums[l] + nums[r];

                if (total > 0) {
                    r = r - 1;
                }
                else if (total < 0) {
                    l = l + 1;
                }
                else {
                    res.push([nums[i], nums[l], nums[r]]);
                    l = l + 1;
                    while ((nums[l] === nums[l - 1]) && (l < r)){
                        l = l + 1;
                    }
                }
            }
        }

        return res;
        
    }
}
