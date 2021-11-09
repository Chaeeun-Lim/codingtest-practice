import collections

def solution1(participant, completion):
    for c in completion:
        if c in participant:
            participant.remove(c)
    return participant

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

def solution4(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

def solu(particitpant, completion):
    result = dict()
    temp = 0
    for p in particitpant:
        result[hash(p)] = p
        temp += hash(p)
    for c in completion:
        temp -= hash(c)
    return result[temp]

def solution3(participant, completion):
    ret = dict()
    for c in completion:
        if c in ret:
            ret[c] += 1
        else:
            ret[c] = 1

    for p in participant:
        if p in ret:
            if ret[p] > 0:
                ret[p] -= 1
            else:
                return p
        else:
            return p


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

print(solu(participant, completion))