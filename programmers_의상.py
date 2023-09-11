import collections
import itertools

def solution(clothes):
    answer = 0
    data = collections.defaultdict(list)
    len_data=[]
    cnt=0
    
    for cloth,key in clothes:
        data[key].append(cloth)
    
    for key, value in data.items():
        len_data.append(len(value))
    
    for i in range(1,len(len_data)+1):
        combi=itertools.combinations(len_data,i)
        multi=1
        for j in combi:
            for k in j:
                multi*=int(k)
            cnt+=multi
            multi=1
            
        
    answer=cnt
    
    return answer
