class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = s.split(" ")
        for x in range(len(words)):
            words[x] = words[x][::-1]
        return ' '.join(words)