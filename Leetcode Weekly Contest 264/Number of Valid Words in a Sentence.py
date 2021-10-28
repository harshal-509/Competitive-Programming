class Solution:
    def countValidWords(self, sentence: str) -> int:
        l=sentence.split()
        ans=0
        for i in range(len(l)):
            x=l[i]
            flag=0
            c=0
            k=-1
            for i in range(len(x)-1):
                if(x[i]!="-" and not(ord(x[i])>=97 and ord(x[i])<=122)):
                    flag=1
                if(x[i]=="-" and (c==1)):
                    flag=1
                    k=i
                if(x[i]=='-' and c==0):
                    c=1
                    k=i
            a=0
            b=0
            if(k!=-1):
                for i in range(k,len(x)):
                    if((ord(x[i])>=97 and ord(x[i])<=122)):
                        a=1
                for i in range(k):
                    if((ord(x[i])>=97 and ord(x[i])<=122)):
                        b=1
            if(k!=-1 and (a==0 or b==0)):
                flag=1
            if(flag or x[-1]=="-"):
                pass
            else:
                if((ord(x[-1])>=97 and ord(x[-1])<=122) or (x[-1]=="," or  x[-1]=="." or  x[-1]=="!")):
                    ans+=1
        return ans