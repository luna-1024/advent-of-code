#!/usr/bin/env python3

from collections import *
import heapq

DIMENSION = 71
DIMENSION_TEST = 7

DIRECTIONS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]

def solution(lines):
    fell = []
    for line in lines:
        x, y = (int(v) for v in line.split(','))
        fell.append((y, x))
    
    test = len(fell) < 50
    dimension = DIMENSION_TEST if test else DIMENSION
    
    start = 0, 0
    end = dimension-1, dimension-1
    
    def steps_for_time(cutoff_time):
        fallen = set(fell[:cutoff_time])
        
        def adjacents(pos):
            adj = []
            for dy, dx in DIRECTIONS:
                pt = pos[0] + dy, pos[1] + dx
                if pt[0] in range(dimension) and pt[1] in range(dimension) and pt not in fallen:
                    adj.append(pt)
            return adj
        
        best = defaultdict(lambda: float('inf'))
        best[start] = 0
        visited = set()
        
        queue = []
        heapq.heappush(queue, (0, start))
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
                
        return best[end]
    
    for t in range(dimension**2+1):
        steps = steps_for_time(t)
        if steps == float('inf'):
            break
    
    # steps at t means t rocks have fallen, counting from 0 means t-1 index
    y, x = fell[t-1]
    print(f'{x},{y}')


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
