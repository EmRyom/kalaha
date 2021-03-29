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


def evaluation(n,nd,sd):
    res=[]
    #for nd in range(1,7):
    w=0
    d=0
    l=0
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
                    w+=1
                if u==0:
                    d+=1
                if u<0:
                    l+=1
                break
            if side:
                i = judge(board,side,nd)
                board,side = traverse(board,True,i-1)
            else:
                i = makeMctsAIChoice(board, side)
                #i = random(board,side)
                board,side = traverse(board,False,i-6)
        print(w,d,l)        
    print(w,d,l,nd,sd)
    
    
"""if w>l:
        res.append(['n',nd,sd])
    if w<l:
        res.append(['o',nd,sd])
    if w==l:
        res.append(['s',nd,sd])
        return -1
        
M=[]
for i in range(6):
    for nd in range(1,6):
        M.append(evaluation(4,nd+i,nd))
        print(M)"""
        
'''
rand 
wins, draws, losses, depth, time (s)
[983, 6, 11, 2, 3.424082040786743]
[982, 6, 12, 3, 11.545182466506958]
[990, 2, 8, 4, 40.22028565406799]
[986, 3, 11, 5, 109.28872013092041]
[997, 1, 2, 6, 322.5370743274689]
[999, 0, 1, 7, 1015.6422221660614]
rand
[95, 3, 2, 1, 0.10169053077697754]
[100, 0, 0, 2, 0.31415772438049316]
[97, 0, 3, 3, 1.036454677581787]
[100, 0, 0, 4, 2.836799383163452]
[99, 1, 0, 5, 8.898838758468628]
[98, 1, 1, 6, 29.45132279396057]
[98, 1, 1, 7, 83.96475315093994]


[97, 1, 2, 1, 0.1878662109375]
[100, 0, 0, 2, 0.40976548194885254]
[99, 0, 1, 3, 1.109595537185669]
[100, 0, 0, 4, 3.4211645126342773]
[100, 0, 0, 5, 10.268865585327148]
[100, 0, 0, 6, 33.9164559841156]


proper tests: 

evaluation(100,1,1)
50 0 50 1 1

evaluation(100,2,2)
50 0 50 2 2

evaluation(100,3,3)
50 0 50 3 3

evaluation(100,4,4)
50 0 50 4 4



evaluation(100,1,2)
0 0 100 1 2

evaluation(100,2,3)
50 0 50 2 3

evaluation(100,3,4)
50 50 0 3 4

evaluation(100,4,5)
50 0 50 4 5

evaluation(100,5,6)
50 0 50 5 6


evaluation(100,1,3)
0 0 100 1 3

evaluation(100,2,4)
0 0 100 2 4

evaluation(100,3,5)
0 0 100 3 5

evaluation(100,4,6)
50 0 50 4 6

evaluation(100,5,7)
50 0 50 5 7


evaluation(100,1,4)
0 0 100 1 4

evaluation(100,2,5)
0 0 100 2 5

evaluation(100,3,6)
0 0 100 3 6

evaluation(100,4,7)
0 0 100 4 7

evaluation(100,5,8)
50 0 50 5 8


evaluation(2,1,5)
0 0 2 1 5

evaluation(2,2,6)
0 0 2 2 6

evaluation(2,3,7)
1 0 1 3 7

evaluation(2,4,8)
0 0 2 4 8

evaluation(2,5,9)
1 0 1 5 9


evaluation(2,1,6)
0 0 2 1 6

evaluation(2,2,7)
0 0 2 2 7

evaluation(2,3,8)
0 0 2 3 8

evaluation(2,4,9)
0 0 2 4 9

evaluation(2,5,10)
1 0 1 5 10


against random :
evaluation(1000,1,0)
942 11 47 1 0

evaluation(1000,2,0)
980 2 18 2 0

evaluation(1000,3,0)
980 2 18 3 0
    
evaluation(1000,4,0)
989 5 6 4 0

evaluation(1000,5,0)
994 2 4 5 0

evaluation(1000,6,0)
993 1 6 6 0
'''

        
        