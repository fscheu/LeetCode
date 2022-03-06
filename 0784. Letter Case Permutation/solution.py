class Solution:
    def letterCasePermutation(self, s: str):
    
        def back(s: str, path: str, i, ret):
            
            if (len(s) == len(path)):
                ret.append(path)
            else:
                if not s[i].isnumeric():
                    back(s,path+s[i].lower(),i+1,ret)
                    back(s,path+s[i].upper(),i+1,ret)
                else:
                    back(s,path + s[i],i+1,ret)
        
        
        ret = []
        back(s,"",0,ret)
        return ret
    