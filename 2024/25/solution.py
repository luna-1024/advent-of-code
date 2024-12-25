#!/usr/bin/env python3

def solution(sections):
    locks = []
    keys = []
    
    for section in sections:
        lines = section.split('\n')

        if all(c == '#' for c in lines[0]):
            is_lock = True
        elif all(c == '#' for c in lines[-1]):
            is_lock = False
            
        walkrange = [range(5, 0, -1), range(1, 6)][is_lock]
        cut = []
        for c in range(5):
            l = 0
            for r in walkrange:
                if lines[r][c] != '#':
                    break
                l += 1
            cut.append(l)
        if is_lock:
            locks.append(list(cut))
        else:
            keys.append(list(cut))
    
    combo_matches = 0
    for lock in locks:
        for key in keys:
            combo_matches += all(li + ki <= 5 for li, ki in zip(lock, key))
            
    print(combo_matches)


if __name__ == '__main__':
    file_in = open('input.txt')
    sections = file_in.read().removesuffix('\n').split('\n\n')
    solution(sections)
