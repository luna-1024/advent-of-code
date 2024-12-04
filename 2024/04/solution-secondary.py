#!/usr/bin/env python3

TARGET = ['M', 'S']

def solution(lines):
    lines = list(lines)

    xmas = 0
    for y in range(1, len(lines) - 1):
        for x in range(1, len(lines[0]) - 1):
            if lines[y][x] != 'A':
                continue
            ul, ur, dl, dr = lines[y-1][x-1], lines[y-1][x+1], lines[y+1][x-1], lines[y+1][x+1]
            
            if sorted((ul, dr)) == TARGET and sorted((ur, dl)) == TARGET:
                xmas += 1
            
    print(xmas)


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
