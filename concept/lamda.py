'''
람다표현식을 이용하면 함수를 간단하게 잓성이 가능
특정한 기능을 수행하는 함수를 한줄에 작성할 수 있다. 이름없는 함수라고도 함

람다표현식이 유용한 경우: 어떠한 함수 자체를 입력으로 받는 또다른 함수가 존재하는 경우
함수의 기능이 간단하거나 한번 사용하고 말경우
'''
def add(a,b):
    return a+b

#일반적인 add() 메서드 사용
print(add(3,7))

# 람다표햔식으로 구현한 add()메소드
print((lambda a,b: a+b)(3,7))

# 람다 표현식 예제 : 내장함수에서 자주 사용되는 람다합수
array = [('홍길동', 50), ('이순신', 32), ('김유신', 74)]

def my_key(x):
    return x[1]



print(sorted(array, key=my_key))
print(sorted(array, key=lambda x:x[1]))

# 람다 표현식 예시 : 여러개의 리스트에 적용
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

result = map(lambda a,b:a+b, list1, list2)
list3 = list(result)
print(list3)

print((lambda a,b:a+b)(list1[1],list2[1]))
