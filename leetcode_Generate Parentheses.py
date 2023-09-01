from collections import deque
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        q=deque([])
        data=[]
        res='('
        untilNow=0
        nowIdx=1
        
        if(nowIdx==n):
            res+=')'
            data.append(res)
            return data
        for j in range(0, nowIdx+1-untilNow):
            q.append([untilNow+j,nowIdx+1,res+")"*j])
        print(q)

        while(q):
            v= q.popleft()
            untilNow,nowIdx,result=v[0],v[1],v[2]
            
            if(untilNow==n):
                data.append(result)
                continue

            result+='('
            if(nowIdx==n):
                result+=")"*(n-untilNow)
                data.append(result)
                continue
            
            for j in range(0, nowIdx+1-untilNow):
                c=result+')'*j
                q.append([untilNow+j,nowIdx+1,c])
        
        return data
