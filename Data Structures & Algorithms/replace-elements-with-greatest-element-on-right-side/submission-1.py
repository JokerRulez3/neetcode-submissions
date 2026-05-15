class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # r = 0
        # while r < len(arr) - 1:
        #     subArray = arr[r+1:len(arr)]
        #     currMax = max(subArray)
        #     arr[r] = currMax
        #     r += 1
        
        # arr[len(arr)-1] = -1

        # return arr

        n = len(arr)
        ans = [0]*n
        rightMax = -1

        for i in range(n-1, -1, -1):
            ans[i] = rightMax
            rightMax = max(arr[i], rightMax)
        
        return ans
        