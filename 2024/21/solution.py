#!/usr/bin/env python3

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

def expand_path(path, padpaths):
    out = ''
    for a, b in pairwise('A' + path):
        out += padpaths[a+b]
    return out

def solution(lines):
    numpadpaths = build_path(NUMPAD)
    dirpadpaths = build_path(DIRPAD)
    
    complexity = 0
    for path in lines:
        assert path[-1] == 'A'
        numeric = int(path[:-1])
        npe = expand_path(path, numpadpaths)
        r1p = expand_path(npe, dirpadpaths)
        r2p = expand_path(r1p, dirpadpaths)
        comp = len(r2p) * numeric
        complexity += comp
        
    print(complexity)
    

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
