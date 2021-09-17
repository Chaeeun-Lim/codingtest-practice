'''
함수
특정한 작업을 하나의 단위로 묶어놓은 것을 의미
불필요한 소스코드의 반복을 줄일 수 있다.

내장함수 : 파이썬이 기본적으로 제공하는 함수
사용자 정의 함수 : 개발자가 직접 정의하여 사용할 수 있는 함수

매개변수=파라미터 : 함수 내부에서 사용할 변수
반환 값 : 함수에서 처리 된 결과를 반환

def 함수명(매개변수):
    실행할 소스코드
    return 반환값

파라미터의 변수를 직접 지정할 수도 있는데 이경우 매개변수의 순서가 달라도 상관없다
def add(a,b):
    return a+b

add(b=3, a=7) -> 상관없음

global : global키워드로 변수를 지정하면 해당 함수에서는 지역변수를 만들지 않고도 함수 바깥에 선언된 변수를 바로 참조가 가능하다

파이썬에서는 함수는 여러개의 반환값을 가질 수있다
'''
def add(a,b):
    return a+b
# 여기서 3,7은 이자
print(add(3,7))

def printAdd(a,b):
    print("더한 결과는", a+b,"입니다")

printAdd(2,4)

a = 0

def fun():
    global a
    a += 1

for i in range(10):
    fun()

print(a)

array = [1,2,3,4,5]
def fun():
    global array
    array = [3,4,5]
    array.append(6)
    print(array)

fun()
print(array)

def operator(a, b):
    add_var = a+b
    substract_var = a-b
    multiply_var = a*b
    divide_var = a/b
    return add_var, substract_var, multiply_var, divide_var

a,b,c,d = operator(7,2)
print(a,b,c,d)