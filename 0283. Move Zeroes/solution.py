class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        iz = 0
        for ix in range(len(nums)):
            if nums[ix] == 0:
                count = count+1
            else:
                nums[iz] = nums[ix]
                iz = iz+1
        if count != 0:
            nums[:] = nums[:-count] + [0 for x in range(count)]