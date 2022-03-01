from collections import Counter
class Solution:
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l_s1 = len(s1)
        if l_s1 > len(s2):
            return False
        
        h_s1 = Counter(s1)    
        for i in range(len(s2)-l_s1+1):
            y = s2[i:(i+l_s1)]
            h_s2 = Counter(y)
            #print(y)
            #print(h_s2)
            if h_s1 == h_s2:
                return True            
        return False