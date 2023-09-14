def solution(n, computers):
    global visited
    answer = 0
    visited=[0]*(len(computers)+1)
    network=0
    for i in range(len(computers)):
        if(visited[i]==0):
            visited[i]=1
            dfs(i,computers)
            network+=1
    
    answer=network
        
    
    return answer

def dfs(start, computers):
    global visited
    for i in range(len(computers)):
        if(computers[start][i]==1 and visited[i]==0):
            visited[i]=1
            dfs(i, computers)
