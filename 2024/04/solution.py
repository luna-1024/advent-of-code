#!/usr/bin/env python3

from collections import *

def diagonalize(hlines):
    out = defaultdict(str)
    for y in range(len(hlines)):
        for x in range(len(hlines[0])):
            out[x + y] += hlines[y][x]
    return list(out.values())


def count(lines, key):
    rkey = ''.join(reversed(key))
    assert key != rkey
    return sum(line.count(key) + line.count(rkey) for line in lines)
    
def solution(lines):
    horz = list(lines)
    vert = [''.join(c) for c in zip(*horz)]
    rev = [''.join(reversed(line)) for line in horz]
    diaga = diagonalize(horz)
    diagb = diagonalize(rev)
    
    key = 'XMAS'
    total = count(horz, key) + count(vert, key) + count(diaga, key) + count(diagb, key)
    print(total)


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
