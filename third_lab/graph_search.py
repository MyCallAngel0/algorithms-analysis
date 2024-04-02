from collections import defaultdict, deque
import random, time
import matplotlib.pyplot as plt


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start_node):
        if start_node not in self.graph:
            return "No such Node"

        visited = set()
        queue = deque([start_node])

        while queue:
            node = queue.popleft()
            visited.add(node)

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    def dfs(self, start_node):
        visited = set()
        stack = deque([start_node])

        while stack:
            node = stack.pop()
            if node in visited:
                continue
            if node not in self.graph:
                continue
            visited.add(node)
            for neighbor in reversed(self.graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)


nodes = []
def generate_random_graphs(num_graphs):
    all_graphs = []
    num_nodes = 0
    for _ in range(num_graphs):
        graph = Graph()
        vertices = set()
        num_nodes += 200
        nodes.append(num_nodes)

        while len(vertices) < num_nodes:
            u, v = random.sample(range(num_nodes), 2)
            if u != v and v not in graph.graph[u]:
                graph.addEdge(u, v)
                vertices.add(u)
                vertices.add(v)

        all_graphs.append(graph)

    return all_graphs


random_graphs = generate_random_graphs(num_graphs=50)
bfs_time = []
dfs_time = []

for graph in random_graphs:
    start_time = time.time()*1000
    graph.bfs(random_graphs.index(graph))
    bfs_time.append(time.time()*1000-start_time)

    start_time = time.time()*1000
    graph.dfs(random_graphs.index(graph))
    dfs_time.append(time.time()*1000 - start_time)

plt.plot(nodes, bfs_time, label='BFS', color='blue', marker='o')
plt.plot(nodes, dfs_time, label='DFS', color='lime', marker='o')
plt.title("Graph searching comparison")
plt.xlabel("Number of nodes")
plt.ylabel("Time (ms)")
plt.legend()
plt.show()