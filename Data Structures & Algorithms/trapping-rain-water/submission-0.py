class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        leftM = rightM = 0
        total = 0

        while left < right:
            if height[left] <= height[right]:
                if height[left] >= leftM:
                    leftM = height[left]
                else:
                    total += leftM - height[left]
                left += 1
            else:
                if height[right] >= rightM:
                    rightM = height[right]
                else:
                    total += rightM - height[right]
                right -= 1
            
        return total
        