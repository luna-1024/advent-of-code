#!/usr/bin/env python3

from itertools import *

def check_report(report):
    sign = (1, -1)[report[-1]-report[0]  < 0]
    mind, maxd = sorted((sign, 3 * sign))
    return all(mind <= l2 - l1 <= maxd for l1, l2 in pairwise(report))

def solution(lines):
    reports = ([int(l) for l in report.split(' ')] for report in lines)
    
    valid = 0
    for report in reports:
        possible = check_report(report)
        
        for i in range(len(report)):
            fixed_report = report[:i] + report[i+1:]
            possible |= check_report(fixed_report) 
        valid += possible
    
    print(valid)


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
