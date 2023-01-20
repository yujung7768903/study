import re

# ^문자 : 문자로 시작되면 매치
# 문자$: 문자로 끝나면 매치
# pattern을 이용하면, 효율성 테스트에서 시간초과가 남

def solution(phone_book):
    phone_book.sort()
    print(phone_book)
    for index in range(len(phone_book) - 1):
        print(f"{phone_book[index]}로 시작하는 번호")
        if phone_book[index + 1].startswith(phone_book[index]):
            return False
        # pattern = re.compile(f"^{phone_book[index]}")
        # if len(pattern.findall(phone_book[index + 1])) > 0:
        #     return False

    return True

phone_book = ["119", "110", "97674223", "1195524421"]
phone_book = ["11", "1"]
print(solution(phone_book))