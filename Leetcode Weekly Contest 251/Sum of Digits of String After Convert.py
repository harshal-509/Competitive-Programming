#Author : koder_786
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ans=0
        ans1=[]
        for i in s:
            ans1.append(int(str(ord(i)-96)))
        for i in range(k-1):
            s=ans1
            ans1=[]
            for j in s:
                t=int(j)
                while(t):
                    ans1.append(int(t%10))
                    t=t//10
            ans1=sum(ans1)
            ans1=list(str(ans1))
        ans2=[]
        for j in ans1:
                t=int(j)
                while(t):
                    ans2.append(int(t%10))
                    t=t//10
        for i in ans2:
            ans+=int(i)
        return ans