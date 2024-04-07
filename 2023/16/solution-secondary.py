#!/usr/bin/env python3

from collections import defaultdict

# dy, dx
# RLDU
DIRS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]

def solution(lines):
    lines = list(lines)
    h, w = len(lines), len(lines[0])
    
    grid = {}
    
    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            if c != '.':
                assert c in '-|/\\'
                grid[(y, x)] = c
    
    def pathcoverage(spoint, sdir):
        # to check point, incoming dir
        paths = {(spoint, sdir)}
        covered = defaultdict(set)
        
        def nextpoint(point, incdir):
            newpoint = point[0] + incdir[0], point[1] + incdir[1]
            if newpoint[0] in range(h) and newpoint[1] in range(w):
                if newpoint not in covered or incdir not in covered[newpoint]:
                    return newpoint
            return None
        
        while len(paths) > 0:
            point, incdir = paths.pop()
            while True:
                covered[point].add(incdir)
                if point in grid:
                    ptype = grid[point]
                    if ptype == '/':
                        incdir = DIRS[3-DIRS.index(incdir)]
                    elif ptype == '\\':
                        incdir = DIRS[(2+DIRS.index(incdir)) % 4]
                    elif ptype == '-' and incdir in [DIRS[2], DIRS[3]]:
                        incdir, defdir = DIRS[0], DIRS[1]
                        defpoint = nextpoint(point, defdir)
                        if defpoint:
                            paths.add((defpoint, defdir))
                    elif ptype == '|' and incdir in [DIRS[0], DIRS[1]]:
                        incdir, defdir = DIRS[2], DIRS[3]
                        defpoint = nextpoint(point, defdir)
                        if defpoint:
                            paths.add((defpoint, defdir))
                point = nextpoint(point, incdir)
                if point == None:
                    break

        coverage = len(covered.keys())
        return coverage
    
    
    starts = []
    starts += [((y, 0), DIRS[0]) for y in range(h)]
    starts += [((y, w-1), DIRS[1]) for y in range(h)]
    starts += [((0, x), DIRS[2]) for x in range(w)]
    starts += [((h-1, x), DIRS[3]) for x in range(w)]
    
    bestcoverage = max(pathcoverage(pt, direc) for pt, direc in starts)
    print(f'Solution: {bestcoverage}')


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
