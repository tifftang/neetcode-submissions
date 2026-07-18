class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)

        have = defaultdict(int)
        values = defaultdict(deque)
        l = 0
        for idx, s in enumerate(s2):
            while s in count and len(values[s]) != 0 and values[s][0] < l:
                have[s] -= 1
                values[s].popleft()
            if s in count and have[s] < count[s]:
                have[s] += 1
                values[s].append(idx)
            elif s in count:
                while have[s] >= count[s]:
                    l = values[s][0] + 1
                    values[s].popleft()
                    have[s] -= 1
                values[s].append(idx)
                have[s] += 1
            else: 
                l = idx + 1
                have = defaultdict(int)
                values = defaultdict(deque)
            if (idx - l + 1) == len(s1): 
                return True
        return False