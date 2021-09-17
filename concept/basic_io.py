'''
모든 프로그램은 적절한 입출력 양식을 가지고 있음
프로그램 동작의 첫 번째 단계는 데이터를 입력받거나 생성하는 것
예시) 학생의 성적데이터가 주어지고, 이를 내림차순으로 정렬한 결과를 출력하는 프로그램

자주 사용되는 표준 입출력의 방법
input() 함수는 한줄의 문자열을 입력받는 함수
map() 함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할때 사용
# 공백을 기준으로 구분된 데이터를 입력받을 때
# 입력받은다음 공백기준으로 분리를하고 정수형으로바꿔준다음에 list형으로 바꿔줌
a = list(map(int, input().split()))
print(a)

# 공백을 기준으로 구분된 데이터의 개수가 많지 않다면 다음과 같이 단순하게 사용함
a, b, c = map(int, input().split())
print(a)
print(b)
print(c)

# 데이터의 개수 입력
n = int(input())
# 각 데이터를 공백을 기준으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)
'''
import sys

'''
사용자로부터 입력을 빠르게 받아야 하는 경우
sys라이브러리에 정의되어 있는 sys.stdin.readline()메서드를 이용
단 입력후 엔터가 줄바꿈 기호로 입력되므로 rstrip() 메서드와 함께 사용

실제로 어떤문제의 경우 입력을 받는 경우가 많아서 시간이 많이 소요되는경우 이를 사용할수있다
이진탐색, 정렬 혹은 그래프 관련 문제에서 자주 사용하는 테크닉
# 문자열 입력받기
data = sys.stdin.readline().rstrip()
print(data)
'''

'''
파이썬에서 기본출력은 print() 함수를 사용
각 변수를 , 를 이용하여 띄어쓰기로 구분하여 출력 가능
print()는 기본적으로 출력 이후에 줄바꿈을 수행
원치 않는경우 'end'(기본적으로 end속성은 줄바꿈으로 설정되어있음)속성을 이용
'''
a = 1
b = 2
print(a, b)
print(7, end=" ")
print(8, end=" ")

answer = 7
print(" 정답은 " + str(answer) + "입니다.")

'''
f-string : 문자열 앞에 접두사 'f'를 붙여서 사용한다
중괄호 안에 변수명을 기입하여 간단히 문자열과 정수를 함께 넣을 수 있다
'''
print(f"정답은 {answer}입니다.")
