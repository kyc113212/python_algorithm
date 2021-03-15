from sys import stdin

def main():
    N, M = map(int, stdin.readline().split())    #size 입력
    matrix = [stdin.readline().rstrip() for _ in range(N)]
    dist = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)] #N*M행렬을 0으로 초기화
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = [(0,0)]
    visited[0][0] = 1

    while queue:
        y,x = queue.pop(0)
        if y == N-1 and x == M-1:
            print(dist[y][x] + 1)
            break
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if visited[ny][nx] == 0 and matrix[ny][nx] == '1':
                    visited[ny][nx] = 1
                    dist[ny][nx] = dist[y][x] + 1
                    queue.append((ny,nx))

if __name__ == '__main__':
    main()