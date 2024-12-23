#!/usr/bin/env python3

from collections import *
from itertools import *

ST = 't'

def solution(lines):
    graph = defaultdict(set)
    for line in lines:
        l, r = line.split('-')
        graph[l].add(r)
        graph[r].add(l)
    
    count = 0
    for a, b, c in combinations(graph.keys(), 3):
        if a[0] != ST and b[0] != ST and c[0] != ST:
            continue
        
        if b in graph[a] and c in graph[b] and a in graph[c]:
            count += 1

    print(count)


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
