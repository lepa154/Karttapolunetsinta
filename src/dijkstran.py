import utils
import heapq

def dijkstran(map, start_point, end_point):
    distances = {start_point: 0}
    before = {}
    queue = [(0, start_point)]
    visited = set()
    
    while len(queue) != 0:
        distance_current, coordinate_current = heapq.heappop(queue)
        if coordinate_current == end_point:
            break
        if coordinate_current in visited:
            continue
        visited.add(coordinate_current)

        for i in utils.find_neighbors(coordinate_current, map):
            distance = i[1]
            coordinate = i[0]
            distance_new = distance_current + distance

            if coordinate not in distances or distance_new < distances[coordinate]:
                distances[coordinate] = distance_new
                before[coordinate] = coordinate_current
                heapq.heappush(queue, (distance_new, coordinate))

    return distance_current
    
