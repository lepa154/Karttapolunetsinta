
# the route appears in the output as P letters
def draw_route(map, visited):
    for i, j in visited:
        map[i][j] = "P"
    return map


        