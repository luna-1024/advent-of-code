#!/usr/bin/env python3

from collections import *
from itertools import *

NUMPAD = ['789', '456', '123', ' 0A']
DIRPAD = [' ^A', '<v>']

DIRECTIONS = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1) 
}

def build_path(pad):
    h = len(pad)
    w = len(pad[0])
    
    bad = set()
    for y in range(h):
        for x in range(w):
            if pad[y][x] == ' ':
                bad.add((y, x))
    assert len(bad) == 1
    bad = next(iter(bad))

    out = {}
    for y1, x1, y2, x2 in product(range(h), range(w), range(h), range(w)):
        c1 = pad[y1][x1]
        c2 = pad[y2][x2]
        if c1 == ' ' or c2 == ' ':
            continue
        
        dy = y2 - y1
        dx = x2 - x1
        by = ('v' * dy) if dy >= 0 else ('^' * abs(dy))
        bx = ('>' * dx) if dx >= 0 else ('<' * abs(dx))
        
        # optimal expansion
        if dx > 0 and (y2, x1) != bad:
            out_path = by + bx + 'A'
        elif (y1, x2) != bad:
            out_path = bx + by + 'A'
        elif (y2, x1) != bad:
            out_path = by + bx + 'A'
        else:
            raise Exception('bad path')
        
        out[c1+c2] = out_path
        
    return out

def expand_cpath(cpath, padpaths):
    out = Counter()
    for pair, count in cpath.items():
        for a, b in pairwise('A' + padpaths[pair]):
            out[a+b] += count
    return out

def solution(lines):
    numpadpaths = build_path(NUMPAD)
    dirpadpaths = build_path(DIRPAD)
    
    complexity = 0
    for path in lines:
        assert path[-1] == 'A'
        numeric = int(path[:-1])
        cpath = Counter(a+b for a, b in pairwise('A' + path))
        ncpath = expand_cpath(cpath, numpadpaths)
        for _ in range(25):
            ncpath = expand_cpath(ncpath, dirpadpaths)
        comp = sum(ncpath.values()) * numeric
        complexity += comp
        
    print(complexity)
    

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
