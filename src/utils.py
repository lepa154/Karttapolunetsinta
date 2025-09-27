import math

def find_neighbors(coordinate, map):
    height = len(map)
    width = len(map[0])
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    possible_neighbors = []
    for i in moves:
        possible_neighbors.append((coordinate[0]+i[0], coordinate[1]+i[1]))
    
    neighbors = []
    for i in possible_neighbors:
        if 0 <= i[0] < height-1 and 0 <= i[1] < width-1 and map[i[0]][i[1]] != '@':
            if i in possible_neighbors[:4]:
                cost = 1
            else:
                cost = math.sqrt(2)  
            neighbors.append((i, cost))
    



    return neighbors





    


if __name__ == "__main__":
    x = (1, 1)
    y = (1, 0)
    print(f"({x[0]+y[0]}, {x[1]+y[1]})")