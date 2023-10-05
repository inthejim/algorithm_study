a=list(list(map(int,input().strip())) for i in range(4))
r=int(input())
instruction=list(list(map(int,input().split())) for i in range(r))

global rotation


def leftcheck(wheel,clock):
    global rotation
    if(wheel<=0):
        return
    if(a[wheel][6]!=a[wheel-1][2]):
        rotation[wheel-1]=clock*-1
        leftcheck(wheel-1,clock*-1)
        

def rightcheck(wheel,clock):
    global rotation
    if(wheel>=3):
        return
    if(a[wheel][2]!=a[wheel+1][6]):
        rotation[wheel+1]=clock*-1
        rightcheck(wheel+1, clock*-1)
        

for i in range(r):
    rotation=[0 for i in range(4)]
    wheel=instruction[i][0]-1
    clock=instruction[i][1]
    rotation[wheel]=clock
    leftcheck(wheel,clock)
    rightcheck(wheel,clock)
    
    for j in range(4):
        if(rotation[j]==1):
            a[j]=[a[j][7]]+a[j][0:7]
        elif(rotation[j]==-1):
            a[j]=a[j][1:8]+[a[j][0]]

answer=0
k=1

for i in range(4):
   answer+=(a[i][0]-0)*k
   k*=2
print(answer)
