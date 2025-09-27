import mapio
import utils
import dijkstran

if __name__ == "__main__":
    map = mapio.read_map()
    start_and_end = mapio.random_start_and_end(map)
    start = start_and_end[0]
    end = start_and_end[1]
    print(start)
    print(end)

    naapurit = utils.find_neighbors(start, map)

    shortest_route = dijkstran.dijkstran(map, start, end)
    print(shortest_route)
