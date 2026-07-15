class Solution {
    public boolean func(int[] nums, int i, int target, int[][] dp){
        if (target == 0){
            return true;
        }
        if (i == 0){
            return target == nums[0];
        }
        if (dp[i][target] != -1)
            return dp[i][target] == 1;
        boolean not_take = func(nums, i-1, target, dp);
        boolean take = false;
        if (nums[i] <= target){
            take = func(nums, i-1, target-nums[i], dp);
        }
        dp[i][target] = (take || not_take) ? 1 : 0;
        return take || not_take;
    }
    public boolean canPartition(int[] nums) {
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }

        if (sum % 2 == 1){
            return false;
        }
        int target = sum / 2;
        int[][] dp = new int[nums.length][target + 1];
        for (int[] row : dp)
            Arrays.fill(row, -1);
        return func(nums, nums.length-1, target, dp);
    }
}

