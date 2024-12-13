#!/usr/bin/env python3

def extract(s, c, extra=0):
    return (int(v.split(c)[1]) + extra for v in s.split(': ')[1].split(', '))

def solve(ax, bx, cx, ay, by, cy):
    det = ax * by - bx * ay
    
    if det == 0:
        if cx * ay == cy * ax and cx * by  == cy * bx:
            return min((cx // ax) * 3, cx // bx)
        else:
            return 0
    
    a, am = divmod(cx * by - cy * bx, det)
    b, bm = divmod(cy * ax - cx * ay, det)
    
    if not (am == 0 and bm == 0 and a > 0 and b > 0):
        return 0
    
    return 3 * a + b

def solution(sections):
    total = 0
    for section in sections:
        ba, bb, pr = section.split('\n')
        ax, ay = extract(ba, '+')
        bx, by = extract(bb, '+')
        cx, cy = extract(pr, '=', 10000000000000)
        
        soln = solve(ax, bx, cx, ay, by, cy)
        total += soln
    
    print(total)


if __name__ == '__main__':
    file_in = open('input.txt')
    sections = (section.strip() for section in file_in.read().split('\n\n'))
    solution(sections)
