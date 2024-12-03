#!/usr/bin/env python3

from itertools import *

def solution(lines):
    reports = ([int(l) for l in report.split(' ')] for report in lines)
    
    valid = 0
    for report in reports:
        sign = (1, -1)[report[-1]-report[0]  < 0]
        mind, maxd = sorted((sign, 3 * sign))
        valid += all(mind <= l2 - l1 <= maxd for l1, l2 in pairwise(report))
    
    print(valid)


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
