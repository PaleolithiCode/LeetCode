'''
Runtime: 170 ms, faster than 35.26% of Python3 online submissions for Course Schedule II.
Memory Usage: 17.1 MB, less than 32.48% of Python3 online submissions for Course Schedule II.
'''
import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list) -> list:
        graph = collections.defaultdict(list)
        visited = [0 for _ in range(numCourses)]
        ans = []
        def dfs(x):
            if visited[x] == 1:
                return True
            if visited[x] == -1:
                return False
            visited[x] = -1
            
            for y in graph[x]:
                if not dfs(y):
                    return False
                
            visited[x] = 1
            ans.append(x)
            return True
            
        for x, y in prerequisites:
            graph[x].append(y)
        
        for x in range(numCourses):
            if not dfs(x):
                return []
        return ans