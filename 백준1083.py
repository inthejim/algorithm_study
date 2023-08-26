import sys

si=sys.stdin.readline

n=int(si().strip())
data=list(map(int,si().strip().split()))
s=int(si().strip())

# 215
# 251
# 521
# 2

for i in range(n):
    if s<=0 :
        break

    checkrange = i+s+1 if (i+s+1<n) else n
    mx_idx=data.index(max(data[i:checkrange]))

    for j in range(mx_idx, i, -1):
        data[j],data[j-1]=data[j-1],data[j]

    s-=(mx_idx - i)

print(*data)
