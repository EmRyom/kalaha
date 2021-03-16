
from kalaha import traverse
from random import randrange

def terminalTest(board):
    
    return (sum(board[0:6])==0 or sum(board[7:13])==0)


def utility(board):
    if terminalTest(board):
        board[6] += sum(board[0:6])
        board[13] += sum(board[7:13])
    return board[6]-board[13]


def maxValue(board, side, alpha, beta, count, depth): 
    
    # limiting depth    
    if terminalTest(board) or count == depth:
        return utility(board), None
    
    v = -100
    m = -100
    actions = nextMoves(board, side)
    # dummy statement
    final_action = actions[0]
    
    for a in actions:
       
        tboard = a[0]
        tside = a[1]
        pos = a[2]
        
        if tside != side:
            v = max(v, minValue(tboard, tside, alpha, beta, count+1, depth))
        else:
            v = max(v, maxValue(tboard, tside, alpha, beta, count+1, depth)[0])
            
        #debug
        '''
        print(str(count) + ':')
        print('pos: ' + str(pos))
        print('v: ' + str(v))
        '''
        if v >= beta:
            return v, None
        alpha = max(alpha, v)
        
        # storing best action
        if count == 0 and m<v:
            final_action = a
            m = v
        
        
    return v, final_action


def minValue(board, side, alpha, beta, count, depth):
    
    # limiting depth    
    if terminalTest(board) or count == depth:
        return utility(board)
    
    v = 100
    actions = nextMoves(board, side)
    
    for a in actions:
        
        tboard = a[0]
        tside = a[1]
        pos = a[2]
        
        if side != tside:
            v = min(v, maxValue(tboard, tside, alpha, beta, count+1, depth)[0])
        else:
            v = min(v, minValue(tboard, tside, alpha, beta, count+1, depth))
            
        #debug
        '''
        print(str(count) + ':')
        print('pos: ' + str(pos))
        print('v: ' + str(v))
        '''
        if v <= alpha:
            return v
        beta = min(beta, v)
    
    return v


def alphaBetaSearch(board, side, depth):
    
    final_action = maxValue(board, side, -100, 100, 0, depth)[1]
    
    return final_action
    
    

def nextMoves(board,side):
    l = []
    for pos in range(1,7):
        b = board.copy()
        if b[pos-1]==0 and side:
            continue
        if b[pos+6]==0 and not side:
            continue
        if side:
            b,s = traverse(b, side, pos-1)
            l.append((b,s,pos))
        if not side:
            b,s = traverse(b, side, pos+6)
            l.append((b,s,pos))
    return l


def judge(board,side):
    
    move = alphaBetaSearch(board, side, 7)[2]
            
    return move

def altJudge(board,side,depth):
    return alphaBetaSearch(board, side, depth)[2]
    

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
    