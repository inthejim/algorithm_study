import sys

si=sys.stdin.readline

n=int(si())
data=[list(si().strip()) for _ in range(n)]
option_list=[]
for i in range(n):
    cnt=0
    for j in range(len(data[i])):
        if(j==0 or (1<=j and data[i][j-1]==' ')):
            if(data[i][j].upper() not in option_list):
                option_list.append(data[i][j].upper())
                cnt+=1
                data[i][j]='['+data[i][j]+']'
                break
    if cnt==0:
        for j in range(1, len(data[i])):
            if('A'<=data[i][j]<='z' and data[i][j].upper() not in option_list):
                option_list.append(data[i][j].upper())
                data[i][j]='['+data[i][j]+']'
                break

    print(''.join(data[i]))
