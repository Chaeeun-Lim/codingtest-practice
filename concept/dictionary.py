'''
사전 자료형 : 키와 값의 쌍을 데이터로 가지는 자료형
리스트나 튜플이 값을 순차적으로 저장하는 것과는 대비됨
원하는 '변경 불가능한 자료형'을 키로 사용
파이썬의 사전 자료형은 해시테이블을 이용하므로 데이터의 조회 및 수정에 있어서 O(1)시간이 소요

키 데이터만 뽑아서 리스트 형태로 뽑기 keys()
값 데이터만 뽑아서 리스트 형태로 뽑기 values()
'''

data = dict()
data['사과'] = "Apple"
data['바나나'] = "Banana"
data['코코넛'] = "Coconut"

print(data)

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다")

key_list = data.keys()
value_list = data.values()
print(key_list)
print(value_list)

for key in key_list:
    print(data[key])

for i in data:
    print(i)

v = [[1, 4], [3, 4], [3, 10]]
answer = []
x = dict()
y = dict()
for i in v:
    nx, ny = str(i[0]), str(i[1])
    if nx in x:
        x[nx] += 1
    else:
        x[nx] = 1
    if ny in y:
        y[ny] += 1
    else:
        y[ny] = 1
for i in x.keys():
    if x[i] == 1:
        answer.append(int(i))
for i in y.keys():
    if y[i] == 1:
        answer.append(int(i))

print(answer)