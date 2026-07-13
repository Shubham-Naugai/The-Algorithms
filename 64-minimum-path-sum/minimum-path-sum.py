class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def f(i, j, dp):
            if(dp[i][j] != -1):
                return dp[i][j]
            if i == len(grid)-1 and j == len(grid[0])-1:
                return grid[i][j]
            if j == len(grid[0])-1:
                return grid[i][j] + f(i+1, j, dp)
            if i == len(grid)-1:
                return grid[i][j] + f(i, j+1, dp)
            
            right = grid[i][j] + f(i, j+1, dp)
            bottom = grid[i][j] + f(i+1, j, dp)
            dp[i][j] = min(right, bottom)
            return min(right, bottom)
        
        dp = [[-1]*len(grid[0]) for _ in range(len(grid))]
        return f(0,0, dp)
