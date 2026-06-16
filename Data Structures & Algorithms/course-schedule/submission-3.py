class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency = {}
        for i in prerequisites:
            if i[0] in adjacency:
                adjacency[i[0]] += [i[1]]
            else:
                adjacency[i[0]] = [i[1]]
        visited = set()
        def dfs(course: int):
            if course in visited:
                return False
            if adjacency.get(course, []) == []:
                return True
            visited.add(course)
            y = len(adjacency[course])
            for i in range(y):
                if not dfs(adjacency[course][i]):
                    return False
            visited.remove(course)
            adjacency[course] = []
            return True
                    

        for i in range(numCourses):
            if not dfs(i):
                return False


        return True