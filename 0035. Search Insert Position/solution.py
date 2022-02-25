class Solution:
    def searchInsert(self, nums, target: int) -> int:
        ini, end = 0, len(nums)-1
        while (ini<=end):
            pivot = ini + round((end-ini)/2)
            print(pivot)
            if nums[pivot] == target:
                return pivot
            else:
                if nums[pivot] > target:
                    end = pivot-1
                else:
                    ini = pivot+1
        
        if (target > nums[pivot]):
            return pivot+1
        else:
            return pivot