#!/usr/bin/env python3

import heapq
from collections import defaultdict

DIRECTIONS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]

def solution(lines):
    grid = list(lines)
    h = len(grid)
    w = len(grid[0])
    
    
    def adjacents(v):
        (y, x), direc = v
        adj = []
        for pdirec in DIRECTIONS:
            if (-pdirec[0], -pdirec[1]) == direc:
                continue
            py, px = y + pdirec[0], x + pdirec[1]
            if grid[py][px] not in '.SE':
                continue
            adj.append((1 if pdirec == direc else 1001, ((py, px), pdirec)))
        return adj
    
    for y in range(h):
        for x in range(w):
            if grid[y][x] == 'S':
                start = (y, x), DIRECTIONS[0]
            elif grid[y][x] == 'E':
                end = y, x
    
    best = defaultdict(lambda: float('inf'))
    best[start] = 0
    visited = set()
    
    queue = []
    heapq.heappush(queue, (0, start))
    while len(queue) > 0:
        score, state = heapq.heappop(queue)
        
        if state in visited:
            continue
        visited.add(state)
        
        for score, adj in adjacents(state):
            test_score = best[state] + score
            if adj not in visited and test_score < best[adj]:
                best[adj] = test_score
                heapq.heappush(queue, (test_score, adj))
    
    best_score = min(best[(end, direc)] for direc in DIRECTIONS)
    print(best_score)

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
