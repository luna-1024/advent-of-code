#!/usr/bin/env python3

DIRECTIONS = {
   '^': (-1, 0),
   '>': (0, 1),
   'v': (1, 0),
   '<': (0, -1),
}

def solution(sections):
    layout, insts = sections
    layout = layout.split('\n')
    insts = insts.replace('\n', '')
    maxy, maxx = len(layout), len(layout[0])
    
    walls = set()
    boxes = set()
    robot = None
    
    for y, line in enumerate(layout):
        for x, c in enumerate(line):
            if c == '#':
                walls.add((y, 2*x))
            elif c == 'O':
                boxes.add((y, 2*x))
            elif c  == '@':
                assert robot is None
                robot = y, 2*x
            else:
                assert c == '.'
    assert robot is not None
    
    def qmove_box(pos, direc):
        assert pos in boxes
        
        padj = pos[0] + direc[0], pos[1] + direc[1]
        if direc[0] != 0:
            # 3 colliding coords above/below
            # unconditionally present as all colliding obj are 2 wide
            tadj = [(padj[0], padj[1] - 1), padj, (padj[0], padj[1] + 1)]
        else:
            # to the left side it could be 2 coords, if there was a 1 wide obj
            # but instead all colliding obj are 2 wide
            tadj = [(padj[0], padj[1] + direc[1])]
        
        move_set = {pos}
        for cadj in tadj:
            if cadj in boxes and move_set is not None:
                sms = qmove_box(cadj, direc)
                if sms is not None:
                    move_set |= sms
                else:
                    move_set = None
            if cadj in walls:
                move_set = None

        return move_set
    
    def move_robot(direc):
        nonlocal robot, boxes
        
        adj_pos = robot[0] + direc[0], robot[1] + direc[1]
        ladj_pos = adj_pos[0], adj_pos[1] - 1
        
        if adj_pos in boxes:
            move_set = qmove_box(adj_pos, direc)
        elif ladj_pos in boxes:
            move_set = qmove_box(ladj_pos, direc)
        elif adj_pos in walls or ladj_pos in walls:
            move_set = None
        else:
            move_set = set()
            
        if move_set is not None:
            boxes -= move_set
            boxes |= {(p[0] + direc[0], p[1] + direc[1]) for p in move_set}
            robot = adj_pos
            return True
        return False

    def printgrid():
        out = ''
        for y in range(maxy):
            for x in range(maxx*2):
                p = y, x
                pp = y, x-1
                if p in walls or pp in walls:
                    out += '#'
                elif p in boxes:
                    out += '['
                elif pp in boxes:
                    out += ']'
                elif p == robot:
                    out += '@'
                else:
                    out += '.'
            out += '\n'
        print(out, end='')

    for inst in insts:
        move_robot(DIRECTIONS[inst])

    gpstotal = sum(100 * y + x for y, x in boxes)
    print(gpstotal)

if __name__ == '__main__':
    file_in = open('input.txt')
    sections = file_in.read().removesuffix('\n').split('\n\n')
    solution(sections)
