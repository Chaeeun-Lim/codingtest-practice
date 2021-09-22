# 멀티탭 구멍 수와 전기사용 수 입력받기
N, K = map(int, input().split())
arr = list(map(int, input().split()))
# 멀티탭
plugin = list()
# 플러그 뺀 수
cnt = 0

for i in range(K):
    # 멀티탭에 이미 내가 꽂혀 있는 경우
    if arr[i] in plugin:
        continue
    # 멀티탭에 자리가 있는 경우
    if len(plugin) < N:
        plugin.append(arr[i])
        continue
    # 멀티탭에 자리가 없는 경우
    # 멀티탭에 내가 안꽂혀 있는 경우
    # 뽑을 멀티탭 인덱스
    out = 0
    # 뽑을 것이 tool에 있는 위치
    out_idx = 0
    # 한번 뽑아야함
    cnt += 1
    for j in range(N):
        if plugin[j] not in arr[i+1:]:
            out = j
            break
        idx = arr[i+1:].index(plugin[j])
        if idx > out_idx:
            out = j
            out_idx = idx
    plugin[out] = arr[i]

print(cnt)


