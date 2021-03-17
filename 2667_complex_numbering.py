from sys import stdin

def numbering(n, matrix, visited, y, x, color, color_map):

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == 0 and matrix[ny][nx] == '1':
            visited[ny][nx] = 1
            color_map[ny][nx] = color
            numbering(n, matrix, visited, ny, nx, color, color_map)





if __name__ == '__main__':

    N = int(input())
    matrix = [stdin.readline().rstrip() for _ in range(N)]  # 한줄을 str로 읽고 N행만큼 읽는다.
    visited = [[0] * N for _ in range(N)]
    color_map = [[0] * N for _ in range(N)]
    color = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == '1' and visited[i][j] == 0:
                color += 1
                visited[i][j] = 1
                color_map[i][j] = color
                numbering(N, matrix, visited, i, j, color, color_map)

    print(color)
    rst = [0] * color
    for i in range(1, color + 1):
        for j in range(N):
            for k in range(N):
                if color_map[j][k] == i:
                    rst[i - 1] = rst[i - 1] + 1

    rst.sort()
    for m in rst:
        print(m)
