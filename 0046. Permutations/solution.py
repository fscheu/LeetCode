class Solution:
    def permute(self, nums):
        
        def bkt(nums, path, ret):
            
            if (len(path) == len(nums)):
                ret.append(path[:])
            else:
                for x in range(len(nums)):
                    if nums[x] not in path:
                        path.append(nums[x])
                        bkt(nums,path,ret)
                        path.remove(nums[x])
        
        ret = []
        bkt(nums,[],ret)
        return ret
