class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # rows
        n = len(triangle)
        #tabulation
        dp = [[-1]*len(triangle[i]) for i in range(len(triangle))]
        # base case
        for j in range(len(triangle[n-1])):
            dp[n-1][j] = triangle[n-1][j]
        
        ##
        for i in range(n-2, -1, -1):
            for j in range(0, i+1):
                d = triangle[i][j] + dp[i+1][j]
                dg = triangle[i][j] + dp[i+1][j+1]
                
                dp[i][j] = min(d, dg)
        
        return dp[0][0]
        
        # def f(i, j, dp):
        #     if(dp[i][j] != -1):
        #         return dp[i][j]
            
        #     if i == len(triangle)-1:
        #         return triangle[i][j]
            
        #     down_right = triangle[i][j] + f(i+1, j+1, dp)
        #     down = triangle[i][j] + f(i+1, j, dp)
        #     dp[i][j] = min(down_right, down)
        #     return min(down_right, down)
        
        # dp = [[-1]*len(triangle[i]) for i in range(len(triangle))]
        # return f(0,0, dp)
