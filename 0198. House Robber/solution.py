class Solution:
    def rob(self, nums) -> int:

        mem = [-1]*len(nums)
        
        def rob_dp(nums,i):
            if i<0:
                return 0
            if mem[i] >= 0:
                return mem[i]
            
            mem[i] = max(rob_dp(nums,i-2)+nums[i], rob_dp(nums,i-1))
            return mem[i]
        
        return rob_dp(nums,len(nums)-1)