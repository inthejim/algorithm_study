import sys

si=sys.stdin.readline

n=int(si())
org_data=list(si().strip() for _ in range(n))
data=sorted(org_data)
print(data)

def check_word(word1, word2):
    length=min(len(word1),len(word2))
    cnt=0
    for i in range(length):
        if(word1[i]==word2[i]):
            cnt+=1
        else:
            break
    return cnt

answer=set()
total_max_value=0
for i in range(len(data)-1):
    if(len(data[i+1])<total_max_value):
        continue
    max=check_word(data[i],data[i+1])
    print(data[i],data[i+1])
    if(total_max_value<max):
        total_max_value=max
        answer=set([data[i],data[i+1]])

    elif(total_max_value==max):
        answer.update([data[i],data[i+1]])

print(answer)
answer=list(answer)
answer.sort(key=lambda x: org_data.index(x))
answer=answer[:2]
for i in answer:
    print(i)
