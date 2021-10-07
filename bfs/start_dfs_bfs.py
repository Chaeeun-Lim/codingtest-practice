# stack 자료구조

stack = []
stack.append(5)
stack.append(3)
stack.append(2)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()
# 나가는 순서대로 최상단부터 출력
print(stack[::-1])
# 일반 리스트 순서로 출력
print(stack)

# queue 자료구조
# 큐 구현을 위해 deque 라이브러리 사용
from collections import deque
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
# 가장 왼쪽에 있는 원소 출력
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

# 먼저 들어온 순서대로 출력
print(queue)
# 역순으로 변경
queue.reverse()
# 나중들어온 원소부터 출력
queue.popleft()
print(queue)

# 재귀함수 : 자기자신을 다시 호출하는 함수
# 단순한 재귀함수 예제
'''
def recursive_function():
    print("재귀함수를 호출합니다.")
    recursive_function()

recursive_function()

# 재귀함수를 문제풀이에 사용할 때에는 재귀함수의 종료조건을 반드시 명시해야 합니다.
def recursive_function_2(i):
    # 100번째 호출을 했을 때 종료되도록 조건을 명시
    if i == 100:
        return
    print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출합니다.')
    recursive_function_2(i+1)
    print(i, '번째 재귀함수를 종료합니다.')

recursive_function_2(1)
'''
# 팩토리얼 구현예제
# 0! 1! 은 모두 1이다.
# 반복적으로 구현한 n!
'''
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1:
        # n이 1이하인 경우 1을 반환
        return 1
    # n! = n * (n - 1)!를 그대로 코드로 작성하기
    return n * factorial_iterative(n-1)

# 각각의 방식을 이용한 n! 출력
print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))
'''

# 최대공약수(GCD) 계산(유클리드 호제법)
# 두개의 자연수에 대한 최대공약수를 구하는 대표적인 알고리즘
'''
유클리드 호제법
    두 자연수 A, B에 대해 (A>B) A를 B로 나눈 나머지를 R이라고 한다.
    이때 A와 B의 최대공약수는 B와 R의 최대공약수와 같다.

유클리드 호제법 아이디어를 그대로 재귀함수로 작성할 수 있다.
def gcd(a, b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a % b)

print(gcd(192, 162))

재귀함수 유의사항
    재귀함수를 잘 활용하면 복잡한 알고리즘을 간결하게 작성할 수 있다.
    단, 오히려 다른사람이 이해하기 어려운 코드가 될 수 있으므로 신중하게 작성해야 한다.
    모든 재귀함수는 반복문을 이용하여 동일한 기능을 구현할 수 있다.
    재귀함수가 반복문보다 유리한 경우도 있고 불리한 경우도 있다.
    컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓입니다.
        그래서 스택을 사용해야 할 때 구현 상 스택 라이브러리 대신에 재귀함수를 이용하는 경우가 많다.
'''




