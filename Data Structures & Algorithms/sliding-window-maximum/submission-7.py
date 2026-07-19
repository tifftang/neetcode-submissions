class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        result = []
        for idx, n in enumerate(nums):
            while q and q[0] < (idx - k + 1):
                q.popleft()
            while q and nums[q[-1]] < n:
                q.pop()
            q.append(idx)
            if idx + 1 >= k:
                result.append(nums[q[0]])
        return result

            