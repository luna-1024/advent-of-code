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
    
    tfid = len(diskl) // 2
    while tfid >= 0:
        rpos = tfid * 2
        assert len(diskl[rpos]) == 1
        assert diskl[rpos][0][0] == tfid
        
        fid, size = diskl[rpos][0]
        
        widx = 1
        while widx < rpos:
            nfid, wsize = diskl[widx][-1]
            if nfid is None and size <= wsize:
                diskl[rpos] = [(None, size)]
                diskl[widx].pop()
                diskl[widx].append((fid, size))
                rsize = wsize - size
                if rsize > 0:
                    diskl[widx].append((None, rsize))
                break
            widx += 2
        
        tfid -= 1

    checksum = 0
    pos = 0
    for chunk in diskl:
        for fid, count in chunk:
            if fid is not None:
                checksum += range_sum(pos, pos + count) * fid
            pos += count
    
    print(checksum)

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
