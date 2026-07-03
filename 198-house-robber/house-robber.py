class Solution:
    def rob(self, nums: List[int]) -> int:

        def func(i, dp):
            if i == 0:
                return nums[i]
            if i < 0:
                return 0
            
            if dp[i] != -1:
                return dp[i]
            take = nums[i] + func(i-2, dp)
            not_take = func(i-1, dp)

            dp[i] = max(take, not_take)
            return max(take, not_take)
        
        dp = [-1] * len(nums)
        return func(len(nums)- 1, dp)

