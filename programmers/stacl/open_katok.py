def solution(record):
    user_map = dict()
    for r in record:
        li = r.split(' ')
        if li[0] == 'Enter' or li[0] == 'Change':
            user_map[li[1]] = li[2]

    answer = []
    for r in record:
        li = r.split(' ')
        if li[0] == 'Enter':
            answer.append('%s님이 들어왔습니다.' % user_map[li[1]])
        elif li[0] == 'Leave':
            answer.append('%s님이 나갔습니다.' % user_map[li[1]])
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))