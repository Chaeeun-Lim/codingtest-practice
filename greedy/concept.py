'''
그리디 알고리즘(탐욕법)
- 현재상황에서 지금 당장 좋은 것만 고르는 방법을 의미한다
- 일반적인 그리디 알고리즘은 문제를 풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력을 요구한다
- 그리디 해법은 정당성분석이 중요하다
    단순히 가장 좋아보이는 것을 반복적으로 선택해도 최적의 해를 구할 수 있는지 검토
- 일반적인 상황에서 그리디 알고리즘은 최적의 해를 보장할 수 없을 때가 많다
- 하지만 코딩테스트에서 대부분의 그리디문제는 탐욕법으로 얻은 해가 최적의 해가 되는 상황에서, 이를 추론할 수 있어야 풀리도록 출제가 된다.
'''
'''
대표적인 예 : 거스름돈
- 당신은 음식점의 계산을 도와주는 점원입니다. 카운터에는 거스름돈으로 사용할 500원 100원 50원 10원짜리 동전이 무한개 존재한다고 가정합니다.
손님에게 거슬러 주어야 할 돈이 n원일 때 거슬러 주어야할 동전의 최소 갯수를 구하시오. 단, 거슬러 줘야할 돈 n은 항상 10의 배수

- 아이디어
    최적의 해를 빠르게 구하기 위해서는 가장 큰 화폐단위 부터 돈을 거슬러주면됨
    n원을 거슬러줘야할 때, 가장먼저 500원으로 거슬러 줄 수 있을만큼 거슬러주고 그 이후 100 50 10동전을 차례로 
    
- 정당성 분석
    기징 큰 화폐단위부터 돈을 거슬러 주는 것이 최적의 해를 보장하는 이유는 무엇일까?
    가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전들을 종합해 다른 해가 나올 수 없다
    만약 n이 800원 이고 화폐단위가 500 400 100 이라면?
    그리디 알고리즘 문제에서는 이처럼 문제풀이를 위한 최소한의 아이디어를 떠올리고 이것이 정당한지 검토할 수 있어야한다.
    
- 시간복잡도 분석
    화폐의 종류가 k라고 할 때, 소스코드의 시간복잡도는 O(k)
    이 알고리즘의 시간복잡도는 거슬러줘야하는 금액과는 무관하며 동전의 총 종류에만 영향을 받음

n = 1260일때의 예시 확인해보자
'''

'''
n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
array = [500, 100, 50, 10]

for coin in array:
    count += n // coin #해당화폐로 거슬러줄 수 있는 동전의 개수 세기
    n %= coin

print(count)
'''

'''
문제 : 1이될때까지

- 문제설명 : 어떠한 수 N이 1이 될 때 까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다
            단 두번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다.
    1. N에서 1을 뺀다
    2. N을 K로 나눈다
    
    예를들어 N이 17 K가 4라고 가정하면 이때 1번의 과정을 한번 수행하면 N은 16이 된다 이후 2번의 과정을 2번 수행하면 N은 1이 된다
    결과적으로 이 경우 전체과정을 실행한 횟수는 3이 된다, 이는 N을 1로 만드는 최소 횟수다
    
    N과 K가 주어질 때 N이 1이 될때까지 1 혹은 2번의 과정을 수행해야하는 최소 횟수를 구하는 프로그램을 작성해라
    
풀이시간 : 15분, 시간제한 : 2초,  메모리제한 : 128MB
입력조건 : 첫째줄에는 N(1<=N<=100000)과 K(2<=K<=100,000)이 공백을 기준으로 출력됨 각각 자연수로 주어짐
출력조건 : 최소수행횟수 출력 

해결아이디어 : 주어진 N에 대해서 최대한 많이 나누기 수행
N의 값을 줄일 때 2이상의 수로 나누는 작업이 1을 빼는 작업보다 수를 훨씬 많이 줄일 수 있다
예를들오 N=25 K=3일경우 

정당성 분석: 가능하면 최대한 많이 나누는 작업이 최적해를 보장하냐?
N이 아무리 큰수여도 K로 계속 나누면 기하급수적으로 빠르게 줄일 수 있다
K가 2이상이기만 하면 K로 나누는 것이 1을 빼는 것보다 할상 빠르게 N을 줄일 수 있다
또한 N은 항상 1에 도달 가능
'''

'''
n, k = map(int, input().split())
cnt = 1

while True: # 기하급수적으로 줄어들기 떄문에 로그시간복잡도
    #N이 K로 나누어 떨어지는 수가 될때까지 뺀다
    #target은 만약 n이 k로 나누어떨어지지 않을 때 가장 가까운 나누어떨어지는 수가 뭔지 구한다
    target = (n//k)*k
    cnt += (n - target)
    n = target

    #N이 K보다 작을 때 (더 이상 나눌 수 없을 때 반복문 탈출)
    if n<k:
        break
    #K로 나누기
    cnt += 1
    n //= k

# 마지막으로 남은 수에 대해 1씩 빼기
cnt += (n-1)
print(cnt)
'''

'''
문제 : 곱하기 혹은 더하기

- 문제설명 : 각자리가 숫자 0부터9로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽까지 하나씩 모든 숫자를 확인해가며
    숫자 사리에 x 혹은 +연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오
    단, +보다 x를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정

ex) 02984라는 문자열이 있을 때 가장 큰 수는
((((0+2)*9)*8)*4) = 576입니다. 또한 만들어질 수 있는 가장 큰 수는 항상 20억 이하의 정수가 되도록 입력이 주어진다.

풀이시간 30분 | 시간제한 1초 | 메모리제한 128MB 
입력조건 : 첫번째 줄에 여러개의 숫자로 구성된 하나의 문자열 S가 주어진다 (1<= S의 길이 <=20)
출력조건 : 만들어질 수 있는 가장 큰수 

- 아이디어 : 대부분의 경우 +보다 x가 값을 더 크게 만든다
    다만 두 수 중에서 하나라도 0이나 1일 경우 곱하기보다 더하기를 수행하는 것이 효율적이다
    따라서 두 수에 대해서 연산을 수행할 때 두수 중에서 하나라도 1 이하인 경우 더하며 두 수 모두 2 이상인경우 곱
'''
'''
str = input()
result = int(str[0])
for i in range(1,len(str)):
    if result <= 1:
        result += int(str[i])
    elif int(str[i]) <= 0:
        result += int(str[i])
    else:
        result *= int(str[i])
print(result)
'''
'''
문제 : 모험가 길드 

-문제설명 : 한 마을에 모험가가 N명있다. 모험가 길드에서는 N명의 모험가를 대상으로 공포도를 측정했는데, 
    공포도가 높은 모험가는 쉽게 공포를 느껴 위험상황 대처 능력이 떨어짐
    모험가 길드장인 채은이는 모험가 그룹을 안전하게 구성하고저 공포도가 X인 모험가는 반드시 X명 이상으로
    구성한 모함가 그룹에 참여해야 여행을 떠날 수 있도록 규정했다
    채은이는 최대 몇 개의 모험가 그룹을 만들 수 있을까? N명의 모험가에 대한 정보가 주어졌을때
    여향을 떠날 수 있는 그룹수의 최댓값을 구하는 프로그램을 작성
    
- 예 ) N=5이고 각 모험가의 공포도는 2 3 1 2 2
    이 경우 그룹 1에 공포도가 1 2 3인 모험가를 한 명씩 넣고 그룹2에 공포도가 2인 남은 두명을 넣으면 총 2개의 그룹 생성가능
    또한 몇명의 모험가는 마음에 그대로 남아 있어도 되기때문에 모든 모험가가 그룹에 들어갈 필요는 없다
    
- 입력조건 : 첫째 줄에 모험가의 수 N이 주어짐
            둘째 줄에 각 모험가의 공포도 값을 N이하의 자연수로 주어지며 각 자연수는 공백으로 구분
- 출력조건 : 여행을 떠날수 있는 그룹의 최댓값 구하기

- 아이디어 : 오름차순 정렬 이후에 공포도가 가장 낮은 모험가부터 하나씩 확인
    앞에서부터 공포도를 하나씩 확인하며 '현재 그룹에 포함된 모험가의 수'가 '현재 확인하고 있는 공포도보다 크거나 같다면' 이를 그룹으로 설정
    이러한 방법을 사용하면 공포도가 오름차순으로 정렬되어 있다는 점에서, 항상 최소한의 모험가의 수만 포함해 그룹을 결성
'''
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0  #총 그룹의 수
cnt = 0 #현재 그룹에 포함된 모험가의 수

for i in data:  #공포도 낮은 것 부터 차례로 확인
    cnt += 1    #현재 그룹에 해당 모험가를 포함시킴
    if cnt >= i:    #현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이면, 그룹결정
        result += 1
        cnt = 0

print(result)



