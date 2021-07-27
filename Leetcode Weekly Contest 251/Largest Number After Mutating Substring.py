#Author : koder_786
class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        ans1=""
        flag=1
        count=0
        for i in num:
            j=int(i)
            if(change[j]>j and flag):
                ans1+=str(change[j])
                count=1
            elif(change[j]==j):
                ans1+=str(change[j])
            else:
                ans1+=str(j)
                if(count==1):
                    flag=0
        return ans1