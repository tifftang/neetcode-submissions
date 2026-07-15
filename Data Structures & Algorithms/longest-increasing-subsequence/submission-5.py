class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def bt(j, last):
            if (j, last) in memo:
                return memo[(j, last)]

            max_l = 0

            for i in range(j, len(nums)):
                if nums[i] > last:
                    max_l = max(
                        max_l,
                        1 + bt(i + 1, nums[i])
                    )

            memo[(j, last)] = max_l
            return max_l

        return bt(0, -float("inf"))