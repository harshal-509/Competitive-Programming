#Author:harshal_509
for _ in range(int(input())):
    s=input()
    h={}
    for i in range(97,123):
        h[chr(i)]=0
    if(s.count("a")==1):
        if(len(s)==0):
            print("YES")
        else:
            flag=1
            if(s[0]>s[-1]):
                a=s[0]                
                i=1
                j=len(s)-1
            else:
                a=s[-1]
                i=0
                j=len(s)-2
            while(i<=j):
                if(ord(s[i])==ord(a)-1):
                    a=s[i]
                    i+=1
                elif(ord(s[j])==ord(a)-1):
                    a=s[j]
                    j-=1
                    
                else:
                    flag=0
                    break
            if(flag):
                print("YES")
            else:
                print("NO")
    else:
        print("NO")