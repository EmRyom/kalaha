
def traverse(board,side,pos):
    stack = board[pos]
    board[pos] = 0
    
    if stack==0:          
        return board,side 
    
    while(stack!=0): 
        if (pos+1 > 13):  # Move
            pos=0
        else:
            pos+=1
        
        if pos==6 and side==0: # To skip the opponents goal
            continue
        if pos==13 and side==1:
            continue
        
        board[pos]+=1
        stack-=1
    
    # 'Stealing' rule implimentation
    if board[pos]==1 and (not pos==6) and (not pos==13) and board[12-pos]>0 :
        if side and pos in range(0,6):
                board[6]+=board[12-pos]+1
                board[12-(pos)]=0
                board[pos]=0
        if not side and pos in range(7,13):
                board[13]+=board[12-pos]+1
                board[12-pos]=0
                board[pos]=0
        
    if (side and pos==6) or (not side and pos==13): # Players get another turn 
        return board, side                          # if it ends in their goal
    else:
        return board, not side
    
   