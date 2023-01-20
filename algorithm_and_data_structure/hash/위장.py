from functools import reduce

def solution(clothes):
    clothesDict = {}
    for name, category in clothes:
        clothesDict[category] = clothesDict.get(category, 1) + 1 # 카테고리 별 안 입는 경우 포함한 총 경우의 수

    return reduce(lambda x, y: x * y, clothesDict.values()) - 1

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
# clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes))