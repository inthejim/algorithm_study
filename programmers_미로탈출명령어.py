#시간초과
from collections import deque

dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
directions = ['d', 'l', 'r', 'u']



def solution(n, m, x, y, r, c, k):
    def get_distance(x, y, r, c):
        return abs(x - r) + abs(y - c)

    def bfs():
        visited = set()
        answer = 'impossible'
        queue = deque([(x-1, y-1, k, '')])

        while queue:
            cx, cy, ck, cstring = queue.popleft()

            if (cx, cy, ck) in visited or get_distance(cx, cy, r-1, c-1) > ck or (ck - get_distance(cx, cy, r-1, c-1)) % 2 == 1:
                continue

            visited.add((cx, cy, ck))

            if cx == r-1 and cy == c-1 and ck == 0:
                answer = cstring
                print(cstring)
                return answer

            if ck == 0:
                continue

            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    queue.append((nx, ny, ck-1, cstring + directions[i]))

        return answer
    return bfs() if bfs() != '' else 'impossible'
