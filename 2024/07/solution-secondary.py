#!/usr/bin/env python3

def concat(a, b):
    return int(str(a) + str(b))

def possible(test, accum, rem):
    if len(rem) == 0:
        return test == accum

    cur, *newrem = rem
    return (possible(test, accum + cur, newrem) or 
            possible(test, accum * cur, newrem) or
            possible(test, concat(accum, cur), newrem))
    

def solution(lines):
    
    total_cal = 0
    
    for line in lines:
        test, vals = line.split(': ')
        test = int(test)
        vals = [int(v) for v in vals.split(' ')]
        
        if possible(test, vals[0], vals[1:]):
            total_cal += test
    
    print(total_cal)


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
