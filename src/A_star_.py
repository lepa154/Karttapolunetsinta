from typing import List, Tuple, Dict, Set
import numpy as np
import heapq
from math import sqrt
from utils import search_heuristic, find_neighbors, find_path

def A_star(start_point, end_point, map):
    #priority list of nodes that have not yet been explored
    open_list = [] 
    # actual cost
    g_score = {start_point: 0} 
    # estimated cost
    h_score = {start_point: search_heuristic(start_point, end_point)} 
    # priority queue (actual cost + estimated cost to end_point)
    f_score = {start_point: g_score[start_point] + h_score[start_point]} 

    heapq.heappush(open_list, (f_score[start_point], start_point))
    
    # nodes visited
    closed = set()      
    # the route from which node to which node                
    before = {}                  
    
    while open_list:
        # get node with lowest f value
        score, current_point = heapq.heappop(open_list) 
        
        if current_point == end_point:
            return g_score[end_point], find_path(before, start_point, end_point) # etsitään kuljettu reitti
            
        closed.add(current_point)
        
        # explore neighbors
        for neighbor, cost in find_neighbors(current_point, map):
            # skip if already explored
            if neighbor in closed:
                continue
                
            # cost for new route to node
            new_g = g_score[current_point] + cost
            
            # create and update neighbor
            if neighbor not in g_score or new_g < g_score[neighbor]:
                g_score[neighbor] = new_g
                h_score[neighbor] = search_heuristic(neighbor, end_point)
                f_score[neighbor] = new_g + h_score[neighbor]
                before[neighbor] = current_point
                heapq.heappush(open_list, (f_score[neighbor], neighbor))
            

    return []  

