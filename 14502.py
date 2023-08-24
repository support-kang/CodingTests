import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().strip().split())
board = []
viruses = []
maxSafeArea = 0

for _ in range(N): #input
    board.append(list(map(int, input().strip().split())))
    
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            viruses.append([i, j])

# 빈 칸의 위치를 미리 저장
empty = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            empty.append([i, j])

# 빈 칸 중에서 3개를 조합하여 벽을 세우는 함수
def buildWalls():
    global maxSafeArea
    global board
    # 빈 칸의 조합을 생성
    comb = combinations(empty, 3)
    # 각 조합에 대해 벽을 세우고 바이러스를 퍼뜨림
    for c in comb:
        for x, y in c:
            board[x][y] = 1 # 벽을 세움
        tmpBoard = spreadVirus(board) # 바이러스를 퍼뜨림
        safeArea = countSafeArea(tmpBoard) # 안전 영역을 계산
        if safeArea > maxSafeArea: # 최대값 갱신
            maxSafeArea = safeArea
        for x, y in c:
            board[x][y] = 0 # 벽을 복구함
    
def spreadVirus(board):
    global viruses
    tmpBoard = [row[:] for row in board]
    for virus in viruses:
        spreadVirusFrom(virus[0], virus[1], tmpBoard)
    return tmpBoard


def spreadVirusFrom(n, m, board): # BFS
    queue = deque()
    queue.append([n, m])
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                board[nx][ny] = 2
                queue.append([nx, ny])

        
def countSafeArea(board):
    count = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                count += 1
    return count

buildWalls()
print(maxSafeArea)
