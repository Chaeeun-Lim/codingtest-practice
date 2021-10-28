'''
리스트 자료형 : 여러개의 데이터를 연속적으로 담아 처리하기 위해 사용되는 자료형
배열과 유사한 기능 및 연결잇스트와 유사한 기능 지원
[]안에 원소를 넣어서 초기화 한다

인덱싱
인덱슷 값을 입력하여 리스트의 특정한 원소에 접근하는 것을 인덱싱이라고 합니다
파이썬의 인텍스 값은 양과 음의 정수 모두 사용가능
음의 정수를 넣으면 원소를 거꾸로 탐색하게 됩니다.

슬라이싱
리스트엣서 연속적인 위치를 갖는 원소들을 가져와야할 때 사용
대괄호안에 콜론을 넣어서 시작인덱스와 끝 인덱스 설정
**끝 인덱스는 실제 인덱스보다 1크게 설정**

리스트 컴프리핸션 : 2차원 리스트를 초기화할 때 효과적으로 사용될 수 있다.
특히 N*M크기의 2차원 리스트를 한번에 초기화해야할때 매우 유용
# 좋은 예시
array3 = [[0]*m for _ in range(n)]
'''
a = [1,2,3,4,5,6,7,8,9]
print(a)
print(a[-1])

#두번째 원소부터 네번째 원소까지
print(a[1:4])

n = 10
a = [0]*n
print(a)


array = [i for i in range(10)]
print(array)

# 반복문 뿐만 아니라 조건문도 포함가능
a=[i for i in range(50) if i%2==1]
print(a)

array = [i*i for i in range(10)]
print(array)

# 코드1 : 리스트 컴프리헨션
array1 = [i for i in range(10) if i%2==1]
print(array1)

# 코드2 : 일반적인 코드
array2 = []
for i in range(10):
    if i%2 == 1:
        array2.append(i)
print(array2)


# N X M 크기의 2차원 리스트 초기화
n = 4
m = 3
array3 = [[0]*m for _ in range(n)]
print(array3)
array3[1][1] = 5
print(array3)

# 잘못된 방법
# [0]*m이 내부적으로 전부 같은 객체로 인식
array4 = [[0]*m]*n
print(array4)
array4[1][1] = 5
print(array4)

'''
파이썬에서는 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 언더바_를 자주사용
'''
#코드1 1부터 9까지의 자연수 더하기
summary = 0
for i in range(1,10):
    summary += i
print(summary)

# 코드2: Hello World를 5번 출력 (내부적으로 변수가 반복에 사용되지 않을음 알려줌
for _ in range(5):
    print("Hello World")

# 리스트에서 특정값을 가지는 원소를 모두제거하기
a = [1,2,3,4,5,5,5]
remove_set = {3,5} #집합자료형

result = [i for i in a if i not in remove_set]
print(result)