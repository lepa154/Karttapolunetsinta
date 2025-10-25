import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from A_star_ import A_star
from jump_point_search import jump
import utils
from mapio import random_start_and_end

def obstacle_free():
    with open ("./data/maps/map_3x3.txt", "r", encoding="utf-8") as f:
        map = [list(line.strip()) for line in f]
    start_and_end = random_start_and_end(map)
    start = start_and_end[0]
    end = start_and_end[1]
    print(f"Alkupiste: {start}")
    print(f"Loppupiste: {end}")

    print(A_star(start, end, map)[0])

    