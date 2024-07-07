class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def bellman_ford(self, src):
        dist = [float("Inf")] * self.V
        dist[src] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Check for negative cycles
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative cycle")
                return

        print("Shortest distances:")
        for i in range(self.V):
            print("From", src, "to", i, ":", dist[i])


# Taking user input to create the graph
V = int(input("Enter the number of vertices: "))
g = Graph(V)

E = int(input("Enter the number of edges: "))
print("Enter the edges (source, destination, weight):")
for _ in range(E):
    u, v, w = map(int, input().split())
    g.add_edge(u, v, w)

src = int(input("Enter the source vertex: "))

g.bellman_ford(src)
