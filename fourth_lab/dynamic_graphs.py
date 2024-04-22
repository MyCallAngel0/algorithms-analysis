import random, time
import matplotlib.pyplot as plt

nV = 4

INF = 999


def floyd_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))
    # Add vertices
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    # print_solution(distance)


def print_solution(distance):
    for i in range(nV):
        for j in range(nV):
            if distance[i][j] == INF:
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


def min_distance(dist, sptSet):
    min_val = float('inf')
    min_index = -1
    for v in range(nV):
        if dist[v] < min_val and sptSet[v] is False:
            min_val = dist[v]
            min_index = v
    return min_index


# Dijkstra's Algorithm implementation
def dijkstra(graph, src):
    dist = [float('inf')] * nV
    dist[src] = 0
    sptSet = [False] * nV

    for cout in range(nV):
        u = min_distance(dist, sptSet)
        sptSet[u] = True

        for v in range(nV):
            if graph[u][v] > 0 and sptSet[v] is False and dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]

def generate_random_graph(num_vertices):
    graph = [[float('inf')] * num_vertices for _ in range(num_vertices)]

    # Generate random edge weights
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i != j:
                weight = random.randint(1, 10)  # Adjust the range as needed
                graph[i][j] = weight

    return graph


idx = 0
floyd_res = []
dij_res = []
inputs = []
for num_vertices in range(10, 1001, 10):
    graph = generate_random_graph(num_vertices)
    start_time = time.time()
    floyd_warshall(graph)
    end_time = time.time()
    ellapsed_time = (time.time() - start_time) * 1000
    floyd_res.append(ellapsed_time)

    start_time = time.time()
    dijkstra(graph, 0)
    ellapsed_time = (time.time() - start_time) * 1000
    dij_res.append(ellapsed_time)

    inputs.append(num_vertices)
    idx += 1
    # print(num_vertices)


plt.plot(inputs, floyd_res, marker='o', label='Floyd Warshall')
plt.plot(inputs, dij_res, marker='o', label='Dijkstra')
plt.legend()
plt.title("Dijkstra vs Floyd")
plt.xlabel("Nr of vertices")
plt.ylabel("Time(ms)")
plt.grid()
plt.show()
