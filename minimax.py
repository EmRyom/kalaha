
from kalaha import traverse

depth = 4

def terminalTest(board):
    
    return (sum(board[0:6])==0 or sum(board[7:13])==0)


def utility(board, side):
    
    if side:
        return board[6]-board[13]
    else:
        return -board[6]+board[13]


def maxValue(board, side, alpha, beta, count, depth): 
    
    # limiting depth    
    if terminalTest(board) or count == depth:
        return utility(board, side), None
    
    v = -100
    actions = nextMoves(board, side)
    # dummy statement
    final_action = actions[0]
    
    for a in actions:
        tboard = a[0]
        tside = a[1]
        #print(maxValue(tboard, tside, alpha, beta, count+1, depth)[0])
        if tside != side:
            v = max(v, minValue(tboard, tside, alpha, beta, count+1, depth))
        else:
            v = max(v, maxValue(tboard, tside, alpha, beta, count+1, depth)[0])
            
        #debug
        #print(str(count) + ':')
        #print('pos: ' + str(a[2]))
        #print('v: ' + str(v))
        if v >= beta:
            return v, final_action
        alpha = max(alpha, v)
        
        # storing best action
        if count == 0 and alpha == v:
            final_action = a
        
        
    return v, final_action


def minValue(board, side, alpha, beta, count, depth):
    
    # limiting depth    
    if terminalTest(board) or count == depth:
        return utility(board, side)
    
    v = 100
    actions = nextMoves(board, side)
    
    for a in actions:
        tboard = a[0]
        tside = a[1]
        
        #print(maxValue(tboard, tside, alpha, beta, count+1, depth))
        if side != tside:
            v = min(v, maxValue(tboard, tside, alpha, beta, count+1, depth)[0])
        else:
            v = min(v, minValue(tboard, tside, alpha, beta, count+1, depth))
            
        #debug
        #print(str(count) + ':')
        #print('pos: ' + str(a[2]))
        #print('v: ' + str(v))
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
    
    move = alphaBetaSearch(board, side, 8)[2]
            
    return move
        
    