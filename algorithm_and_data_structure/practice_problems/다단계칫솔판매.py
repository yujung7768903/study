# 문제 풀이 시간: 52s
# 딕셔너리를 만들어서 추천인을 찾지 않고, index를 사용하면 시간이 더 오래걸림

def solution(enrollList, referralList, sellerList, amountList):
    enrollAmountDict = {key: 0 for key in enrollList + ["-"]}
    referralDict = {member: referral for member, referral in zip(enrollList, referralList)}
    print(referralDict)
    for seller, amount in zip(sellerList, amountList):
        divideMoney(seller, amount * 100, referralDict, enrollAmountDict)
    print(enrollAmountDict)

    return [enrollAmountDict[value] for value in enrollList]

def divideMoney(member, money,referralDict, enrollAmountDict):
    print(f"member: {member}, money: {money}")
    takeMoney = money
    if money >= 10 and member != "-":
        giveMoney = takeMoney // 10
        takeMoney -= giveMoney
        divideMoney(referralDict[member], giveMoney, referralDict, enrollAmountDict)
    enrollAmountDict[member] += takeMoney

# 1원 미만인 경우에는 이득을 분배하지 않음
# enroll: 판매원의 이름을 담은 배열
# referral: 참여시킨 다른 판매원의 이름을 담은 배열 (추천 없이 참여:"-")
# seller: 판매원 이름 나열
# amount: 판매 수량
# 칫솔 한개당 100원

# Test
enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
print(solution(enroll, referral, seller, amount))
# 정답 = [360, 958, 108, 0, 450, 18, 180, 1080]