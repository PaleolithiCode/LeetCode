'''
Runtime: 122 ms, faster than 37.37% of Python3 online submissions for Dungeon Game.
Memory Usage: 15 MB, less than 86.26% of Python3 online submissions for Dungeon Game.
'''
import math
def calculateMinimumHP(dungeon: list) -> int:
    '''
    dp[i][j] denote the minimum amount of HP we need before jumping into the cell
    '''
    m, n = len(dungeon), len(dungeon[0])
    dp = [[math.inf for _ in range(n + 1)] for __ in range(m + 1)]
    dp[m][n - 1] = 1
    dp[m - 1][n] = 1

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j], 1)
    
    return dp[0][0]

dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
print(calculateMinimumHP(dungeon))