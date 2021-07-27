#Author : koder_786
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        a=1
        z=Counter(s)
        t=""
        count=0
        for i in z:
            if(count==0):
                t=z[i]
                count+=1
            else:
                if(z[i]==t):
                    a+=1
        if(a==len(z)):
            return 1
        else:
            return 0