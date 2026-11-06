import heapq

graph = {'S': [('A', 1), ('B', 4)], 'A': [('C', 2)], 'B': [('G', 5)], 'C': [('G', 3)], 'G': []}
h = {'S': 5, 'A': 4, 'B': 4, 'C': 2, 'G': 0}
true_cost = {'S': 6, 'A': 5, 'B': 5, 'C': 3, 'G': 0}

print('Admissibility check, h must be <= true cost:')
for node in ['S', 'A', 'B', 'C', 'G']:
    print(node, 'h =', h[node], 'true cost =', true_cost[node], 'ok =', h[node] <= true_cost[node])

print()
print('Consistency check, h(u) must be <= cost + h(v):')
for node in graph:
    for nxt, w in graph[node]:
        print(node, '->', nxt, h[node], '<=', w, '+', h[nxt], '=', w + h[nxt], 'ok =', h[node] <= w + h[nxt])

print()
print('First three expansions by hand:')
print('S: g = 0, h = 5, f = 0 + 5 = 5')
print('A: g = 1, h = 4, f = 1 + 4 = 5')
print('C: g = 1 + 2 = 3, h = 2, f = 3 + 2 = 5')
print('Frontier after C: G (6, 0, 6), B (4, 4, 8). G is picked next.')


def astar_search(h_values):
    count = 0
    heap = [(h_values['S'], count, 0, 'S', ['S'])]
    best = {'S': 0}
    order = []
    while heap:
        f, _, g, node, path = heapq.heappop(heap)
        if g != best[node]:
            continue
        order.append(node)
        if node == 'G':
            return path, g, order
        for nxt, w in graph[node]:
            new_g = g + w
            if new_g < best.get(nxt, 9999):
                best[nxt] = new_g
                count += 1
                heapq.heappush(heap, (new_g + h_values[nxt], count, new_g, nxt, path + [nxt]))
    return None, 0, order


print()
print('Normal run:', astar_search(h))
h_bad = dict(h)
h_bad['C'] = 10
print('h(C) changed from 2 to 10, true cost of C is 3, so 10 is an overestimate.')
print('Overestimate run:', astar_search(h_bad))
