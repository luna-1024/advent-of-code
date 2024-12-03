#!/usr/bin/env python3

import re

def solution(lines):
    count = True
    total = 0
    for line in lines:
        for m in re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don\'t)\(\)', line):
            x, y, do, do_not = m.groups()
            if do is not None:
                count = True
            elif do_not is not None:
                count = False
            elif count:
                total += int(x) * int(y)

    print(total)


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
