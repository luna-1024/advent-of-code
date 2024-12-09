#!/usr/bin/env python3

from collections import *

def range_sum(n, m):
    return (m - n) * (n + (m - 1)) // 2

def solution(lines):
    
    disk = list(lines)
    assert len(disk) == 1
    disk = disk[0]
    
    diskl = []
    
    for i, c in enumerate(disk):
        count = int(c)
        if i % 2 == 0:
            assert count > 0
            fid = i // 2
            diskl.append([(fid, count)])
        else:
            diskl.append([(None, count)])
    
    widx = 1
    while diskl[-2][-1][0] is None:
        (fid, fl), = diskl.pop()
        while fl > 0 and diskl[-1][-1][0] is None:
            nfid, size = diskl[widx].pop()
            assert nfid is None
            fw = min(size, fl)
            diskl[widx].append((fid, fw))
            fl -= fw
            frem = size - fw
            if frem == 0:
                widx += 2
            else:
                diskl[widx].append((None, frem))
        if diskl[-1][0][0] is None:
            diskl.pop()
        elif fl > 0:
            diskl.append([(fid, fl)])
    if diskl[-1][-1][0] is None:
        diskl[-1].pop()

    checksum = 0
    pos = 0
    for chunk in diskl:
        for fid, count in chunk:
            checksum += range_sum(pos, pos + count) * fid
            pos += count
    
    print(checksum)

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
