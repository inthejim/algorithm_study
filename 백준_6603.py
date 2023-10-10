import sys
from itertools import combinations

si=sys.stdin.readline
def solution(k, testcases):
    for item in combinations(testcases, 6):
        print(' '.join(list(map(str, item))))
    return 0

while(True):
    testcases=list(map(int, si().split(' ')))
    k=testcases[0]
    if(k==0):
        break
    testcases=testcases[1:]
    solution(k, testcases)
    print()
