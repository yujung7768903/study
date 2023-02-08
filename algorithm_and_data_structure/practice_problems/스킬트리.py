# 문제 풀이 시간: 15.53s

def solution(skill, skillTrees):
    answer = 0
    for item in skillTrees:
        useSkill = ""
        for itemSkill in item:
            if itemSkill in skill: useSkill += itemSkill
        if useSkill == skill[:len(useSkill)]:
            answer += 1

    return answer

# Test
skillTrees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution("CBD", skillTrees))