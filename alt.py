from minimax import utility
from kalaha import traverse
from random import randrange

def southGreedy(board, side):
    move=1
    v=48
    for i in range(1,7):
        b=board.copy()
        if b[i+6]==0:
            continue
        b,s=traverse(b, False, i+6)
        if utility(b)<v:
            v=utility(b)
            move=i
    return move

def random(board,side):
    c=[]
    for pos in range(1,7):
        if board[pos-1]==0 and side:
            continue
        if board[pos+6]==0 and not side:
            continue
        c.append(pos)
    i = randrange(len(c))
    return c[i]    
    