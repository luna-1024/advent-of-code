#!/usr/bin/env python3

import heapq
from collections import defaultdict
from itertools import *

DIRECTIONS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]

CHEAT_DIST = 20
THRESHOLD = 100
THRESHOLD_TEST = 50

def solution(lines):
    grid = list(lines)
    h = len(grid)
    w = len(grid[0])
    
    
    def adjacents(v):
        y, x = v
        adj = []
        for dy, dx in DIRECTIONS:
            py, px = y + dy, x + dx
            if grid[py][px] not in '.SE':
                continue
            adj.append((py, px))
        return adj
    
    for y in range(h):
        for x in range(w):
            if grid[y][x] == 'S':
                start = y, x
            elif grid[y][x] == 'E':
                end = y, x
                
    def full_paths_from(start_pos):
        best = defaultdict(lambda: float('inf'))
        best[start_pos] = 0
        visited = set()
        
        queue = []
        heapq.heappush(queue, (0, start_pos))
        while len(queue) > 0:
            score, pos = heapq.heappop(queue)
            
            if pos in visited:
                continue
            visited.add(pos)
            
            for adj in adjacents(pos):
                test_score = best[pos] + 1
                if adj not in visited and test_score < best[adj]:
                    best[adj] = test_score
                    heapq.heappush(queue, (test_score, adj))
    
        return best
    
    start_best = full_paths_from(start)
    end_best = full_paths_from(end)
    
    normal_dist = start_best[end]
    
    threshold = THRESHOLD if h > 16 else THRESHOLD_TEST
    cutoff = normal_dist - threshold
    
    count = 0
    impmap = defaultdict(int)
    for (cheat_start, start_dist), (cheat_end, end_dist) in product(start_best.items(), end_best.items()):
        bridge_dist = abs(cheat_end[0] - cheat_start[0]) + abs(cheat_end[1] - cheat_start[1])
        
        if bridge_dist > CHEAT_DIST:
            continue
        
        cheated_dist = start_dist + end_dist + bridge_dist
        if cheated_dist <= cutoff:
            count += 1
            impmap[normal_dist - cheated_dist] += 1
    
    print(count)

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
