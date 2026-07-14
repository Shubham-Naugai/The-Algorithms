class Solution {
    public int cherrySum(int[][] grid, int i, int j, int k, int[][][] dp){
        if (j < 0 || j > grid[0].length - 1 || k < 0 || k > grid[0].length - 1){
            return 0;
        }
        if (i == grid.length - 1){
            if (j == k){
                return grid[i][j];
            }
            return grid[i][j] + grid[i][k];
        }
        
        if (dp[i][j][k] != -1) return dp[i][j][k];
        
        int maxCherries = 0;
        for (int r1 = -1; r1<=1; r1++){
            for (int r2 = -1; r2<=1; r2++){
                int totalCherries = 0;
                if (j == k){
                    totalCherries = grid[i][j] + cherrySum(grid, i+1, j+r1, k+r2, dp);
                }
                else{
                    totalCherries = grid[i][j] + grid[i][k] + cherrySum(grid, i+1, j+r1, k+r2, dp);
                }
                maxCherries = Math.max(maxCherries, totalCherries);
            }
        }
        dp[i][j][k] = maxCherries;
        return maxCherries;
    }
    public int cherryPickup(int[][] grid) {
        int[][][] dp = new int[grid.length][grid[0].length][grid[0].length];
        for (int[][] arr2d : dp) {
            for (int[] arr1d : arr2d) {
                Arrays.fill(arr1d, -1);
            }
        }
        return cherrySum(grid, 0, 0, grid[0].length-1, dp);
    }
}