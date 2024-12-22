#!/usr/bin/env python3

MOD = 2**24
STEPS = 2000

def advance_secret(n):
    n ^= (n << 6) % MOD
    n ^= (n >> 5) % MOD
    n ^= (n << 11) % MOD
    return n

def solution(lines):
    numbers = [int(line) for line in lines]
    
    total = 0
    for number in numbers:
        for _ in range(STEPS):
            number = advance_secret(number)
        total += number
    print(total)
    

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
