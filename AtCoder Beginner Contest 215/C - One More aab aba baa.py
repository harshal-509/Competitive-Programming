from itertools import permutations
l=list(input().split())
s=l[0]
k=int(l[1])
t=sorted(set((permutations(s))))
print("".join(t[k-1]))