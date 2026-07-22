class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1]*(amount+1) for _ in range(n)]
        
        def f(i, a):
            if i == 0:
                if a%coins[0] == 0:
                    return a//coins[0]
                return float("inf")
            
            if dp[i][a] != -1:
                return dp[i][a]
            nt = f(i-1, a)
            t = float("inf")
            if coins[i] <= a:
                t = 1 + f(i, a-coins[i])
            
            dp[i][a] = min(t, nt)
            return dp[i][a]
        
        ans = f(n-1, amount)
        if ans == float("inf"):
            return -1
        return ans