#!/usr/bin/env python3

from collections import defaultdict

OPS = {
    'AND': lambda x, y: x and y,
    'OR': lambda x, y: x or y,
    'XOR': lambda x, y: x != y
}

SWAPS = {} 

for a, b in [('dbp', 'fdv'), ('z15', 'ckj'), ('z23', 'kdf'), ('z39', 'rpp')]:
    SWAPS[a] = b
    SWAPS[b] = a

def swaplook(w):
    if w in SWAPS:
        return SWAPS[w]
    return w

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
        w1, w2 = sorted([w1, w2])
        output = swaplook(output)
        spec = operand, w1, w2, output
        gates[w1].add(spec)
        gates[w2].add(spec)
    
    inmx = max(int(wn[1:]) for wn in wires)
    assert f'x{inmx}' in wires and f'y{inmx}'in wires
    
    (operanda, w1a, w2a, outputa), (operandb, w1b, w2b, outputb) = sorted(gates['x00'])
    assert w1a == w1b =='x00' and w2a == w2b == 'y00' and operanda == 'AND' and operandb == 'XOR'
    assert outputb == 'z00'
    carry = outputa
    
    # This is a manual validator. It is not fully featured to prompt all types of correction suggestions.
    for wn in range(1, inmx+1):
        print(f'validating index {wn}')

        (operanda, w1a, w2a, partcarrya), (operandb, w1b, w2b, initsum) = sorted(gates[f'x{wn:02}'])
        assert w1a == w1b ==f'x{wn:02}' and w2a == w2b == f'y{wn:02}' and operanda == 'AND' and operandb == 'XOR'
        
        (operanda, w1a, w2a, partcarryb), (operandb, w1b, w2b, finalsum) = sorted(gates[initsum])
        if carry not in (w1a, w2a):
            print(sorted(gates[initsum]))
            #assert carry in (w1b, w2b)
            print(f'carry wire {carry} should swap output {partcarryb}')
            break
            
        if carry not in (w1b, w2b):
            assert carry in (w1a, w2a)
            print(f'carry wire {carry} should swap output {finalsum}')
            break
        
        fstarget = f'z{wn:02}'
        if finalsum != fstarget:
            print(f'swap output exp {fstarget} found {finalsum}')
            break
        
        (operanda, w1a, w2a, newcarrya), = sorted(gates[partcarrya])
        (operandb, w1b, w2b, newcarryb), = sorted(gates[partcarryb])
        if newcarrya != newcarryb:
            print(f'one of these is wrong: {newcarrya} {newcarryb}')
        
        assert operanda == 'OR'
        if partcarryb not in (w1a, w2a):
            print(f'swap issue {partcarrya}')
        
        assert operandb == 'OR'
        if partcarrya not in (w1b, w2b):
            print(f'swap issue {partcarryb}')
            
        carry = newcarrya
        
    if wn == inmx:
        print(f'validating index {wn+1}')
        if carry != f'z{wn+1}':
            print(f'bad final digit exp z{wn+1} got {carry}')
        else:
            print(','.join(sorted(SWAPS.keys())))

if __name__ == '__main__':
    file_in = open('input.txt')
    sections = file_in.read().removesuffix('\n').split('\n\n')
    solution(sections)
