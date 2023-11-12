def solution(sequence):
    answer = 0
    temp1=[]
    temp2=[]
    for i in range(len(sequence)):
        if(i%2==0):
            temp1.append(sequence[i]*1)
            temp2.append(sequence[i]*-1)
        if(i%2==1):
            temp1.append(sequence[i]*-1)
            temp2.append(sequence[i]*1)
            
    for i in range(1,len(sequence)):
        temp1[i]=max(temp1[i-1]+temp1[i], temp1[i])
        temp2[i]=max(temp2[i-1]+temp2[i], temp2[i])
    answer=max([max(temp1),max(temp2)])
    return answer
