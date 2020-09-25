agents that can plan ahead to solve problems

complexity from many states

sequence of actions from starting point to destination

definition of a problem

    Initial State =>  s0 

    Actions (s) =>  {a1, a2, a3...}

        in some problems agent will have the same actions available in all states 

        in some problems actions dependent on the state 

            routes you have available depend on which city (state) you're in

    Result (s, a) => s'
        s: previous state
        a: previous action
        s': new state

    GoalTest(s) => True | False 

        tells if this state is a goal or not 

        route finding: goal would be destination city. 

                  aj       aj+1
    Path Cost (Si -> Si + 1 -> Si+2) => cost value (n)
                                        where i = 0, 1,...
                                              j = 1, 2,...

    Step Cost  (s, a, s') => n (cost of that action)

apply to route finding

    state space: set of all the states

        navigate the state space by applying actions 

        actions are specific to each city

    frontier: 
        
        ends of the paths

        the farthest points that have been explored

    explored part of the state

    unexplored part of the state 

Uniform Cost Search algorithm (cheapest first)

    cheapest (lowest) path cost 

    on average, need to search 1/2 the search space before find goal

    to improve, need to add knowledge

estimate of distance from start to goal

    straight line distance from start to goal 

Greedy Best First Search algorithm 

    expands the path that is the shortest distance to the goal, according to the estimate

    now the search is directed towards the goal 

A* Search

    f = g + h

    g(path) = path cost
    h(path) = h(s) = estimated distance to the goal

    minimize g 

    minimize h 

    finds the shortest path and expands the minium number of paths possible 

    "best estimated total path cost first"

A* finds the lowest cost path if: h(s) < true cost

    h (estimated distance to the goal at a state) should never overestimate distance to a goal 

    h is optimistic 

    h is admissable 

    







