#!/usr/bin/env python3

from collections import *
from math import prod

# y, x
DIMENSION = (103, 101)
TEST_DIMENSION = (7, 11)

STEPS = 100

def solution(lines):
    robots = []
    for line in lines:
        robots.append(tuple(tuple(int(n) for n in v.split('=')[1].split(',')) for v in line.split(' ')))

    maxy, maxx = DIMENSION if len(robots) > 12 else TEST_DIMENSION
    
    def move(robot, steps):
        (px, py), (vx, vy) = robot
        fx = (px + vx * steps) % maxx
        fy = (py + vy * steps) % maxy 
        return fx, fy
    
    def quadrant(position):
        if position[1] == maxy // 2 or position[0] == maxx // 2:
            return None
        q = 0
        if position[1] > maxy // 2:
            q += 2
        if position[0] > maxx // 2:
            q += 1
        return q
    
    quads = Counter(quadrant(move(robot, STEPS)) for robot in robots)
    factor = prod(count for quad, count in quads.items() if quad is not None)
    print(factor)
    

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
