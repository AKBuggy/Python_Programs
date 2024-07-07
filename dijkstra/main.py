import sys


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name):
        self.vertices[name] = {}

    def add_edge(self, from_vertex, to_vertex, weight):
        self.vertices[from_vertex][to_vertex] = weight

    def dijkstra(self, start_vertex):
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start_vertex] = 0
        visited = set()
        while len(visited) < len(self.vertices):
            current_vertex = min(
                (vertex for vertex in self.vertices if vertex not in visited),
                key=lambda vertex: distances[vertex]
            )
            visited.add(current_vertex)
            for neighbor, weight in self.vertices[current_vertex].items():
                new_distance = distances[current_vertex] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
        return distances


def main():
    graph = Graph()

    num_vertices = int(input("Enter the number of vertices: "))
    for i in range(num_vertices):
        vertex_name = input("Enter the name of vertex {}: ".format(i + 1))
        graph.add_vertex(vertex_name)

    num_edges = int(input("Enter the number of edges: "))
    for i in range(num_edges):
        from_vertex, to_vertex, weight = input("Enter edge {} (from_vertex to_vertex weight): ".format(i + 1)).split()
        graph.add_edge(from_vertex, to_vertex, int(weight))

    start_vertex = input("Enter the start vertex: ")
    distances = graph.dijkstra(start_vertex)

    print("Shortest distances from vertex {}:".format(start_vertex))
    for vertex, distance in distances.items():
        print("To vertex {}: {}".format(vertex, distance))


if __name__ == "__main__":
    main()
