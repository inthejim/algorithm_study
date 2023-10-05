import copy

global L,C,array
L, C=map(int,input().split())
array=sorted(list(input().split()))
selected=[0 for _ in range(C)]

def recursive(idx, check1, check2, cnt, selected):
    if(L-cnt> C-idx):
        return
    if(L==cnt):
        if(check1>=2 and check2>=1):
            answer=''
            for i in range(C):
                if(selected[i]):
                    answer+=array[i]
            print(answer)
        return
    for i in range(idx+1,C):
        if(selected[i]==0):  
            temp=copy.deepcopy(selected)
            temp[i]=1
            if(array[i] in ['a','i','e','o','u']):
                recursive(i, check1,check2+1,cnt+1, temp)
            else:
                recursive(i, check1+1,check2,cnt+1, temp)
    return 

for i in range(C):
    # recursive(i,0,0,0,selected)
    temp=copy.deepcopy(selected)
    temp[i]=1
    if(array[i] in ['a','i','e','o','u']):
        recursive(i,0,1,1,temp)
    else:
        recursive(i,1,0,1,temp)
        
