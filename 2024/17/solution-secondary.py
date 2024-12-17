#!/usr/bin/env python3

'''
b = a & 7
b = b ^ 7
c = a // (2 ^ b)
b = b ^ 7
a = a // (2 ^ 3)
b = b ^ c
out <- b & 7
loop if a > 0

while a > 0:
    b = (a & 7) ^ 7
    c = a // (2 ^ b)
    b ^= 7 ^ c
    out <- b & 7
    a //= 8

# each output depends on 16 lsb of a, then shift on 8 bits of a
~ = not, xor 7
L = list(of u8), pop/peek accesses lsb
while len(a) > 0:
    let b: u3 = L.peek()
    let c: u3 = L.peek2() >> b
    L.pop()
    b ^= ~c
    out(b)
'''


class HaltException(Exception):
    pass

def run_program(a, b, c, program):
    
    ip = 0
    def get():
        nonlocal ip
        if ip >= len(program):
            raise HaltException()
        v = program[ip]
        ip += 1
        return v
    out = []
    
    def get_combo():
        operand = get()
        if operand < 4:
            return operand
        elif operand == 4:
            return a
        elif operand == 5:
            return b
        elif operand == 6:
            return c
        elif operand == 7:
            raise Exception('reserved combo operand type 7')
    
    try:
        while ip < len(program):
            ic = get()
            #jumped = False
            if ic == 0:
                # adv
                a = a // (2**get_combo())
            elif ic == 1:
                # bxl
                b = b ^ get()
            elif ic == 2:
                # bst
                b = get_combo() & 7
            elif ic == 3:
                # jnz
                if a != 0:
                    ip = get()
                    #jumped = True
            elif ic == 4:
                # bxc
                get()
                b = b ^ c
            elif ic == 5:
                # out
                out.append(get_combo() & 7)
            elif ic == 6:
                # bdv
                b = a // (2**get_combo())
            elif ic == 7:
                # cdv
                c = a // (2**get_combo())
    except HaltException:
        pass
    return out

def solution(sections):
    regs, program = sections
    ra, rb, rc = (int(reg.split(': ')[1]) for reg in regs.split('\n'))
    program = [int(v) for v in program.split(': ')[1].split(',')]
        
    def test_run(a):
        return run_program(a, rb, rc, program)
    
    def find_program(a=0, index=len(program)-1):
        for delta in range(8):
            test_a = a * 8 + delta
            if test_run(test_a) == program[index:]:
                if index == 0:
                    return test_a
                final_a = find_program(test_a, index - 1)
                if final_a is not None:
                    return final_a
        return None
        
    print(find_program())



if __name__ == '__main__':
    file_in = open('input.txt')
    sections = file_in.read().removesuffix('\n').split('\n\n')
    solution(sections)
