class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
        have = Counter(s2[:len(s1)])
        if count == have: return True
        for i in range(len(s1), len(s2)):
            have[s2[i]] += 1
            have[s2[i-len(s1)]] -= 1
            if count == have: return True
        return False