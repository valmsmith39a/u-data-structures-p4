import math


class AStar(object):

    def shortest_path(self, M, start, goal):
        # intersections = M.intersections
        intersections = {0: [0.7798606835438107, 0.6922727646627362],
                         1: [0.7647837074641568, 0.3252670836724646],
                         2: [0.7155217893995438, 0.20026498027300055],
                         3: [0.7076566826610747, 0.3278339270610988],
                         4: [0.8325506249953353, 0.02310946309985762],
                         5: [0.49016747075266875, 0.5464878695400415],
                         6: [0.8820353070895344, 0.6791919587749445],
                         7: [0.46247219371675075, 0.6258061621642713],
                         8: [0.11622158839385677, 0.11236327488812581],
                         9: [0.1285377678230034, 0.3285840695698353]}
        # TODO: use M.roads
        # connected_intersections = M.roads[current_intersection]
        connected_intersections = [2, 5, 6]
        current_int = start
        end_int = goal

        distance_dict = {}

        for connected_i in connected_intersections:
            conn_int_x = intersections[connected_i][0]
            conn_int_y = intersections[connected_i][1]
            curr_int_x = intersections[current_int][0]
            curr_int_y = intersections[current_int][1]
            end_int_x = intersections[end_int][0]
            end_int_y = intersections[end_int][1]

            # g
            distance_int = math.sqrt((conn_int_x - curr_int_x)
                                     ** 2 + (conn_int_y - curr_int_y)**2)

            # h
            distance_end = math.sqrt((end_int_x - conn_int_x)
                                     ** 2 + (end_int_y - conn_int_y)**2)

            # f
            distance = distance_int + distance_end

            distance_dict[connected_i] = [distance_int, distance_end, distance]

        # TODO:
        # Get the smallest f and that is the next node
        # Figure out the stopping condition
        # All all the frontiers explored
        pass


# show_map(map_40, start=5, goal=34, path=[5, 16, 37, 12, 34])
a_star = AStar()
map_40 = 'test map 40'
path = a_star.shortest_path(map_40, 5, 9)

if path == [5, 16, 37, 12, 34]:
    print("great! Your code works for these inputs!")
else:
    print("something is off, your code produced the following:")
    print(path)
