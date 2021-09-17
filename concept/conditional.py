'''
조건문: 프로그램의 흐름을 제어하는 문법
들여쓰기: 파이썬에서는 코드의 블록을 들여쓰기로 지정합니다.
비교연산자: 특정한 두 값을 비교할 때 이용 == != > < >= <=
논리연산자: 논리값(T / F) 사이의 연산을 수행할 때 사용 X and Y, X or Y, not X (X가 거짓일 때 참)

다수의 데이터를 담는 자료형을 위해 in과 not in연산자 제공
리스트 튜플 문자열 사전 모두에서 사용가능
x in list : 리스트안에 x가 들어 있으면 참
x not in 문자열 : 문자열 안에 x가 없으면 참

pass 키워드
- 아무것도 처리하고 싶지 않을 때 pass 키워드를 사용
ex) 디버깅 과정엣서 일단 조건문의 형태만 만들어 놓고 조건문을 처리하는 부분을 비워 놓고 싶은경우
score = 85

if score >= 70:
    pass # 나중에 작성할 소스코드
else:
    print('성적이 70점 미만입니다.')
    print("조금 더 분발하세요.")

print('프로그램을 종료합니다.')

파이썬 조건문 내에서의 부등식 : 다른 프로그래밍 언어와 다르게 파이썬으느 조건문 안에서 수학의 부등식 그대로 사용가능
x > 0 and x < 20 과 0 < x < 20 은 같은 결과를 반환

'''
score = 85

if score >= 70:
    print("성적이 70점 이상입니다.")
    if score >= 90:
        print('우수한 성적입니다.')
else:
    print('성적이 70점 미만입니다.')
    print("조금 더 분발하세요.")

print('프로그램을 종료합니다.')

a = -7
if a>=0:
    print("a >= 0")
elif a>=-10:
    print("0 > a >= -10")
else:
    print("-10 > a")

score = 85

if score >= 90:
    print("학점이 A 입니다")
elif score >= 80:
    print("학점이 B 입니다")
elif score >= 70:
    print("학점이 C 입니다")
else:
    print("학점이 F 입니다")

# 조건문의 간소회
# 실행될 소스코드가 한줄인경우 궅이 줄바꿈을 하지 않고 간략하게 표현이 가능
score = 85
if score >= 80: result = "Success"
else: result="Fail"
print(result)

#조건부 표현식은 if~else문을 한줄에 작성할수 있도록해줌
score = 65
result = "Success" if score >= 80 else "Fail"
print(result)

x = 15
if x > 0 and x < 20:
    print("x는 0이상 20미만의 수 입니다.")

if 0 < x < 20:
    print("x는 0이상 20미만의 수 입니다.")