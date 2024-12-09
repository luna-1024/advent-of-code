#!/usr/bin/env python3

from collections import *
from itertools import *

def solution(lines):
    
    antns = defaultdict(set)
    
    lines = list(lines)
    maxy, maxx = len(lines), len(lines[0])

    validpt = lambda p: p[0] in range(maxy) and p[1] in range(maxx)
    
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c != '.':
                antns[c].add((y, x))

    anodes = set()
    for locs in antns.values():
        for (y1, x1), (y2, x2) in combinations(locs, 2):
            dy, dx = y2-y1, x2-x1
            pl = y1-dy, x1-dx
            ph = y2+dy, x2+dx
            for pt in (pl, ph):
                if validpt(pt):
                    anodes.add(pt)

    print(len(anodes))

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
