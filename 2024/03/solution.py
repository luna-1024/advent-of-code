#!/usr/bin/env python3

import re

def solution(lines):
    total = 0
    for line in lines:
        for m in re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)', line):
            x, y = map(int, m.groups())
            total += x * y

    print(total)


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
