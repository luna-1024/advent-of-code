#!/usr/bin/env python3

from collections import  *
from itertools import *

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def count_nc(ds):
    total = 0
    for cs in ds.values():
        cs = sorted(cs)
        total += 1
        for pa, pb in pairwise(cs):
            if pb != pa + 1:
                total += 1
    return total

def perimeter(points):
    ys, xs = defaultdict(set), defaultdict(set)
    for y, x in points:
        for dy, dx in DIRECTIONS:
            ck = y + dy, x + dx
            if ck not in points:
                # use coordinate system for perimeter pieces such that
                # these 4 edge locations must be distinct:
                # above/below N and above/below N+1
                py, px = y + dy/4, x + dx/4
                if dy != 0:
                    ys[py].add(int(px))
                else:
                    xs[px].add(int(py))

    return count_nc(ys) + count_nc(xs)

def solution(lines):
    grid = list(lines)
    maxy, maxx = len(grid), len(grid[0])
    
    def fullregion(y, x):
        ty = grid[y][x]
        points = set()
        scan = set([(y, x)])
        while len(scan) > 0:
            nextscan = set()
            for y, x in scan:
                points.add((y, x))
                for dy, dx in DIRECTIONS:
                    ny, nx = y + dy, x + dx
                    if ny in range(maxy) and nx in range(maxx) and grid[ny][nx] == ty:
                        pt = ny, nx
                        if pt not in points:
                            nextscan.add(pt)
            scan = nextscan
        return points
    
    mapped = set()
    
    def cost_and_mark(y, x):
        nonlocal mapped
        assert (y, x) not in mapped
        points = fullregion(y, x)
        area = len(points)
        perim = perimeter(points)
        mapped |= points
        return area * perim
    
    total = 0
    for y in range(maxy):
        for x in range(maxx):
            if (y, x) not in mapped:
                total += cost_and_mark(y, x)
    print(total)


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
