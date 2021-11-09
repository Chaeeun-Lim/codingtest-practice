def solution1(phone_book):
    phone_book.sort()
    comp = phone_book[0]
    for i in range(1, len(phone_book)):
        if phone_book[i].startswith(comp):
            return False
        else:
            comp = phone_book[i]
    return True

def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer

def solution3(phone_book):
    answer = True
    result = {}
    for phone_number in phone_book:
        result[phone_number] = 1
    for phone_number in phone_book:
        temp = ''
        for number in phone_number:
            temp += number
            if temp in result and temp != phone_number:
                answer = False
    return answer


#phone_book = ["119", "97674223","1195524421"]
#phone_book = ["123","456","789"]
phone_book = ["12","123","1235","567","88"]
print(solution(phone_book))