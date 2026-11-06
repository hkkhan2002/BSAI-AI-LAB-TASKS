graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["G"], "F": [], "G": []}

def dls(node, goal, limit, path):
    if node == goal:
        return "FOUND", path
    if limit == 0:
        if graph[node]:
            return "CUTOFF", None
        return "FAILURE", None
    cutoff = False
    for n in graph[node]:
        if n in path:
            continue
        status, result = dls(n, goal, limit - 1, path + [n])
        if status == "FOUND":
            return "FOUND", result
        if status == "CUTOFF":
            cutoff = True
    if cutoff:
        return "CUTOFF", None
    return "FAILURE", None

def iddfs(start, goal, max_limit):
    for limit in range(max_limit + 1):
        status, path = dls(start, goal, limit, [start])
        print("IDDFS limit", limit, "->", status, path)
        if status == "FOUND":
            return path
    return None


def main():
    for limit in [1, 2, 3, 4]:
        status, path = dls("A", "G", limit, ["A"])
        print("DLS limit", limit, "->", status, path)
    print()
    for max_limit in [1, 2, 3, 4]:
        print("IDDFS max limit", max_limit)
        iddfs("A", "G", max_limit)
        print()


if __name__ == "__main__":
    main()
