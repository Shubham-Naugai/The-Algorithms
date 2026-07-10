class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        def func(i,j,dp):
            if obstacleGrid[i][j] != 0:
                return 0
            if(dp[i][j] != -1):
                return dp[i][j]
            
            if(i == m-1 and j == n-1):
                return 1
            
            if(i == m-1 and j < n-1):
                return func(i,j+1,dp)
            if(j == n-1 and i < m-1):
                return func(i+1,j,dp)
            
            down = func(i+1,j,dp)
            right = func(i,j+1,dp)
            dp[i][j] = down + right
            return down + right
        dp = [[-1]*n for _ in range(m)]
        return func(0,0,dp)