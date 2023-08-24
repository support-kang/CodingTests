import sys

input = sys.stdin.readline

N, L = map(int, input().strip().split())
board = []

for _ in range(N):
    board.append(list(map(int, input().strip().split())))

def check(road): #road: 한 줄 리스트
    global L
    global N
    
    setted = [False] * N
    
    for i in range(len(road)): # 세가지로 구분할 수 있다 같은경우, 높아지는 경우, 낮아지는 경우
        if i == 0:
            continue
        if road[i] == road[i - 1]: # 같은 경우
            continue
        
        if road[i] > road[i - 1]: # 높아지는 경우
            if road[i] - road[i - 1] != 1:
                return False
            if i - L < 0:
                return False
            for j in range(i - L, i):
                if road[j] != road[i - 1]:
                    return False
                if setted[j]:
                    return False
                setted[j] = True
        
        if road[i] < road[i - 1]: # 낮아지는 경우
            if road[i - 1] - road[i] != 1:
                return False
            if i + L - 1 >= N:
                return False
            for j in range(i, i + L):
                if road[j] != road[i]:
                    return False
                if setted[j]:
                    return False
                setted[j] = True
    
    return True

def checkBoard(board):
    global N
    global L
    
    cnt = 0
    
    for i in range(N):
        if check(board[i]):
            cnt += 1
            
    for i in range(N):
        tmp = []
        for j in range(N):
            tmp.append(board[j][i])
        if check(tmp):
            cnt += 1
    
    return cnt

print(checkBoard(board))