class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        x=n+1
        if(n>=666666):
            return 1224444
        while(1):
            m=str(x)
            z=Counter(m)
            a=0
            for i in z:
                if(z[i]==int(i)):
                    a+=1
            if(len(z)==a):
                return x
            x+=1