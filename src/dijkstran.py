import utils
import heapq
from utils import find_path, find_neighbors

def dijkstran(map, start_point, end_point):
    # dictionary of what is the shortest distance to a point so far
    distances = {start_point: 0}        
    # to save the route
    before = {}
    # priority queue                         
    queue = [(0, start_point)]  
    # Which points have been visited so far        
    visited = set()
    

    while len(queue) != 0:
        # search for the point with the smallest distance from the points found so far
        distance_current, coordinate_current = heapq.heappop(queue)
        if coordinate_current == end_point:
            break
        if coordinate_current in visited:
            continue
        visited.add(coordinate_current)

        # through all the points that we can move to
        for i in utils.find_neighbors(coordinate_current, map):
            distance = i[1]
            coordinate = i[0]
            # smallest distance to the point from the start_point
            distance_new = distance_current + distance

            # the point has not been visited or the new distance is smaller than the one already found
            if coordinate not in distances or distance_new < distances[coordinate]: 
                distances[coordinate] = distance_new
                before[coordinate] = coordinate_current
                # add coordinate to priority queue
                heapq.heappush(queue, (distance_new, coordinate))

    # what route the algorithm has taken
    path = find_path(before, start_point, end_point)

    # if didn't reach end_point
    if end_point not in distances:
        return None, None
    # return shortest distance to enc_point and path
    return distances[end_point], path

    


    
