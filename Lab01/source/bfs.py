def bfs(matrix, start, end, heuristic=None):
    """
    Args:
        1. matrix: The matrix read from the input file,
        2. start, end: The starting and ending points,
    Returns:
        1. cost 
        2. The route from the starting point to the ending one, defined by an array of (x, y), e.g. route = [(1, 2), (1, 3), (1, 4)]
        3. The visited nodes
    """
    # 1. Define walls and array of direction based on the route
    walls = [(i, j) for i in range(len(matrix))
             for j in range(len(matrix[0])) if matrix[i][j] == 'x']
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    # 2. Define cost for each point
    cost = {(i, j): 0 for i in range(len(matrix))
            for j in range(len(matrix[0])) if matrix[i][j] != 'x'}
    cost[start] = 0
    cost[end] = 0

    # 3. Define the route
    route = [start]
    visited = [start]

    # 4. Define the queue
    queue = []
    queue.append(start)

    # 5. Define the parent
    parent = {}
    parent[start] = None

    # 6. Define the cost
    cost = {}
    cost[start] = 0

    # 7. Define the flag
    flag = False

    while queue:
        current = queue.pop(0)
        if current == end:
            flag = True
            break
        for i in range(4):
            x = current[0] + dx[i]
            y = current[1] + dy[i]
            if (x, y) not in walls and (x, y) not in visited:
                queue.append((x, y))
                visited.append((x, y))
                parent[(x, y)] = current
                cost[(x, y)] = cost[current] + 1

    # 8. Return the route
    if flag:
        current = end
        while current != start:
            route.append(current)
            current = parent[current]
        route.append(start)
        route.reverse()

        for node in route:
            if node in visited:
                visited.remove(node)

        return cost[end], route, visited
    else:
        return -1, [], visited
