class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            n1, n2 = numbers[l], numbers[r]
            if n1 + n2 == target:
                return [l + 1, r + 1]
            elif n1 + n2 < target:
                l += 1
            else:
                r -= 1
        return [0, 0]