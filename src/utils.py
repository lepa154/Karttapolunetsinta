import math
from typing import Tuple

# looking for possible points from which to move
def find_neighbors(coordinate, map):
    height = len(map)
    width = len(map[0])
    possible_moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    
    neighbors = []
    for i in possible_moves: 
        x = i[0]
        y = i[1]
        # coordinates of the next move
        new_x = coordinate[0] + x 
        new_y = coordinate[1] + y
        # the coordinates are not outside the map or at an obstacle
        if 0 <= new_x < height and 0 <= new_y < width and map[new_x][new_y] != '@':
            # move up/down or left/right: cost 1, here 10 to avoid decimals
            # move to northeast/southeast/southwest/northwest: cost sqrt(2), here 14 to avoid decimals
            if x == 0 or y == 0:
                cost = 10
            else:
                cost = 14
            # add a point to the neighbors
            neighbors.append(((new_x, new_y), cost))
    
    return neighbors

def search_heuristic(point_a, point_b):

    # calculate the absolute value between two points
    x = abs(point_a[0] - point_b[0])
    y = abs(point_a[1] - point_b[1])
    # in multiples of ten to avoid decimals
    return 10 * (x + y) + (4 * min(x, y))

def distance(point_a, point_b):
    x = abs(point_a[0] -point_b[0])
    y = abs(point_a[1] - point_b[1])

    return max(x, y)

# which points belong to the shortest path
def find_path(before_path, start_point, end_point):
    path = [end_point]
    point = end_point
    while point in before_path:
        path.append(point)
        # from which point to we came from to this point
        point = before_path[point]
    path.reverse()
    path.insert(0, start_point)

    return path

def check_over_the_edge(point, map):
    x = point[0]
    y = point[1]
    if 0 <= x < len(map) and 0 <= y < len(map[0]):
        return map[x][y]
    else:
        return None
    
def safe_read(map, x, y):
    if 0 <= x < len(map) and 0 <= y < len(map[0]):
        return map[x][y]
    return None  # kartan ulkopuoli
    
def has_forced_neighbor(map, point, direction):
    x, y = point
    dx, dy = direction

    for nx in [-1, 0, 1]:
        for ny in [-1, 0, 1]:
            if nx == 0 and ny == 0:
                continue

            neighbor = safe_read(map, x + nx, y + ny)
            if neighbor is None:
                continue

            # jos viereinen ruutu on este ja viereinen ruutu sen vieressä on vapaa
            if neighbor != ".":
                adj = safe_read(map, x - nx, y - ny)
                if adj == ".":
                    return True
    return False



    


if __name__ == "__main__":
    x = (1, 1)
    y = (1, 0)
    print(f"({x[0]+y[0]}, {x[1]+y[1]})")