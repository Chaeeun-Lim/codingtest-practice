'''
DP(동적 계획법, 다이나믹 프로그래밍) : 메모리를 적절히 사용하여 수행시간 효율성을 비약적으로 향상시키는 방법
    이미 계산된 결과는 별도의 메모리 영역에 저장하여 다시 계산하지 않도록, 구현은 일반적으로 두가지 방식(탑다운, 보텀업)으로 구성

* 특정 문제가 다음의 조건을 만족할 때 사용
    1. 최적 부분 구조 : 큰 문제를 작은 문제로 나눌 수 있으며, 작은 문제의 답을 모아 큰 문제를 해결할 수 있다.
    2. 중복되는 부분 문제 : 동일한 작은 문제를 반복적으로 해결해야 한다.
'''
# 피보나치 수 구해보기 (재귀)
def fibonaci(n):
    if n == 1 or n == 2:
        return 1
    return fibonaci(n-1) + fibonaci(n-2)

print(fibonaci(4))
'''
단순 재귀함수로 구현하면 지수시간 복잡도를 가짐(2^n) 어떤 부분이 여러번 호출됨 (중복되는 부분 문제)

dp는 사용조건을 만족하는지 확인
- 큰 문제를 작은 문제로 나눌 수 있는지 -> 0 : f(3)을 f(2) + f(1)로
- 중복되는 부분 문제 : 0 : f(2) 등이 매우 많이 호출

[메모이제이선] : 한번 계산한 결과를 메모리 공간에 메모하는 기법, 값을 기록해놓는다는 점에서 캐싱이라고도 한다.

[탑다운(메모이제이션) 방식은 하향식이라고도하며 보텀업은 상향식이라고도 함]
dp의 전형적인 형태는 보텀업, 결과저장용 리스트는 dp테이블이라고 부름. 
엄밀히말하면 메모이제이션은 이전에 계산된 결과를 일시적으로 기록해 놓는 넒은 개념(dp에 국한된 개념은 아님)
'''
# 피보나치 with DP
# 한번 계산된 결과 메모이제이션하기위한 리스트 초기화
d = [0] * 100

def fibo(n):
    if n == 1 or n == 2:
        return 1
    if d[n] != 0:
        return d[n]
    d[n] = fibo(n-1) + fibo(n-2)
    return d[n]

print(fibo(99))

# 보텀업 방식
dp = [0] * 100
dp[1] = 1
dp[2] = 1
n = 99
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])

# 예시1: 개미전사
#n = int(input())
#k = list(map(int, input().split()))
n = 4
k = [1,3,1,5]

d = [0] * 100
d[0] = k[0]
d[1] = max(d[0], k[1])

for i in range(n):
    d[i] = max(d[i-1], d[i-2] + k[i])

print(d[n-1])

# 1로 만들기
#x = int(input())
x = 4
d = [0] * 30001

for i in range(2, x+1):
    d[i] = d[i-1]+1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)

print(d[x])

# 효율적인 화폐구성
#n, target = map(int, input().split())
#bills = []
#for _ in range(n):
#    bills.append(int(input()))
n, target = 2, 15
bills = [2, 3]

d = [10001] * (target+1)
d[0] = 0
for i in range(n):
    for j in range(bills[i], target+1):
        if d[j - bills[i]] != 10001:
            d[j] = min(d[j], d[j - bills[i]] + 1)
if d[target] == 10001:
    print(-1)
else:
    print(d[target])
    print(d)

# 금광
#t = int(input())
t = 1
for _ in range(t):
    #n, m = map(int, input().split())
    n, m = 3, 4
    #golds = list(map(int, input().split()))
    golds = [1, 3, 3, 2, 2, 1, 4, 1, 0, 6, 4, 7]
    dp = []
    idx = 0
    # 테이블 입력받기
    for _ in range(n):
        dp.append(golds[idx:idx+m])
        idx += m
    print(dp)
    # dp진행
    for y in range(1, m):
        for x in range(n):
            # 위에서 내려올때
            if x == 0:
                left_up = 0
            else:
                left_up = dp[x-1][y-1]
            # 아래서 오는 경우
            if x == n-1:
                left_down = 0
            else:
                left_down = dp[x+1][y-1]
            # 옆에서 오는 경우
            left = dp[x][y-1]
            dp[x][y] = dp[x][y] + max(left, left_down, left_up)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)

# 병사 배치하기
#n = int(input())
#m = list(map(int, input().split()))
n = 7
m = [15, 11, 4, 8, 5, 2, 4]

m.reverse()
dp = [1] * n
for i in range(1, n):
    for j in range(0, i):
        if m[i] > m[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(n - max(dp))


