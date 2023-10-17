from collections import deque

def solution(begin, target, words):
    answer = 0
    queue=deque([])
    queue.append([begin,0])
    visited=[0]*len(words)
    while(queue):
        word, step=queue.popleft()
        if(word==target):
            answer=step
            break
            
        for idx, w in enumerate(words):
            if(visited[idx]==0):
                cnt=0
                for i in range(len(w)):
                    if w[i]!=word[i]:
                        cnt+=1
                if(cnt==1):
                    queue.append([w, step+1])
                    visited[idx]=1

    return answer
