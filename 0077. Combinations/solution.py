class Solution:
    def combine(self, n: int, k: int):
        
        def bk(n,k,i,a,res):
            
            #print("i: " + str(i) + " k: " + str(k) + " a: " + str(a) + " res: " + str(res))

            if (len(a) == k):
                #res.append(a[:])
                res.append(a)
            else:
                i += 1
                for x in range(i,n+1):
                    #a.append(x)
                    bk(n,k,x,a + [x],res)
                    #a.remove(x)

        a = []
        res = []
        bk(n,k,0,a,res)
        return(res)

                
                