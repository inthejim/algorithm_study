import sys

si=sys.stdin.readline

r,c,t=map(int,si().split(' '))

rooms=[[*map(int, si().split(' '))] for _ in range(r)]

cleaners=[]

#top 기준
tx=[0,-1,0,1]
ty=[1,0,-1,0]
#bottom 기준
bx=[0,1,0,-1]
by=[1,0,-1,0]

def find():
    for i in range(r):
        for j in range(c):
            if(rooms[i][j]==-1):
                cleaners.append((i,j))
                if(len(cleaners)==2):
                    return
find()
top_cleaner, bottom_cleaner=cleaners
top=top_cleaner
top_dir=0
bottom=bottom_cleaner       
bottom_dir=0        

def top_func(visited,top_dir):
    if(top[0]==top_cleaner[0] and top[1]==top_cleaner[1]):
        return visited,top_dir
    cnt=0
    for i in range(4):
        nx=top[0]+tx[i]
        ny=top[1]+ty[i]
        if(0<=nx<r and 0<=ny<c):
            cnt+=1
    d_values=rooms[top[0]][top[1]]//5
    rooms[top[0]][top[1]]=max(0, rooms[top[0]][top[1]]-d_values*cnt)
    
    for i in range(4):
        nx=top[0]+tx[i]
        ny=top[1]+ty[i]
        if(0<=nx<r and 0<=ny<c and rooms[nx][ny]!=-1):
            visited[nx][ny]=d_values

    if(not (0<=top[0]+tx[top_dir]<=top_cleaner[0] and 0<=top[1]+ty[top_dir]<c)):
        top_dir+=1
    top[0]+=tx[top_dir]
    top[1]+=ty[top_dir]
    return visited,top_dir


def bottom_func(visited,bottom_dir):
    if(bottom[0]==bottom_cleaner[0] and bottom[1]==bottom_cleaner[1]):
        return visited,bottom_dir
    cnt=0
    for i in range(4):
        nx=bottom[0]+bx[i]
        ny=bottom[1]+by[i]
        if(0<=nx<r and 0<=ny<c and rooms[nx][ny]!=-1):
            cnt+=1
    d_values2=rooms[bottom[0]][bottom[1]]//5
    rooms[bottom[0]][bottom[1]]=max(0, rooms[bottom[0]][bottom[1]]-d_values2*cnt)
    
    for i in range(4):
        nx=bottom[0]+bx[i]
        ny=bottom[1]+by[i]
        if(0<=nx<r and 0<=ny<c):
            visited[nx][ny]=d_values2

    if(not (bottom_cleaner[0]<=bottom[0]+by[bottom_dir]<r and 0<=bottom[1]+by[bottom_dir]<c)):
        bottom_dir+=1
    bottom[0]+=bx[bottom_dir]
    bottom[1]+=by[bottom_dir]
    return visited,bottom_dir

while(t):
    visited=[[0]*c for _ in range(r)]
    vistied,top_dir=top_func(visited,top_dir)
    visited,bottom_dir=bottom_func(visited, bottom_dir)
    
    for i in range(r):
        for j in range(c):
            rooms[i][j]+=visited[i][j]
    
    t-=1

print(sum(map(sum, rooms))+2)

