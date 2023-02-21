# 문제 풀이 시간: 7분 15초

def groupAnagrams(strs):
        anagramDict = {}
        for str in strs:
            key = ''.join(sorted(str))
            anagramDict[key] = anagramDict.get(key, []) + [str]
        return anagramDict.values()

strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

print(groupAnagrams(strs))