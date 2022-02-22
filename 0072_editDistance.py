'''
Runtime: 307 ms, faster than 18.42% of Python3 online submissions for Edit Distance.
Memory Usage: 17.6 MB, less than 71.10% of Python3 online submissions for Edit Distance.
'''
def minDistance(word1: str, word2: str) -> int:
    dp_solution = [[0 for _ in range(len(word1) + 1)] for __ in range(len(word2) + 1)]
    for i in range(len(dp_solution[0])):
        dp_solution[0][i] = i
    for j in range(len(dp_solution)):
        dp_solution[j][0] = j

    for i in range(len(word1)):
        for j in range(len(word2)):
            if word1[i] == word2[j]:
                dp_solution[j + 1][i + 1] = dp_solution[j][i]
            else:
                dp_solution[j + 1][i + 1] = 1 + min(dp_solution[j][i], dp_solution[j + 1][i], dp_solution[j][i + 1])
    
    return dp_solution[-1][-1]

# ans = 3
print(minDistance("horse", "ros"))