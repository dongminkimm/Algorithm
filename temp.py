# from collections import deque

# tc = int(input())

# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

# def dfs(x ,y, visited, m, n):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx >= 0 and ny >= 0 and nx < n and ny < m:
#             if graph[nx][ny] not in visited:
#                 visited.add((nx, ny))
#                 visited = dfs(nx, ny, visited, m, n)
#                 return
#     return visited


# for _ in range(tc):
#     m, n, k = map(int, input().split())
#     graph = [[0] * m for _ in range(n)]
#     visited = set()

#     for _ in range(k):
#         a, b = map(int, input().split())
#         graph[b][a] = 1
    
#     cnt = 0
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] == 1:
#                 visited.add((i, j))
#                 visited = dfs(i, j, visited, m, n)
#                 cnt += 1
#     print(cnt)
