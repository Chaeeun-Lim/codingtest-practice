'''
이진탐색 알고리즘:  정렬되어 있는 리스트에서 탐색범위를 절반씩 좁혀가면서 데이터를 탐색하는 방법 O(logN)
    시작점, 끝점, 중간점을 이용하여 탐색범위를 설정
'''
# 재귀적 구현
def binary_search_self(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 적을 경우 왼쪽확인
    if array[mid] > target:
        return binary_search_self(array, target, start, mid-1)
    # 반대
    else:
        return binary_search_self(array, target, mid+1, end)

# 반복문 구현
def binary_search_for(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽확인
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid + 1
    return None

n, target = 10, 9
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
result = binary_search_for(array, target, 0, n-1)
if not result:
    print("원소가 존재하지 않습니다.")
else:
    print("원소가 인덱스", result, "에 존재합니다.")

# 파이썬 이진탐색 라이브러리
from bisect import bisect_left, bisect_right

#bisect_left(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
#bisect_right(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환
a = [1, 2, 4, 4, 8]
x = 4

print(bisect_right(a, x))
print(bisect_left(a, x))
# 라이브러리 이용해서 특정범위에 속하는 데이터의 개수 구하기
# 값이 [left_value, right_value] 인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    l_idx = bisect_left(a, left_value)
    r_idx = bisect_right(a, right_value)
    return r_idx - l_idx

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(a, 4, 4))
print(count_by_range(a, -1, 3))

# 파메트릭서치 : 최적화문제를 결정문제 (예.아니오)로 바꾸어 해결하는 기법
# 예) 특정조건을 만족하는 가장 알맞은 값을 빠르게 찾는 문제
# 일반적으로 코딩테스트에서 파메트릭서치는 이진탐색을 이용하여 해결가능

# 문제 : 떡볶이 떡 만들기
'''
아이디어 : 적절한 높이를 찾을 떄까지 이진탐색을 수행하여 높이 H를 반복해서 조정
'현재 이 높이로 자르면 조건만족?' 를 확인한 후에 조건 만족 여부에 따라 탐색범위를 좁혀서 해결
절단기의 높이는 0부터 10억까지의 정수, 이렇게 큰 탐색범위를 보면 가장먼저 이진탐색을 떠올려야 한다

중간점의 값은 시간이 지날수록 '최적화된 값'이 되기 떄문에 과정을 반복하면서 얻을 수 있는 떡의 길이합이
필요한 떡의 길이보다 크거나 값을 때마다 중간점의 값을 기록하면 된다.
'''
n, m = 4, 6
rc = [19, 15, 10, 17]
start = 0
end = max(rc)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for r in rc:
        # 잘랐을 떄 떡의 양 갱신
        if r > mid:
            total += r - mid
    # 떡 양 부족한 경우 더 많이 자르기
    if total < m:
        end = mid - 1
    # 충분할 경우 더 많이 자르기
    else:
        result = mid    # 최대한 덜 잘랐을 떄가 정답이므로 여기서 result에 기록
        start = mid + 1

print(result)

# 정렬된 배열에서 특정수의 개수 구하기