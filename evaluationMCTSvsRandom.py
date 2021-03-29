from kalaha import traverse
from minimax import judge
from alt import random, southGreedy
import mctsAlg

def makeMctsAIChoice(board, side):
    theNode = mctsAlg.Node(board) 
    algoInstance = mctsAlg.MCTS(board,0,theNode, 200)
    indexToChoose = algoInstance.iterateAndChoose(20, theNode)
    #done due to parameter specification that is passed to 'traverse' function in evaluation
    return (indexToChoose+7)+6


def evaluation(n):
    res=[]
    w=0
    d=0
    l=0
    print("win,draw,loss")
    for p in range(n):
        c=4
        board=[c,c,c,c,c,c,0,  c,c,c,c,c,c,0]
        side = True
        if p>=n/2:
            side = False
        while(True):
            if sum(board[0:6])==0 or sum(board[7:13])==0:
                board[6] += sum(board[0:6])
                board[13] += sum(board[7:13])
                u = board[6] - board[13]
                if u>0:
                    l+=1
                if u==0:
                    d+=1
                if u<0:
                    w+=1
                break
            if side:
                i = random(board,side)
                board,side = traverse(board,True,i-1)
            else:
                i = makeMctsAIChoice(board,side)
                board,side = traverse(board,False,i-6)
        print(w,d,l)        
    print(w,d,l)
    

evaluation(100)