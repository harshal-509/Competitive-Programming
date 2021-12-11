class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        mod=1000000007
        def lcm(a,b):
            return (a*b)//gcd(a,b)
        x=min(a,b)
        i=x
        j=x*n
        while(i<j):
            m=i+(j-i)//2
            x=m//a+m//b-m//lcm(a,b)
            if(x>=n):
                j=(m)
            else:
                i=(m)+1
        return (j)%mod
