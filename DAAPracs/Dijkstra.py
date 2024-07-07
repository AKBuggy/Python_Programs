import heapq

MAX_VALUE = (1 << 32)


class Solution:

    # Function to find the vertex with minimum distance value, from the set
    # of vertices not yet included in shortest path tree.
    def minDistance(self, dist, sptSet, V):

        # initializing minimum value.
        mini = MAX_VALUE
        min_index = 0

        for v in range(V):
            if sptSet[v] == False and dist[v] <= mini:
                mini = dist[v]
                min_index = v

        return min_index

    # Function to find the shortest distance of all the vertices
    # from the source vertex S.
    def dijkstra(self, V, adj, S):

        # creating Adjacency matrix from Adjacency list.
        adj_mat = [[0 for i in range(V)] for i in range(V)]

        for i in range(V):
            for j in range(len(adj[i])):
                adj_mat[i][adj[i][j][0]] = adj[i][j][1]

        # dist[] is output list. dist[i] will hold the
        # shortest distance from source to i.
        dist = [0 for i in range(V)]

        # sptSet[i] will true if vertex i is included in shortest
        # path tree or shortest distance from src to i is finalized.
        sptSet = [False for i in range(V)]

        # initializing all distances as INFINITE.
        for i in range(V):
            dist[i] = MAX_VALUE

        # distance of source vertex from itself is always 0.
        dist[S] = 0

        # iterating over all vertices.
        for count in range(V - 1):

            # picking the minimum distance vertex from the set of vertices
            # not yet processed and marking the picked vertex as processed.
            u = self.minDistance(dist, sptSet, V);
            sptSet[u] = True

            # updating dist[] value of adjacent vertices of the picked vertex.
            for v in range(V):

                # updating dist[v] only if it's not in sptSet, there is an
                # edge from u to v, and total weight of path from source to
                # v through u is smaller than current value of dist[v].
                if sptSet[v] == False and adj_mat[u][v] != 0 and dist[u] != MAX_VALUE and dist[u] + adj_mat[u][v] < \
                        dist[v]:
                    dist[v] = dist[u] + adj_mat[u][v]

        # returning the list.
        return dist


if __name__ == '__main__':
    T = int(input("Enter the number of test cases: "))
    for _ in range(T):
        V, E = map(int, input("Enter no. of vertices and edges: ").split())
        adj = [[] for _ in range(V)]
        print("Enter the edges:")
        for _ in range(E):
            u, v, w = map(int, input().split())
            adj[u].append((v, w))
            adj[v].append((u, w))
        S = int(input("Enter the source vertex: "))
        ob = Solution()
        res = ob.dijkstra(V, adj, S)
        print("Shortest distances from source vertex", S, ":")
        for i in res:
            print(i, end=" ")
        print()
