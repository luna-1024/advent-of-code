#!/usr/bin/env python3

from collections import *

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
        return (fx, fy), (vx, vy)
    
    def quadrant(position):
        if position[1] == maxy // 2 or position[0] == maxx // 2:
            return None
        q = 0
        if position[1] > maxy // 2:
            q += 2
        if position[0] > maxx // 2:
            q += 1
        return q
    
    def draw_robots(robots):
        pos = set(p for p, v in robots)
        print('\n'.join(''.join('.#'[(x, y) in pos] for x in range(maxx)) for y in range(maxy)))
    
    t = 0
    while True:
        robots = [move(robot, 1) for robot in robots]
        t += 1

        quads = Counter(quadrant(p) for p, v in robots)
        t1, t2, *_ = sorted(quads.values(), reverse=True)
        # low entropy
        if t1 / t2 > 3:
            #print(t)
            #draw_robots(robots)
            #print()
            break

    print(t)

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
