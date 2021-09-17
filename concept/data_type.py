#1,000,000,000의 지수 표현 방식 -> 기본적으로 실수형 데이터
import time

a = 1e9
print(int(a))

a = 75.25e1
print(a)

a = 3954e-3
print(a)

a = 0.3 + 0.6
print(a)

if a == 0.9:
    print(True)
else:
    print(False)

# 개발과정에서 실수값을 제대로 비교하지 못해서 원하는 결과를 얻지 못할 수 있다
# 따라서 round() 함수를 이용할 수 있으며 이러한 방식이 권장됨

a = 0.3 + 0.6
print(round(a, 4))

if round(a,4) == 0.9:
    print(True)
else:
    print(False)

# 수 자료형의 연산
# 나누기 연산자 / 를 주의해서 사용해여한다
'''
파이썬에서는 나누기 연산자/ 는 나눠진 결과를 실수형으로 반환
다양한 로직을 설계할때 나머지연산자 %를 이용해야 하는 경우가 많다
파이썬에서 몫을 얻기 위해서 몫연산자 //를 사용한다
이외에도 거듭연산자 **를 비롯해 다양한 연산자 존재
'''
b = 2
print(b**8)

c = 7
d = 3
print(c/d)
print(c//d)
print(c%d)