#!/usr/bin/env python3

def solution(lines):
    
    left, right = zip(*[map(int, line.split('   ')) for line in lines])
    left, right = sorted(left), sorted(right)

    total = 0
    for li, ri in zip(left, right):
        total += abs(li - ri)
    
    print(total)


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
