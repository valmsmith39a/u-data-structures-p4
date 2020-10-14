Route Planner 

A* search algorithm 

Disconnected network of 10 intersections 

Edge between 2 roads is literal straight road 

Helper functions:

    from helpers import Map, load_map, show_map
    from student_code import shortest_path

Map object

    intersections

        dictionary

        Ex 

        {0: [0.7798606835438107, 0.6922727646627362],
        1: [0.7647837074641568, 0.3252670836724646],
        2: [0.7155217893995438, 0.20026498027300055],
        3: [0.7076566826610747, 0.3278339270610988],
        4: [0.8325506249953353, 0.02310946309985762],
        5: [0.49016747075266875, 0.5464878695400415],
        6: [0.8820353070895344, 0.6791919587749445],
        7: [0.46247219371675075, 0.6258061621642713],
        8: [0.11622158839385677, 0.11236327488812581],
        9: [0.1285377678230034, 0.3285840695698353]}

    roads

        list 

        i: intersection 

        roads[i]: list of intersections connected to intersection i

            i = 3

            [2, 5, 6]

            Ex  map_10.roads[0] 

            [7, 6, 5]

            map_10.roads

            [[7, 6, 5],
            [4, 3, 2],
            [4, 3, 1],
            [5, 4, 1, 2],
            [1, 2, 3],
            [7, 0, 3],
            [0],
            [0, 5],
            [9],
            [8]]

To run: 
show_map(map_40, start=5, goal=34, path=[5,16,37,12,34])

Create the graph, or maybe I don't need to

Distance, use a^2 + b^2 = c^2

key components of A*

s0: initial state

actions function: a(s) => {a1, a2...}

results function: r(s, a) => s'

goal test function: g(s) => True/False

path cost function: pc(transitions) => cost value

step cost function: sc(s, a, s') => n (cost of that action)

h function 

f = g + h

g function: g(s) => cost of the path

h function: h(s) => estimate from next city to destination
