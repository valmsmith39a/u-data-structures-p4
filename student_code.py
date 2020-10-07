import math


def shortest_path(M, start, goal):
    intersections = M.intersections
    roads = M.roads

    start_coord = intersections[start]
    goal_coord = intersections[goal]

    connected_roads = roads[start]
    connected_road_coords = []
    current_coord = start_coord

    f_total_estimated_cost = 0
    f_least = [0, 0]

    for connected_road in connected_roads:
        connected_road_coords.append(
            [intersections[connected_road], connected_road])

    for idx, connected_road_coord in enumerate(connected_road_coords):
        g_path_cost = math.sqrt((current_coord[0] - connected_road_coord[0][0]) ** 2 + (
            current_coord[1] - connected_road_coord[0][1]) ** 2)
        h_estimated_path_cost = math.sqrt(
            connected_road_coord[0][0] - goal_coord[0] ** 2 + connected_road_coord[0][1] - goal_coord[1] ** 2)

        f = g_path_cost + h_estimated_path_cost

        if idx is 0:
            f_least = [f, connected_road_coord]

        if f < f_least[0]:
            f_least = [f, connected_road_coord]

    # TODO: Get to the next coordinate based on the least estimated total path cost

    return
