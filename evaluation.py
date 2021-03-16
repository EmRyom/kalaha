from kalaha import traverse
from minimax import altJudge, random
from time import time

def evaluation(n):
    res=[]
    for depth in range(2,8):
        w=0
        d=0
        l=0
        start=time()
        for p in range(n):
            c=4
            board=[c,c,c,c,c,c,0,  c,c,c,c,c,c,0]
            side = True
            while(True):
                if sum(board[0:6])==0 or sum(board[7:13])==0:
                    board[6] += sum(board[0:6])
                    board[13] += sum(board[7:13])
                    u = board[6] - board[13]
                    if u>0:
                        w+=1
                    if u==0:
                        d+=1
                    if u<0:
                        l+=1
                    break
                if side:
                    i = altJudge(board,side,depth)
                    board,side = traverse(board,True,i-1)
                else:
                    i = random(board,side)
                    board,side = traverse(board,False,i+6)
            print(w,d,l,depth)
        res.append([w,d,l,depth,time()-start])
    print(res)

        
        