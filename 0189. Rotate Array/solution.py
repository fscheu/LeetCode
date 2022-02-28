class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k%l
        nums[:] =  nums[-k:] + nums[:-k]