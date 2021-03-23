from kalaha import traverse


def terminalTest(board):
    
    return (sum(board[0:6])==0 or sum(board[7:13])==0)


def utility(board, player):
    if terminalTest(board):
        board[6] += sum(board[0:6])
        board[13] += sum(board[7:13])
    if player:
        return board[6]-board[13]
    else:
        return board[13]-board[6]


def maxValue(board, side, alpha, beta, count, depth, player): 
    
    # limiting depth    
    if terminalTest(board) or count == depth:
        return utility(board, player), None
    
    v = -100
    m = -100
    actions = nextMoves(board, side)
    # dummy statement
    final_action = actions[0]
    
    for a in actions:
       
        tboard = a[0]
        tside = a[1]
        
        if tside != side:
            v = max(v, minValue(tboard, tside, alpha, beta, count+1, depth, player))
        else:
            v = max(v, maxValue(tboard, tside, alpha, beta, count+1, depth, player)[0])
            
        if v >= beta:
            return v, None
        alpha = max(alpha, v)
        
        # storing best action
        if count == 0 and m<v:
            final_action = a
            m = v
        
        
    return v, final_action


def minValue(board, side, alpha, beta, count, depth, player):
    
    # limiting depth    
    if terminalTest(board) or count == depth:
        return utility(board, player)
    
    v = 100
    actions = nextMoves(board, side)
    
    for a in actions:
        
        tboard = a[0]
        tside = a[1]
        
        if side != tside:
            v = min(v, maxValue(tboard, tside, alpha, beta, count+1, depth, player)[0])
        else:
            v = min(v, minValue(tboard, tside, alpha, beta, count+1, depth, player))
            
        if v <= alpha:
            return v
        beta = min(beta, v)
    
    return v


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


def judge(board, side, depth):
    return (maxValue(board, side, -100, 100, 0, depth, side)[1])[2]
