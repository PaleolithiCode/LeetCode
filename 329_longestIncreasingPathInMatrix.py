'''
Runtime: 381 ms, faster than 97.01% of Python3 online submissions for Longest Increasing Path in a Matrix.
Memory Usage: 14.7 MB, less than 96.70% of Python3 online submissions for Longest Increasing Path in a Matrix.
'''
def longestIncreasingPath(matrix: list) -> int:
    M = len(matrix)
    N = len(matrix[0])
    dp_solution = [[0 for _ in range(N)] for __ in range(M)]

    def dfs(i, j):
        if not dp_solution[i][j]:
            right = dfs(i + 1, j) if i < M - 1 and matrix[i][j] > matrix[i + 1][j] else 0
            left = dfs(i - 1, j) if i - 1 >= 0 and matrix[i][j] > matrix[i - 1][j] else 0
            top = dfs(i, j - 1) if j - 1 >= 0 and matrix[i][j] > matrix[i][j - 1] else 0
            down = dfs(i, j + 1) if j < N - 1 and matrix[i][j] > matrix[i][j + 1] else 0
            dp_solution[i][j] =  1 + max(right, left, top, down)
        return dp_solution[i][j]

    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0
    
    return max(dfs(x, y) for x in range(M) for y in range(N))

matrix = [[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]]
print(longestIncreasingPath(matrix))