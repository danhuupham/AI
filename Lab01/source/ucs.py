from queue import PriorityQueue


def ucs(matrix, start, end, heuristic=None, bonus_points=[], portals=[]):
    """
    Args:
        1. matrix: The matrix read from the input file,
        2. start, end: The starting and ending points,
    Returns:
        1. cost 
        2. The route from the starting point to the ending one, defined by an array of (x, y), e.g. route = [(1, 2), (1, 3), (1, 4)]
        3. The visited nodes
    """
    # 1. Define walls
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
    queue = PriorityQueue()
    queue.put((0, start))

    # 5. Define the parent
    parent = {}
    parent[start] = None

    # 6. Define the cost
    cost = {}
    cost[start] = 0

    # 7. Define portals
    portals_dict = {tuple(portal[:2]): tuple(portal[2:]) for portal in portals}

    # 7. Define the flag
    flag = False

    while not queue.empty():
        current = queue.get()[1]
        if current == end:
            flag = True
            break
        for i in range(4):
            x = current[0] + dx[i]
            y = current[1] + dy[i]
            if (x, y) not in walls and (x, y) not in visited:
                if (x, y) in portals_dict:
                    visited.append((x, y))
                    x, y = portals_dict[(x, y)]
                queue.put((cost[current] + 1, (x, y)))
                visited.append((x, y))
                parent[(x, y)] = current
                cost[(x, y)] = cost[current] + 1

    # 8. Return the route
    if flag:
        current = end
        while current != start:
            if current in portals_dict.values():
                tp = list(portals_dict.keys())[
                    list(portals_dict.values()).index(current)]
                route.append(current)
                route.append(tp)
                current = parent[current]
            else:
                route.append(current)
                current = parent[current]
        route.append(start)
        route.reverse()

        for node in route:
            if node in visited:
                visited.remove(node)

        return cost[end], route, visited
    else:
        return 'NO', [], visited
