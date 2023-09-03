def solution(triangle):
    answer = 0
    height=len(triangle)
    result=[[0]*height for _ in range(height)]
    result[0][0]=triangle[0][0]
    i=2
    while(i<=height):
        for j in range(i):
            if(j==0):
                result[i-1][j]=result[i-2][j]+triangle[i-1][j]
            elif(j==i-1):
                result[i-1][j]=result[i-2][j-1]+triangle[i-1][j]
            else:
                result[i-1][j]=triangle[i-1][j]+max(result[i-2][j-1],result[i-2][j])
        i+=1
    answer=max(result[height-1])
        
        
    return answer
