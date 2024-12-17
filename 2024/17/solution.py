#!/usr/bin/env python3

class HaltException(Exception):
    pass

def run_program(a, b, c, program, outfn):
    
    ip = 0
    def get():
        nonlocal ip
        if ip >= len(program):
            raise HaltException()
        v = program[ip]
        ip += 1
        return v
    
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
                outfn(get_combo() & 7)
            elif ic == 6:
                # bdv
                b = a // (2**get_combo())
            elif ic == 7:
                # cdv
                c = a // (2**get_combo())
    except HaltException:
        pass

def solution(sections):
    regs, program = sections
    ra, rb, rc = (int(reg.split(': ')[1]) for reg in regs.split('\n'))
    program = [int(v) for v in program.split(': ')[1].split(',')]
    
    out = []
    def retain_out(v):
        out.append(v)
    
    run_program(ra, rb, rc, program, retain_out)
    print(','.join(str(v) for v in out))


if __name__ == '__main__':
    file_in = open('input.txt')
    sections = file_in.read().removesuffix('\n').split('\n\n')
    solution(sections)
