class Solution:
    def twoSum(self, numbers, target: int):
        
        i1 = 0
        i2 = 1
        lastNE = 1
        limit = len(numbers)-1
        while (numbers[i1] + numbers[i2]) != target:
            if ((numbers[i1] + numbers[i2]) > target):
                i1 = lastNE
                lastNE = lastNE +1
                i2 = i1 + 1
            else:
                if i2 < limit:
                    if numbers[i1] == numbers[i2]:
                        lastNE = i2
                    i2 = i2 + 1
                else:
                    i1 = i1 + 1
                    
        return [i1+1,i2+1]   