from typing import List
from queue import Queue


class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        visited = [False] * V
        bfs_result = []
        queue = Queue()
        queue.put(0)
        visited[0] = True

        while not queue.empty():
            node = queue.get()
            bfs_result.append(node)
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    queue.put(neighbor)
                    visited[neighbor] = True

        return bfs_result


if __name__ == '__main__':
    T = int(input("Enter the number of test cases: "))
    for i in range(T):
        V, E = map(int, input("Enter the number of vertices and edges: ").split())
        adj = [[] for i in range(V)]
        print("Enter the edges:")
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
        ob = Solution()
        ans = ob.bfsOfGraph(V, adj)
        print("BFS Traversal:", end=" ")
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()
