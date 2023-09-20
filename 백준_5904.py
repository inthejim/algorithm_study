import sys
si=sys.stdin.readline
n=int(si())

s0='moo'
def bf(n, depth, b_len):
    new_len=2*b_len +1+ depth+2
    if(n<=3):
        print(s0[n-1])
        return
    if new_len<n:
        bf(n,depth+1, new_len)
    else:
        if(b_len+1==n):
            print('m')
            return
        elif(n<=b_len+depth+2+1):
            print('o')
            return
        else:
            bf(n-(b_len+depth+2+1),1,3)

bf(n,1,3)

    
