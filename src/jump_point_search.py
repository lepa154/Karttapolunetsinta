import heapq
from utils import find_neighbors, find_path, search_heuristic, check_over_the_edge, has_forced_neighbor, distance

def jump(map, point, direction, end_point):
    rows = len(map)
    cols = len(map[0])

    new_point = (point[0] + direction[0], point[1] + direction[1])

    if not (0 <= new_point[0] < rows and 0 <= new_point[1] < cols):
        return None
    if map[new_point[0]][new_point[1]] != ".":
        return None
    
    if new_point == end_point:
        return new_point
    
    # jos tällä ruudulla on pakottava naapuri, se on jump point
    if has_forced_neighbor(map, new_point, direction):
        return new_point

    # jos liikut diagonaalisesti, jatka myös molempia suoria suuntia
    dx, dy = direction
    if dx != 0 and dy != 0:
        if jump(map, new_point, (dx, 0), end_point) is not None or \
           jump(map, new_point, (0, dy), end_point) is not None:
            return new_point

    # jatka eteenpäin samaan suuntaan
    return jump(map, new_point, direction, end_point)


def A_star_for_jump_point(start_point, end_point, map):
    directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]

    open_list = []
    g_score = {start_point: 0}
    h_score = {start_point: search_heuristic(start_point, end_point)}
    f_score = {start_point: g_score[start_point] + h_score[start_point]}

    heapq.heappush(open_list, (f_score[start_point], start_point))
    closed = set()
    before = {}

    while open_list:
        score, current_point = heapq.heappop(open_list)

        if current_point == end_point:
            return g_score[end_point], find_path(before, start_point, end_point)

        closed.add(current_point)

        for direction in directions:
            jump_point = jump(map, current_point, direction, end_point)
            if jump_point is None or jump_point in closed:
                continue

            new_g = g_score[current_point] + distance(current_point, jump_point)

            if jump_point not in g_score or new_g < g_score[jump_point]:
                before[jump_point] = current_point
                g_score[jump_point] = new_g
                h_score[jump_point] = search_heuristic(jump_point, end_point)
                f_score[jump_point] = new_g + h_score[jump_point]
                heapq.heappush(open_list, (f_score[jump_point], jump_point))

    # jos polkua ei löydy, palautetaan kaksi arvoa
    return None, None
