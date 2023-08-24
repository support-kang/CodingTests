import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())
r, c, d = map(int, input().strip().split())

room = []
room.append([1] * (M + 2))
for i in range(N):
    room.append([1] + list(map(int, input().strip().split())) + [1])
room.append([1] * (M + 2))

def checkUncleanedAround(row, col):
    global room
    
    if room[row - 1][col] == 0:
        return True
    if room[row][col + 1] == 0:
        return True
    if room[row + 1][col] == 0:
        return True
    if room[row][col - 1] == 0:
        return True
    
    return False

row = r + 1
col = c + 1
cnt = 0

#   0
# 3   1
#   2

while True: #cleaned = 2
    if room[row][col] == 0:
        room[row][col] = 2
        cnt += 1
    
    if checkUncleanedAround(row, col):
        d -= 1
        if d < 0:
            d = 3
        if d == 0:
            if room[row - 1][col] == 0:
                row -= 1
                continue
        elif d == 1:
            if room[row][col + 1] == 0:
                col += 1
                continue
        elif d == 2:
            if room[row + 1][col] == 0:
                row += 1
                continue
        elif d == 3:
            if room[row][col - 1] == 0:
                col -= 1
                continue
    else:
        if d == 0:
            if room[row + 1][col] == 1:
                break
            else:
                row += 1
                continue
        elif d == 1: 
            if room[row][col - 1] == 1:
                break
            else:
                col -= 1
                continue 
        elif d == 2:
            if room[row - 1][col] == 1:
                break
            else:
                row -= 1
                continue
        elif d == 3:
            if room[row][col + 1] == 1:
                break
            else:
                col += 1
                continue
            
print(cnt)