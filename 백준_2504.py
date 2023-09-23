import sys

si=sys.stdin.readline

data=list(si())
stack=[]
t=1
answer=0
for i,val in enumerate(data):
    if(val=='('):
        stack.append(val)
        t*=2
    elif(val=='['):
        stack.append(val)
        t*=3
    elif(val==')'):
        if(not stack or stack[-1]=='['):
            answer=0
            break
        if(data[i-1]=='('):
            answer+=t
        t//=2
        stack.pop()
    elif(val==']'):
        if(not stack or stack[-1]=='('):
            answer=0
            break
        if(data[i-1]=='['):
            answer+=t
        t//=3
        stack.pop()
if stack: answer=0
print(answer)
