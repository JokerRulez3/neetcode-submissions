class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = self.buildGraph(n, edges)

        visited = set()
        count = 0

        for node in range(n):
            if self.explore(graph, node, visited) == True:
                count += 1
        
        return count
    
    def explore(self, graph, node, visited):
        if node in visited:
            return False
        visited.add(node)

        for neighbour in graph[node]:
            self.explore(graph, neighbour, visited)
        
        return True

    def buildGraph(self, n, edges: List[List[int]]) -> Dict:
        graph = {i: [] for i in range(n)}

        for edge in edges:
            a, b = edge
            graph[a].append(b)
            graph[b].append(a)
        
        return graph