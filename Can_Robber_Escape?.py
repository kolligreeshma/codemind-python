n=int(input())
lis=list(map(int,input().split()))
f=1
for i in lis:
    if i>=n:
        f=0
        break
if f==1:
    print("YES")
else:
    print("NO")