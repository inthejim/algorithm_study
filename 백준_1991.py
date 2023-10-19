n=int(input())
aa=[[] for i in range(n)]
for i in range(n):
    a,b,c=input().split()
    aa[ord(a)-ord('A')].append(b)
    aa[ord(a)-ord('A')].append(c)

def dfs(aa, visited,idx,print_list):
    if(visited[idx]==1):
        return
    visited[idx]=1
    for i in range(2):
        k=ord(aa[idx][i])-ord('A')
        if(0<k<n):
            print_list.append(aa[idx][i])
            dfs(aa,visited,k,print_list)

visited=[0 for i in range(n)]
print_list=[]
print_list.append('A')

for i in range(n):
    dfs(aa,visited,i,print_list)
for i in range(n):
    print(print_list[i],end='')

def dfs_1(aa,idx):
    visited=[]
    visited.append(chr(idx+ord('A')))
    i=idx
    while(True):
        k=ord(aa[i][0])-ord('A')
        if(0<k<n):
            visited.append(aa[i][0])
            i=k
        else:
            break
    while(visited):
        v=visited.pop()
        print(v,end='')
        k=ord(v)-ord('A')
        if(aa[k][1]!='.'):
            m=ord(aa[k][1])-ord('A')
            dfs_1(aa,m)


def dfs_2(aa,idx,n):
    visit=[0 for i in range(n)]
    visited=[]
    visited.append(idx)
    visit[idx]=1
    while(visited):
        i=visited[-1]
        l=ord(aa[i][0])-ord('A')
        r=ord(aa[i][1])-ord('A')
        if(l<0 and r<0):
            v=visited.pop()
            print(chr(v+ord('A')),end='')
            continue
        if(0<=l and visit[l]==1 and 0<=r and visit[r]==1):
            v=visited.pop()
            print(chr(v+ord('A')),end='')
            continue
        if((0>l and 0<=r and visit[r]==1) or (0>r and 0<=l and visit[l]==1)):
            v=visited.pop()
            print(chr(v+ord('A')),end='')
            continue
        if(0<=r<n and visit[r]==0):
            visited.append(r)
            visit[r]=1
        if(0<=l<n and visit[l]==0):
            visited.append(l)
            visit[l]=1
        
print()            
dfs_1(aa,0)
print()

dfs_2(aa,0,n)
print()
            
