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
    
    walls = set()
    boxes = set()
    robot = None
    
    for y, line in enumerate(layout):
        for x, c in enumerate(line):
            if c == '#':
                walls.add((y, x))
            elif c == 'O':
                boxes.add((y, x))
            elif c  == '@':
                assert robot is None
                robot = y, x
            else:
                assert c == '.'
    assert robot is not None
    

    def transmit_force(pos, direc, is_robot=False):
        nonlocal robot
        update_robot = robot == pos
        assert is_robot == update_robot
        
        adj_pos = pos[0] + direc[0], pos[1] + direc[1]
        assert adj_pos != robot
        
        if adj_pos in boxes:
            can_move = transmit_force(adj_pos, direc)
        elif adj_pos in walls:
            can_move = False
        else:
            can_move = True
            
        if can_move:
            if update_robot:
                robot = adj_pos
            else:
                boxes.remove(pos)
                boxes.add(adj_pos)
            return True
        else:
            return False

    for inst in insts:
        transmit_force(robot, DIRECTIONS[inst], True)
        
    gpstotal = sum(100 * y + x for y, x in boxes)
    print(gpstotal)

if __name__ == '__main__':
    file_in = open('input.txt')
    sections = file_in.read().removesuffix('\n').split('\n\n')
    solution(sections)
