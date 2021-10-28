import math

# 하나의 소수의 판별
def prime_number(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

# 다수의 소수판별 : 특정한 수의 범위 안에 존재하는 모든 소수 찾기
def cnt_prime_number_in_range(n):
    # 처음엔 모든수가 소수라고 초기화
    array = [True for i in range(n+1)]
    for i in range(2, int(math.sqrt(n))+1):
        if array[i]:
            j = 2
            while i*j <= n:
                array[i*j] = False
                j += 1
    result = []
    for i in range(2, n+1):
        if array[i]:
            result.append(i)
    return result

# 투 포인터 알고리즘 : 리스트에 순차적으로 접근해야 할 때 두개의 점의 위치를 기록하면서 처리하는 알고리즘
# 흔히 2,3,4,5,6,7번 학생을 지목해야 할 때 간단히 '2번부터 7번까지의 학생'이라고 부름
# 리스트에 담긴 데이터에 순차적으로 접근해야 할 때는 시작점과 끝점 2개의 점으로 접근할 데이터의 범위 표현 가능

# 특정한 합을 가지는 부분연속 수열 찾기
# n개의 자연수로 구성된 수열 중 합이 m인 부분연속 수열의 개수를 구할떄 [1,2,3,4,5] 5
def two_pointer(numbers, m):
    n = len(numbers)
    cnt = 0
    interval_sum = 0
    end = 0
    for i in range(n):
        while interval_sum < m and end < n:
            interval_sum += numbers[end]
            end += 1
        if interval_sum == m:
            cnt +=1
        interval_sum -= numbers[i]
    return cnt

# 구간합 : 연속적으로 나열된 n개의 수가 있을 떄 특정 구간의 모든 수를 합한 값을 계산하는 문제
# n개의 정수로 구성된 수열과 m개의 쿼리정보가 주어짐 (각 쿼리는 왼 오 로 구성됨) 각 쿼리구간에 포함된 데이터들의 합을 출력
# 접두사합을 활용 : 배열의 맨 앞부터 특정 위치까지의 합을 미리 구해놓는거
def range_sum(num_list, queries):
    sum_list = [0]
    val = 0
    for i in num_list:
        val += i
        sum_list.append(val)
    ans_list = []
    for query in queries:
        l, r = query
        ans_list.append(sum_list[r]-sum_list[l-1])
    return ans_list

print(prime_number(7))
print(cnt_prime_number_in_range(26))
print(two_pointer([1,2,3,2,5], 5))
print(range_sum([10,20,30,40,50], [(3,4)]))