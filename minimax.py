
from kalaha import traverse

depth = 4

def nextMoves(board,side):
    l = []
    for pos in range(1,7):
        b = board.copy()
        if b[pos-1]==0 and side:
            continue
        if b[pos+6]==0 and not side:
            continue
        if side:
            res = traverse(b, side, pos-1)
            l.append([[res[0],res[1]],pos])
        if not side:
            res = traverse(b, side, pos+6)
            l.append([[res[0],res[1]],pos])
    return l


def judge(board,side):
    l = nextMoves(board,side)
    max = -10000
    move = 0
    for i in l:
        b = i[0][0]
        
        
        if b[6]-b[13]> max and side:
            max = b[6]-b[13]
            move = i[1]
            
        if -b[6]+b[13]> max and not side:
            max = -b[6]+b[13]
            move = i[1]
            
    return move
        
    