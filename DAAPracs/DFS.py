class Solution:

    # Recursive function to perform DFS traversal
    def dfs(self, node, visited, adj, result):
        visited[node] = True
        result.append(node)
        for neighbor in adj[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, adj, result)

    # Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        visited = [False] * (V + 1)
        result = []
        self.dfs(0, visited, adj, result)
        return result


if __name__ == '__main__':
    T = int(input("Enter the number of test cases: "))
    while T > 0:
        V, E = map(int, input("Enter the number of vertices and edges: ").split())
        adj = [[] for _ in range(V + 1)]
        print("Enter the edges:")
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob = Solution()
        ans = ob.dfsOfGraph(V, adj)
        print("DFS Traversal:", end=" ")
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()
        T -= 1
