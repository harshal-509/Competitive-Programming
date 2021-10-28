class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        ans=-1
        for i in s.split():
            try:
                x=int(i)
                if(x>ans):
                    ans=x
                else:
                    return 0
            except:
                pass
        return 1