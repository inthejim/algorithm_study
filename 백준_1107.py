def possible(num, broken):
    if num == 0:
        if 0 in broken:
            return 0
        else:
            return 1
    
    length = 0
    while num > 0:
        d = num % 10
        if d in broken:
            return 0
        length += 1
        num //= 10
    return length

def main():
    N = int(input())
    M = int(input())

    broken = set()
    if M > 0:
        broken = set(map(int, input().split()))

    ans = abs(N - 100)

    for num in range(1000001):
        len1 = possible(num, broken)
        if len1 > 0:
            ans = min(ans, abs(num - N) + len1)

    print(ans)

if __name__ == "__main__":
    main()
