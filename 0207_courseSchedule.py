'''
Runtime: 154 ms, faster than 44.01% of Python3 online submissions for Course Schedule.
Memory Usage: 17.3 MB, less than 23.52% of Python3 online submissions for Course Schedule.
'''
import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list) -> bool:           
        graph = collections.defaultdict(list)
        visited = [0 for _ in range(numCourses)]
        
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
            return True
            
        for x, y in prerequisites:
            graph[x].append(y)
        
        for x in range(numCourses):
            if not dfs(x):
                return False
        return True
        