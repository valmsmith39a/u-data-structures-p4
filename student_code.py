import math
import heapq


def get_distance(loc1, loc2, Map):
    coord1 = Map.intersections[loc1]
    coord2 = Map.intersections[loc2]
    x1 = coord1[0]
    x2 = coord2[0]
    y1 = coord1[1]
    y2 = coord2[1]

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def shortest_path(M, start, goal):
    intersections = M.intersections
    roads = M.roads

    explored = set()
    frontier = []
    g_values = dict()
    f_values = dict()
    best_previous_node = dict()

    for intersection in intersections.keys():
        if intersection == start:
            g_values[intersection] = 0
            f_values[intersection] = get_distance(start, goal, M)

        else:
            g_values[intersection] = float('inf')
            f_values[intersection] = float('inf')

    heapq.heappush(frontier, (float('inf'), start))
    current_node = start

    while len(frontier) != 0:
        f, current_node = heapq.heappop(frontier)
        explored.add(current_node)

        if current_node == goal:
            total_path = [current_node]
            curr_node = current_node
            while curr_node in best_previous_node.keys():
                curr_node = best_previous_node[curr_node]
                total_path.append(curr_node)
            return [x for x in reversed(total_path)]

        connected_nodes = roads[current_node]

        for node in connected_nodes:
            if node in explored:
                continue

            g_connected_node_temp = g_values[current_node] + \
                get_distance(current_node, node, M)
            h_connected_node = get_distance(node, goal, M)
            f_connected_node = g_connected_node_temp + h_connected_node

            if g_connected_node_temp >= g_values[node]:
                continue

            best_previous_node[node] = current_node
            g_values[node] = g_connected_node_temp
            f_values[node] = f_connected_node

            if node not in explored:
                if node not in frontier:
                    heapq.heappush(frontier, (f_connected_node, node))

    return None
