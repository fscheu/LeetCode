class Solution:
    def minimumTotal(self, triangle) -> int:
        
        def min_DP_rec(tri, level, i):
            
            if level == len(tri)-1:
                return tri[level][i]
            
            min_sub = min( min_DP_rec(tri,level+1,i), min_DP_rec(tri,level+1,i+1) ) 
            return min_sub + tri[level][i]
        
        res = [ [None for _ in range(len(x))] for x in triangle ]
        def min_DP_rec_mem(tri, level, i):
            
            if level == len(tri)-1:
                return tri[level][i]
            
            if res[level][i]:
                return res[level][i]
            
            res[level][i] = min( min_DP_rec_mem(tri,level+1,i), min_DP_rec_mem(tri,level+1,i+1) ) 
            res[level][i] += tri[level][i]
            return res[level][i]
        
        def min_DP_it(tri):
            if not tri:
                return 0
            
            res[len(tri)-1] = tri[-1:][0]
            print(res)
            for i in range(len(tri)-2,-1,-1):
                for j in range(len(tri[i])):
                    res[i][j] = min(res[i+1][j], res[i+1][j+1]) + tri[i][j]
            print(res)
            return res[0][0]
        
        #return min_DP_rec(triangle,0,0)
        #return min_DP_rec_mem(triangle,0,0)
        return min_DP_it(triangle)