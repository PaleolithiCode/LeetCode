import collections, sys


'''
https://leetcode.com/problems/minimum-number-of-refueling-stops/discuss/613853/Python-5-solutions-gradually-optimizing-from-Naive-DFS-to-O(n)-space-DP
For a problem with no clear DP idea, always start with DFS/BFS solution
A DFS solution with return values instead of a self.rst global value can be easier to be rewrotten with memorization
For knapsack problems, when the value amount is too large or there is a limitation on value to reach, consider to build a dp[i][j] with former i bags, pick j of them instead of the regular way dp[i][j] with former i bags, value j can be constructed or not.
Original 0-1 knapsack: maximum value given # of bags limitation: dp[i][j] = bool, in former i bags, j VALUE can be constructed or not.
Reversed 0-1 knapsack: minimum # of bags used to reach a given value dp[i][j] = value, in former i bags, j # OF BAGS being picked, what is the maximum value.
In a space-uncompressed dp solution, inner loop's left to right / right to left updating direction doesn't matter when dp[i][j] not related to dp[i][j +/-1] , but the compressed 1-d dp's updating direction matters a lot, because last row's results might be replaced by current row's ones. Check here for anthoer exapmle where updating direction needs to be modified because of space optimization.
'''
def minRefuelStops(target: int, startFuel: int, stations: list) -> int:
    full_target = target
    
    def dfs(curFuel, start, target):
        if curFuel >= target:
            return 0
        rst = sys.maxsize
        for i in range(start, len(stations)):
            dis, fuel = stations[i][0] - (full_target - target), stations[i][1]
            if curFuel - dis >= 0:
                rst = min(rst, dfs(curFuel - dis + fuel, i + 1, target - dis) + 1)
        return rst
    stops = dfs(startFuel, 0, target)
    return stops if stops != sys.maxsize else -1
        
target, startFuel, stations =100, 50, [[25,25],[50,50]] # 1
# target, startFuel, stations =1, 1, [] # 0
# target, startFuel, stations =100, 10, [[10,60],[20,30],[30,30],[60,40]] # 2
# target, startFuel, stations =100, 1, [[10,100]] # -1
print(minRefuelStops(target, startFuel, stations))