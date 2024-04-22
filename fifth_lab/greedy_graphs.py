import random, time
import matplotlib.pyplot as plt

INF = 9999999


def prim_algorithm(G, V):
    selected = [0] * V
    selected[0] = True
    no_edge = 0
    while no_edge < V - 1:
        minimum = INF
        x = 0
        y = 0
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if not selected[j] and G[i][j]:
                        if minimum > G[i][j]:
                            minimum = G[i][j]
                            x = i
                            y = j
        selected[y] = True
        no_edge += 1

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)
    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1


def kruskal_algorithm(G, V):
    result = []
    i = 0
    e = 0
    G_sorted = sorted(
        [(G[i][j], i, j) for i in range(V) for j in range(i + 1, V)], key=lambda x: x[0]
    )
    parent = [i for i in range(V)]
    rank = [0] * V
    while e < V - 1:
        w, u, v = G_sorted[i]
        i += 1
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            e += 1
            result.append((u, v, w))
            union(parent, rank, x, y)

inputs = []

prim_res = []
krusk_res = []

for V in range(10, 501, 10):
    G = [[0] * V for _ in range(V)]
    for i in range(V):
        for j in range(i + 1, V):
            G[i][j] = G[j][i] = random.randint(1, 100)
    # print(V)

    start_time = time.time()
    prim_algorithm(G, V)
    ellapsed_time = (time.time() - start_time) * 1000
    prim_res.append(ellapsed_time)

    start_time = time.time()
    kruskal_algorithm(G, V)
    ellapsed_time = (time.time() - start_time) * 1000
    krusk_res.append(ellapsed_time)

    inputs.append(V)

plt.plot(inputs, prim_res, marker='o', label='Prim')
plt.plot(inputs, krusk_res, marker='o', label='Kruskal')
plt.legend()
plt.title("Prim vs Kruskal")
plt.xlabel("Nr of vertices")
plt.ylabel("Time(ms)")
plt.grid()
plt.show()