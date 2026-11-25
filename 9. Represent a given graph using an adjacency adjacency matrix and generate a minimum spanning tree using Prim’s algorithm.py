
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj = [[0 for _ in range(vertices)]
                    for _ in range(vertices)]

    def add_edge(self, source, destination, weight):
        self.adj[source][destination] = weight
        self.adj[destination][source] = weight

    def display_graph(self):
        print("\nAdjacency Matrix:")
        for row in self.adj:
            print(row)

    def prims(self):
        visited = [False] * self.vertices
        key = [float('inf')] * self.vertices
        parent = [-1] * self.vertices

        key[0] = 0
        total_weight = 0

        for _ in range(self.vertices):
            minimum = float('inf')
            u = -1

            for v in range(self.vertices):
                if not visited[v] and key[v] < minimum:
                    minimum = key[v]
                    u = v

            if u == -1:
                print("\nGraph is disconnected. MST cannot be formed.")
                return

            visited[u] = True

            if parent[u] != -1:
                print(parent[u], "-", u, "Weight:", key[u])
                total_weight += key[u]

            for v in range(self.vertices):
                if (self.adj[u][v] != 0 and
                        not visited[v] and
                        self.adj[u][v] < key[v]):
                    key[v] = self.adj[u][v]
                    parent[v] = u

        print("\nMinimum Spanning Tree Weight:", total_weight)


def main():
    vertices = int(input("Enter number of vertices: "))

    if vertices <= 0:
        print("Number of vertices must be greater than zero.")
        return

    graph = Graph(vertices)

    edges = int(input("Enter number of edges: "))

    if edges < 0:
        print("Number of edges cannot be negative.")
        return

    print("Enter each edge as source, destination and weight (0 to",
          vertices - 1, "):")

    for i in range(edges):
        source, destination, weight = map(
            int, input(f"Edge {i + 1}: ").split()
        )

        if (0 <= source < vertices and
                0 <= destination < vertices and
                source != destination and weight > 0):
            graph.add_edge(source, destination, weight)
        else:
            print("Invalid edge or weight.")
            return

    graph.display_graph()

    print("\nMinimum Spanning Tree using Prim's Algorithm:")
    graph.prims()


if __name__ == "__main__":
    main()
