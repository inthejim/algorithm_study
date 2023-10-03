import sys

x,y,w,s=map(int, sys.stdin.readline().split(' '))
answer=0
if(w*2<=s):
    answer=(x+y)*w
else:
    tmp=min(x,y)
    answer+=tmp*s
    tmp2=max(x,y)-tmp
    if(tmp2%2==0):
        answer+=min(tmp2*s,tmp2*w)
    else:
        answer+=min(((tmp2-1)*s+w),tmp2*w)

print(answer)
