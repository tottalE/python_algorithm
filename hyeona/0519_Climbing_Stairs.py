class Solution:
    def climbStairs(self, n: int) -> int:
        if(n==1):
            return 1

        dp = [0 for _ in range(n+1)]

        dp[1] = 1
        dp[2] = dp[1]+1

        for i in range(3,n+1):
            dp[i] = dp[i-2]+dp[i-1]

        return dp[n]
