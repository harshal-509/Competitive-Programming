class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        n=len(plants)
        i=0
        j=n-1
        ans=0
        a=capacityA
        b=capacityB
        while(i<=j):
            if(i==j):
                if(a>=plants[i]):
                    a-=plants[i]
                elif(b>=plants[i]):
                    b-=plants[i]
                else:
                    ans+=1
                i+=1
            else:
                if(a<plants[i]):
                    ans+=1
                    a=capacityA
                    a-=plants[i]
                else:
                    a-=plants[i]
                if(b<plants[j]):
                    ans+=1
                    b=capacityB
                    b-=plants[j]
                else:
                    b-=plants[j]
            i+=1
            j-=1
        return ans