#Author : koder_786
class Solution:
    def minimumMoves(self, s: str) -> int:
        n=len(s)
        a=0
        i=0
        while(i<n-2):
            if(s[i]=="X" and i<n-2):
                a+=1
                i+=2
            i+=1
        while(i<n):
            if(s[i]=="X"):
                a+=1
                break
            i+=1
        return a