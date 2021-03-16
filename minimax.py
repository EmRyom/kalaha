
from kalaha import traverse
from random import randrange

i = [0]

def test(d):    
    i[0]=0
    
    print(boardValue([4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0],True,d))
    print(i)

def boardValue(board,side,depth):
    i[0]+=1
    b = board.copy()
    if depth==0:
        return b[6]-b[13],b[6]-b[13]
    else:
        high=-48
        low=48
        for pos in range(1,7):
            b = board.copy()
            if b[pos-1]==0 and side:
                continue
            if b[pos+6]==0 and not side:
                continue
            if side:    
                b,s = traverse(b, side, pos-1)
                low,high=boardValue(b,s,depth-1)
            else:
                b,s = traverse(b, side, pos+6)
                low,high=boardValue(b,s,depth-1)
        return low,high
                

def judge(board,side):
    depth = 6
    m = -100
    r = 48
    move = 1
    for pos in range(1,7):
        b = board.copy()
        if b[pos-1]==0 and side:
            continue
        if b[pos+6]==0 and not side:
            continue
        if side:    
            b,s = traverse(b, side, pos-1)
            th,tl=boardValue(b,s,depth-1)
            #print(th,tl)
        else:
            b,s = traverse(b, side, pos+6)
            th,tl=boardValue(b,s,depth-1)
        if th - tl < r and (tl+th)/2 > m :
            m = (tl+th)/2
            r = th - tl
            move=pos
        
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
        
        
        