import sys

input = sys.stdin.readline

n = int(input().strip())
t = []
dp = [0] * n
maxIncome = 0
idx = 0

def findMaxIncome(idx, income):
    global maxIncome
    global t
    global dp
    if idx >= n:
        if income > maxIncome:
            maxIncome = income
        return
    
    findMaxIncome(idx + t[idx][0], income + t[idx][1])
    findMaxIncome(idx + 1, income)

for _ in range(n):
    t.append(list(map(int, input().strip().split())))

for i in range(n):
    if i + t[i][0] > n:
        t[i][1] = 0
    
for i in range(n):
    findMaxIncome(i, 0)
    
print(maxIncome)