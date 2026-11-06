import heapq

graph = {"S": [("A", 1), ("B", 4)], "A": [("C", 2)], "B": [("G", 5)], "C": [("G", 3)], "G": []}
h = {"S": 5, "A": 4, "B": 4, "C": 2, "G": 0}


def search(start, goal, use_h):
    count = 0
    start_f = h[start] if use_h else 0
    heap = [(start_f, count, 0, start, [start])]
    best = {start: 0}
    order = []
    expanded = 0
    while heap:
        f, _, g, node, path = heapq.heappop(heap)
        if g != best[node]:
            continue
        order.append(node)
        if node == goal:
            return path, g, order, expanded
        expanded = expanded + 1
        for nxt, w in graph[node]:
            new_g = g + w
            if new_g < best.get(nxt, 9999):
                best[nxt] = new_g
                count += 1
                new_f = new_g + h[nxt] if use_h else new_g
                heapq.heappush(heap, (new_f, count, new_g, nxt, path + [nxt]))
    return None, 0, order, expanded


path, cost, order, expanded = search("S", "G", True)
print("A* path:", path)
print("A* cost:", cost)
print("A* processed order:", order)
print("A* expanded nodes (goal not counted):", expanded)
path2, cost2, order2, expanded2 = search("S", "G", False)
print("UCS path:", path2)
print("UCS cost:", cost2)
print("UCS processed order:", order2)
print("UCS expanded nodes (goal not counted):", expanded2)
