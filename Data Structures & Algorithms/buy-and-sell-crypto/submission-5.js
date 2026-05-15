class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let maxP = 0;
        let minBuy = prices[0];

        for (let i = 0; i<prices.length; i++) {
            maxP = Math.max(maxP, prices[i] - minBuy);
            minBuy = Math.min(minBuy, prices[i]);
        }

        return maxP;
    }
}
