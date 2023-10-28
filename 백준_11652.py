import sys

si=sys.stdin.readline

n=int(si())
dict={}

for i in range(n):
    component=int(si())
    if(dict.get(component,0)):
        dict[component]+=1
    else:
        dict[component]=1
    
sorted_dict=sorted(dict.items(),key=lambda x: (-x[1],x[0]))
print(sorted_dict[0][0])




    
