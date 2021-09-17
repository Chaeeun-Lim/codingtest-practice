'''
반복문 while
'''
i = 0
result = 0
while i<10:
    if i%2 == 1:
        result += i
    i +=1
print(result,i)

# for문에서 연속적인 값을 차례로 순회할때는 range()를 사용
# 이때 range(시작값, 끝값+1) 형태로 사용, 인자를 하나만 넣으면 자동으로 시작값은 0
result = 0
for i in range(1,31):
    result += i

print(result)

sum = 0
for i in range(1,10):
    if i%2 == 0:
        continue
    sum += i
print(sum)

#반복문을 즉시 탈출하고자 할 때 break사용
i=1
while True:
    if i == 5:
        break
    i += 1
print(i)

# 점수가 80점만 넘으면 합격
scores = [83, 65, 77, 90, 92]

for i in range(len(scores)):
    if scores[i] >= 80:
        print(i+1,"번 학생은 합격입니다.")

# 특정번호의 학생은 제외
cheating_student_list = {2,4}

for i in range(len(scores)):
    if i+1 in cheating_student_list:
        continue
    if scores[i] >= 80:
        print(i+1,"번 학생은 합격입니다")

# 구구단 출력해보기
for i in range(1,10):
    for j in range(1, 10):
        print(i,"X",j,"=",i*j)
    print()