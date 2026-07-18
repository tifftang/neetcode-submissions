class Solution:
    def trap(self, height: List[int]) -> int:
        maxL, maxR, l, r = height[0], height[-1], 0, len(height) - 1
        area = 0
        while l < r:
            if height[l] < height[r]:
                maxL = max(height[l], maxL)
                area += (maxL - height[l])
                l += 1
            else:
                maxR = max(height[r], maxR)
                area += (maxR - height[r])
                r -= 1
        return area