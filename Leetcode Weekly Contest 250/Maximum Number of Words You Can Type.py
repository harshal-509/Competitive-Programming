#Author : koder_786
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ans=0
        text=text.split()
        for i in text:
            flag=1
            for j in brokenLetters:
                if(j in i):
                    flag=0
                    break
            if(flag):
                ans+=1
        return ans