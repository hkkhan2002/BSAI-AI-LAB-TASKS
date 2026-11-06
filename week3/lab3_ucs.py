import heapq
from collections import deque

graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F', 'G'], 'D': [], 'E': ['G'], 'F': [], 'G': []}
weights = {('A', 'B'): 1, ('A', 'C'): 2, ('B', 'D'): 2, ('B', 'E'): 1,
           ('C', 'F'): 3, ('C', 'G'): 10, ('E', 'G'): 1}


def ucs(start, goal):
    n = 0
    pq = [(0, n, start, [start])]
    best_cost = {start: 0}
    order = []
    while pq:
        cost, _, node, path = heapq.heappop(pq)
        if cost != best_cost[node]:
            continue
        order.append(node)
        if node == goal:
            return path, cost, order
        for nxt in graph[node]:
            new_cost = cost + weights[(node, nxt)]
            if new_cost < best_cost.get(nxt, 9999):
                best_cost[nxt] = new_cost
                n += 1
                heapq.heappush(pq, (new_cost, n, nxt, path + [nxt]))
    return None, 0, order


def bfs_path(start, goal):
    q = deque([(start, [start])])
    seen = {start}
    while q:
        node, path = q.popleft()
        if node == goal:
            return path
        for nxt in graph[node]:
            if nxt not in seen:
                seen.add(nxt)
                q.append((nxt, path + [nxt]))
    return None


path, cost, order = ucs('A', 'G')
print('UCS processing order:', order)
print('UCS path:', path)
print('UCS cost:', cost)

total = 0
for i in range(len(path) - 1):
    total = total + weights[(path[i], path[i + 1])]
print('Cost checked by adding edges again:', total)

broute = bfs_path('A', 'G')
bcost = 0
for i in range(len(broute) - 1):
    bcost = bcost + weights[(broute[i], broute[i + 1])]
print('BFS path on the same graph:', broute)
print('BFS path cost:', bcost)
