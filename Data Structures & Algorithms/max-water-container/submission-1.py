class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Brute Force (O(n2)):
        """

        res = 0

        for l in range(len(heights)):
            for r in range(l+1, len(heights)):
                area = (r - l) * min(heights[l], heights[r])
                res = max(res, area)
        
        return res
        """

        res = 0
        leftP = 0
        rightP = len(heights) - 1

        while leftP < rightP:
            area = (rightP - leftP) * min(heights[leftP], heights[rightP])
            res = max(res, area)

            if heights[leftP] < heights[rightP]:
                leftP += 1
            else:
                rightP -= 1
        
        return res
     
        