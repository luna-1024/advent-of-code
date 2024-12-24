#!/usr/bin/env python3

from collections import defaultdict

OPS = {
    'AND': lambda x, y: x and y,
    'OR': lambda x, y: x or y,
    'XOR': lambda x, y: x != y
}

def parse_wire(wire):
    name, val = wire.split(': ')
    return name, bool(val)

def solution(sections):
    wirespecs, gatespecs = sections
    
    wires = {}
    for wirespec in wirespecs.split('\n'):
        name, val = wirespec.split(': ')
        wires[name] = bool(int(val))
        
    gates = defaultdict(set)
    for gatespec in gatespecs.split('\n'):
        expr, output = gatespec.split(' -> ')
        w1, operand, w2 = expr.split(' ')
        spec = operand, w1, w2, output
        gates[w1].add(spec)
        gates[w2].add(spec)
    
    proc = list(wires.items())
    donewires = set()
    while len(proc) > 0:
        setwire, val = proc.pop()
        donewires.add(setwire)
        for operand, w1, w2, output in gates[setwire]:
            if not (output not in wires and w1 in wires and w2 in wires):
                continue
            res = OPS[operand](wires[w1], wires[w2])
            wires[output] = res
            proc.append((output, res))
        
    num = sum(val * (1 << int(wn[1:])) for wn, val in wires.items() if wn[0] == 'z')
    print(num)

if __name__ == '__main__':
    file_in = open('input.txt')
    sections = file_in.read().removesuffix('\n').split('\n\n')
    solution(sections)
