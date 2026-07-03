class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def func(i, arr, dp):
            if i == 0:
                return arr[i]
            if i < 0:
                return 0
            
            if dp[i] != -1:
                return dp[i]
            take = arr[i] + func(i-2, arr, dp)
            not_take = func(i-1, arr, dp)

            dp[i] = max(take, not_take)
            return max(take, not_take)
        
        excludefirst = func(len(nums)-2, nums[1:], [-1] * (len(nums)-1))
        excludelast = func(len(nums)-2, nums[:-1], [-1] * (len(nums)-1))
        return max(excludefirst, excludelast)
