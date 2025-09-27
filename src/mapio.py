import random

def read_map():
    with open ("./data/maps/map2.txt", "r", encoding="utf-8") as f:
        lines = [list(line.strip()) for line in f]

    return lines

def random_start_and_end(map):
    height = (len(map))-1
    witdh = len((map[0]))-1

    while True:
        x = random.randint(0, height)
        y = random.randint(0, witdh)
        start_coordinate = (x, y)
        if map[x][y] == '.':
            break

    while True:
        x = random.randint(0, height)
        y = random.randint(0, witdh)
        end_coordinate = (x, y)
        if map[x][y] == '.':
            if end_coordinate != start_coordinate:
                break

    return (start_coordinate, end_coordinate)
