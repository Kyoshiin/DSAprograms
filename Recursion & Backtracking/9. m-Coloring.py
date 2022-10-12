# Python3 program for solution of M Coloring
# problem using backtracking

def safeToClr(node, graph, color, colr):
    for adj_nodes in graph[node]:
        if color[adj_nodes] == colr:
            return False

    return True


def solve(node, graph, m, n, color):
    if node == n:
        return True

    for colr in range(1, m + 1):
        if safeToClr(node, graph, color, colr):
            color[node] = colr

            if solve(node + 1, graph, m, n, color): return True
            color[node] = 0  # backtracking when no possible colour for node found
    return False  # when no possible colour found


def graphColouring(graph, m, n):
    color = [0] * n
    return 1 if solve(0, graph, m, n, color) else 0


# Driver Code
# 1 -> can be coloured
# 0-> cant be coloured
if __name__ == '__main__':
    # case:1
    # n = 4
    # graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
    # m = 3

    # case:2
    n = 3
    graph = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    m = 2
    print(graphColouring(graph, m, n))
