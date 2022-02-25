
class Solution:
    
    def binary_search(self,nums, target: int, ini: int, end: int) -> int:
        """ Recursive version"""

        if (end < ini):
            return -1
        
        ret = (end+ini)//2
        if nums[ret] == target:
            return ret
        else:
            if nums[ret] > target:
                return self.binary_search(nums,target,ini,ret-1)    
            else:
                return self.binary_search(nums,target,ret+1,end)
    
    def search(self, nums, target: int) -> int:
                    
        return self.binary_search(nums, target, 0, len(nums)-1)

