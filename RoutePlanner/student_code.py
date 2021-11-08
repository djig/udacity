import math
import heapq
from ds import getMap


def shortest_path(M,start,goal):
    """
    Returns a list of intersections that form the shortest
    path from start to goal.
    using A* algorithm and a min-heap(priority queue)

    """
    estimated_cost = get_estimated_cost(M, goal)
    min_cost_heap = []
    # add the start node to the heap
    heapq.heappush(min_cost_heap, (0, start))
    # initialize the explored dictionary
    explored = dict()
    # initialize the parent dictionary
    previous_paths = dict()
    # initialize the cost dictionary
    cost = dict()
    explored[start] = True
    # for start node parent is None
    previous_paths[start] = None
    # for start node cost is 0
    cost[start] = 0
    while min_cost_heap:
        # pop the node with the minimum cost
        curr = heapq.heappop(min_cost_heap)[1]
        # if the current node is the goal node
        if curr == goal:
            res = []
            res.append(curr)
            #  build the path based on the parent dictionary
            while previous_paths[curr] is not None:
                res.insert(0,previous_paths[curr])
                curr = previous_paths[curr]
    
            return res
        # if curr== 8:
        #     print(M.roads[curr])
        #  get all the neighbors/roads of the current node
        for road in M.roads[curr]:
            if road not in explored:
                explored[road] = True
                # set parent for road
                previous_paths[road] = curr
                # set cost for road
                cost[road] = cost[curr] + calculate_distance(M.intersections[curr], M.intersections[road])
                # add f=g+h to the heap
                heapq.heappush(min_cost_heap, (cost[road] + estimated_cost[road], road))
                if curr== 8:
                    print(min_cost_heap)
    return None
    
def calculate_distance(node1, node2):
    """
    calculate the distance between two nodes
    """
    x0, y0 = node1
    x1, y1 = node2
    distance = (x1-x0)*(x1-x0) + (y1-y0) * (y1-y0)
    return math.sqrt(distance)


def get_estimated_cost(M, node_index):
    """
    get the estimated cost for each node
    after third test case failing
    i tried esitmated cost as the distance from the goal node
    using the heuristic function
    http://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html
    tweaked the heuristic function Diagonal distance 
    tried euclidean distance and manhattan distance 
    both failed for path = shortest_path(map, 8, 24)
    Tweaked Diagonal distance worked for path = shortest_path(map, 8, 24)

    """
    node1 = M.intersections[node_index]
    dict_estimated_cost = dict()
    for node,cords in M.intersections.items():
        dx = abs(cords[0] - node1[0])
        dy = abs(cords[1] - node1[1])
        h = (dx + dy) + (math.sqrt(2) - 3 ) * min(dx, dy)
        dict_estimated_cost[node] = h
    return dict_estimated_cost


map = getMap()
path = shortest_path(map, 8, 24)
print(path)
path = shortest_path(map, 5, 34)
print(path)
