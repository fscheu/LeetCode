class Solution:
    
    def rec_flFill(self,image,sr,sc,actColor,newColor):
        
        if image[sr][sc] == actColor:
            image[sr][sc] = newColor
            if sr > 0:
                self.rec_flFill(image,sr-1,sc,actColor,newColor)
            if sr < len(image)-1:
                self.rec_flFill(image,sr+1,sc,actColor,newColor)
            if sc > 0:
                self.rec_flFill(image,sr,sc-1,actColor,newColor)
            if sc < len(image[sr])-1:
                self.rec_flFill(image,sr,sc+1,actColor,newColor)
        
    
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        actColor = image[sr][sc]
        if actColor != newColor:
            self.rec_flFill(image,sr,sc,actColor,newColor)
        return image