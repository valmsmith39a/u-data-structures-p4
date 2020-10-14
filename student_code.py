"""
Sources:
    A* Search Algorithm
    https://en.wikipedia.org/wiki/A*_search_algorithm
    http://robotics.caltech.edu/wiki/images/e/e0/Astar.pdf
    https://www.redblobgames.com/pathfinding/a-star/introduction.html
    https://www.geeksforgeeks.org/a-search-algorithm/
    https://brilliant.org/wiki/a-star-search/
    
    Euclidean distance
    https://www.cut-the-knot.org/pythagoras/DistanceFormula.shtml
    
    Priority Queue
    https://docs.python.org/3/library/heapq.html
    https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/
"""
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

    # initialize g and f values
    for intersection in intersections.keys():
        if intersection == start:
            g_values[intersection] = 0
            f_values[intersection] = get_distance(start, goal, M)

        else:
            g_values[intersection] = float('inf')
            f_values[intersection] = float('inf')

    # create priority queue with `start` intersection
    heapq.heappush(frontier, (float('inf'), start))
    current_node = start

    while len(frontier) != 0:

        if current_node == goal:
            # build total_path
            total_path = [current_node]

            while current_node in best_previous_node.keys():
                current_node = best_previous_node[current_node]
                total_path.append(current_node)

            total_path.reverse()

            return total_path

        connected_nodes = roads[current_node]

        for node in connected_nodes:
            if node in explored:
                continue

            # calculate g value of connected node, with current node as the previous node
            g_connected_node_temp = g_values[current_node] + \
                get_distance(current_node, node, M)
            # calculate h of connected node
            h_connected_node = get_distance(node, goal, M)
            f_connected_node = g_connected_node_temp + h_connected_node

            # if calculated g value is greater than existing g value, then not the "best" previous node
            if g_connected_node_temp >= g_values[node]:
                continue

            # store best previous node, g and h values
            best_previous_node[node] = current_node
            g_values[node] = g_connected_node_temp
            f_values[node] = f_connected_node

            # push to priority queue
            if (node not in explored) and (node not in frontier):
                heapq.heappush(frontier, (f_connected_node, node))

        f, current_node = heapq.heappop(frontier)
        explored.add(current_node)

    return None
