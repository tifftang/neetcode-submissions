class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * len(text2) for i in range(len(text1))]
        for i in range(len(text1)):
            t1 = text1[i]
            for j in range(len(text2)):
                if text2[j] == t1:
                    if i - 1 >= 0 and j-1>=0:
                        print(i - 1)
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = 1
                else:
                    if i - 1 >= 0:
                        dp[i][j] = dp[i-1][j] 
                    if j - 1 >=0:
                        dp[i][j] = max(dp[i][j-1],dp[i][j]) 
        return dp[len(text1) - 1][len(text2) - 1]