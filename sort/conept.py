# 정렬 알고리즘
# 1. 선택 정렬 : 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해서 맨 앞의 데이터와 바꾸는 것
# 시간 복잡도 = O(n^2)
a = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(a)):
    min_idx = i
    for j in range(i+1, len(a)):
        if a[min_idx] > a[j]:
            min_idx = j
    a[i], a[min_idx] = a[min_idx], a[i]

print(a)
# 2. 삽입정렬 : 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입, 선택정렬에 비해 구현난이도 높지만 일반적으로 더 효율적으로 동작
#  시간복잡도 : O(n^2) 최선의 경우 O(n) : 현재 데이터가 거의 정렬되어있다면 매우빠르게 동작
a = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(a)):
    for j in range(i, 0, -1):
        if a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
        else:
            break
print(a)
# 3. 퀵정렬 : 기준데이터를 설정하고 그 기준보다 큰 데이터와 작은데이터의 위치를 바꿈
# 가장 기본적인 큌정렬은 첫번째데이터를 기중 데이터로 설정
# 왜 빠르게 동작할까? : 이상적인 경우 분할이 절반씩 일어난다면 전체연산 횟수로 O(nlogn)기대할 수 있다 (평균) but 최악은 O(n^2)
a = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:    # 원소가 한개인 경우
        return
    pivot = start       # 피벗은 첫번째 원소
    left = start+1
    right = end
    while left <= right:    # 엇갈릴떄까지 수행
        # 피벗보다 큰 데이터를 찾을 떄 까지 반복
        while left <= end and a[left] <= a[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 떄 까지 반복
        while right > start and a[right] >= a[pivot]:
            right -= 1
        if left > right:        # 엇갈린 경우에는 작은데이터와 피벗을 교체
            a[right], a[pivot] = a[pivot], a[right]
        else:                   # 엇갈리지 않았다면 작은데이터와 큰 데이터를 교체
            a[left], a[right] = a[right], a[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(a, 0, len(a)-1)
print(a)
# 간결한 퀵정렬
a = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort2(array):
    if len(array) <= 1:
        return array
    pivot = array[0]    # 피벗은 첫번쨰원소
    tail = array[1:]    # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]     # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]     # 분할된 오른쪽 부분

    # 분할 이후 왼쪽과 오른쪽 부분에서 각각 정렬을 수행하고 전체리스트 반환
    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)

print(quick_sort2(a))

# 4. 계수정렬: 특정조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작함, 계수정렬은 데이터의 크기범위가 제한되어있어 정수형태로
#       표현할 수 있을 때 사용
# 시간복잡도 : 데이터의 개수가 n 데이터(양수) 중 최대값이 k일떄 최악의 경우에도 O(K+K)를 보장
# 그 데이터와 같은게 몇번 들어가 있는지 인덱스에 저장하고, 인덱스 수만큼 그 값 출력하기

# 문제: 두 배열의 원소 교체

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))