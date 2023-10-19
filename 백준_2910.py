import sys

si=sys.stdin.readline

n,c=si().split(' ')
data=[*map(int,si().split(' '))]
dic={}
for i in data:
    dic[i]=dic.get(i,0)+1
sortedDic=sorted(dic.items(),key=lambda x:x[1],reverse=True)

print(''.join(list(((str(x[0])+' ')*x[1]) for x in sortedDic)).lstrip())
