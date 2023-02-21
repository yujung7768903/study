def topKFrequent(nums, k):
        numsDict = {}
        for num in nums:
            numsDict[num] = numsDict.get(num, 0) + 1

        sortKeyList = sorted(numsDict.keys(), key=lambda key: numsDict[key], reverse=True)
        return sortKeyList[:k]

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
nums = [1,1,1,2,2,3]
print(topKFrequent(nums, 2))