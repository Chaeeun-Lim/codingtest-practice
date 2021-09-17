'''
실전에서 유용한 표준 라이브러리
-내장함수 : 기본입출력 함수부터 정렬함수까지 기본적인 함수들을 제공
-itertools: 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능들을 제공
    특히 순열과 조합 라이브러리는 코딩테스트에서 자주 사용됨(모든 경우의 수를 고려해야하는 경우 효과적)
    완전탐색유형에서 소스코드 간결하게 도와주는 경우 많음
-heapq : 힙 자료구조를 제공
    일반적으로 우선순위 큐 기능을 구현하기 위해서 사용
    다익스트라같은 최단경로 알고리즘에서 사용
-bisect : 이진탐색 기능을 제공
    기본적인 형태의 이진탬색기능이 필요할때 효과적
-collections : 덱(deque), 카운터(Counter) 등 유용한 자료구조를 포함
-math : 필수적인 수학적 기능들 제공
    팩토리얼, 제곱근, 최대공약수, 삼각함수 관련 함수부터 파이와 같은 상수를 포함
'''

#sum()
result = sum([1,2,3,4,5])
print(result)
#min() max()
min_result = min(6,3,2,6)
max_result = max(4,2,7,2)
print(min_result, max_result)
#eval() 문자열 수식을 계산해준다
result = eval("(3+5)*7")
print(result)

#sorted()
result = sorted([9,1,8,5,4])
reverse_result = sorted(result, reverse=True)
print(result)
print(reverse_result)

#sorted() with key (정렬기준 명시)
array = [('홍길동', 50), ('이순신', 32), ('김유신', 74)]
result = sorted(array, key=lambda x:x[1], reverse=True)
print(result)

'''
순열과 조합 
- 모든 경우의 수를 고려해야 할 때 어떤 라이브버리를 효과적으로 사용할 수 있을까요?
순열 : 서로다른 n개에서 서로다른 r개를 선택해서 일렬로 내열하는 것
    {'A', 'B', 'C'} 에서 세개를 선택해서 나열하는 경우 : 'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'
조합 : 서로다른 n개에서 순서상관없이 서로다른 r개를 선택하는 것
    {'A', 'B', 'C'} 에서 순서를 고려하지 않고 두개를 뽑는경우 : 'AB', 'BC', 'AC'
    
순열의 수 : nPr = n*(n-1)*(n-2)* ... * (n-r+1)
조합의 수 : nCr =  (n*(n-1)*(n-2)* ... * (n-r+1))/r!
'''
# 순열
from itertools import permutations
data = ['A','B','C'] #데이터 준비
result = list(permutations(data,3)) #모든 순열 구하기
print(result)

# 조합
from itertools import combinations
data = ['A','B','C'] #데이터 준비
result = list(combinations(data,2)) #2개를 뽑는 모든 조합 구하기
print(result)

# 중복순열과 중복조합
from itertools import product
data = ['A','B','C'] #데이터 준비
result = list(product(data, repeat=2)) #2개를 뽑는 모든 순열 구하기 (중복허용)
print(result)

from itertools import combinations_with_replacement
data = ['A','B','C'] #데이터 준비
result = list(combinations_with_replacement(data,2)) #2개를 뽑는 모든 조합구하기 (중복혀용)
print(result)

'''
Counter : 등장횟수를 세는 기능
리스트와 같은 반복가능한 객체가 주어졌을 때 내부의 원소가 몇 번 씩 등장했는지를 알려준다.
'''
from collections import Counter
counter = Counter(['red','blue','red','green','blue','blue'])
print(counter['blue']) # 'blue'가 등장한 횟수 출력
print(counter['green']) # 'green'이 등장한 횟수 출력
print(dict(counter)) # 사전 자료형으로 반환

# 최대공약수와 최소공배수
import math
# 최소공배수를 LCM을 구하는 함수 -> 공통된 배수 중 가장 작은것
def lcm(a,b):
    return a*b // math.gcd(a,b)

a = 21
b = 14

print(math.gcd(21, 14)) #최대 공약수GCD를 계산
print(lcm(21,14)) #최소 공배수계산 LCM