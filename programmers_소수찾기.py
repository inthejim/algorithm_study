from itertools import permutations

def determine_prime(find):
    print(find)
    i=2
    while(i*i<=find):
        if(find%i==0):
            return 0
        i+=1
    return 1

def solution(numbers):
    answer = 0
    numbers=list(map(int,numbers))
    prs=set()
    for num in range(1,len(numbers)+1):
        temp=set()
        for i in permutations(numbers,num):
            a=0
            k=1
            for j in i:
                a+=j*k
                k*=10
            temp.add(a)
        prs.update(temp)
    
    cnt=0
    
    for i in prs:
        if(i==0 or i==1):
            continue
        cnt+=determine_prime(i)
        
    answer=cnt
        
    return answer

