#!/usr/bin/env python3

from collections import *

def solution(lines):
    graph = defaultdict(set)
    for line in lines:
        l, r = line.split('-')
        graph[l].add(r)
        graph[r].add(l)
    
    
    largest_group = set()
    for node in graph:
        group = {node}
        for cand in graph:
            if cand != node and all(member in graph[cand] for member in group):
                group.add(cand)
        
        if len(group) > len(largest_group):
            largest_group = group
    
    print(','.join(sorted(largest_group)))


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
