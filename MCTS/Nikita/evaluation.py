from time import time
from random import randrange
import mctsAlgRewrite
from time import time
from termcolor import colored
import sys

def traverse(board,side,pos):
    stack = board[pos]
    board[pos] = 0
    
    if stack==0:
        return board,side
    
    while(stack!=0):
        pos = move(pos)
        if pos==6 and side==0:
            continue
        if pos==13 and side==1:
            continue
        board[pos]+=1
        stack-=1
    
    if board[pos]==1 and (not pos==6) and not pos==13:
        if side and pos in range(0,6):
            board[6]+=board[12-pos]+1
            board[12-(pos)]=0
            board[pos]=0
        if not side and pos in range(7,13):
            board[13]+=board[12-pos]+1
            board[12-pos]=0
            board[pos]=0
        
    if (side and pos==6) or (not side and pos==13):
        return board, side
    
    return board, not side


def move(pos):
    if (pos+1 > 13):
        return 0
    else:
        return pos+1



def randomF(board,side):
    c=[]
    for pos in range(1,7):
        if board[pos-1]==0 and side:
            continue
        if board[pos+6]==0 and not side:
            continue
        c.append(pos)
    i = randrange(len(c))
    #print (c[i])
    return c[i]   


def makeAChoice(board, side):

    theNode = mctsAlgRewrite.Node(board) 
    algoInstance = mctsAlgRewrite.MCTS(board,0,theNode, 35)
    indexToChoose = algoInstance.iterateAndChoose(40, theNode)
    #print("1indexto choose: ", indexToChoose+1 ,"(",indexToChoose+7, ")")
    return indexToChoose+7
    #return userInput()+6

def showBoard(board):
    print("\n")
    print(colored("6   5   4   3   2   1",'cyan'),'\n')
    print('   '.join(str(e) for e in list(reversed(board[0:6]))))
    print(board[6],"                 ",board[13])
    print('   '.join(str(e) for e in board[7:13]),'\n')
    print(colored("1   2   3   4   5   6",'red'))

def evaluation(n):
    res=[]
    w=0
    d=0
    l=0
    start=time()
    for p in range(n):
        c=4
        board=[c,c,c,c,c,c,0,  c,c,c,c,c,c,0]
        side = True
        while(True):
            #showBoard(board)
            if sum(board[0:6])==0 or sum(board[7:13])==0:
                board[6] += sum(board[0:6])
                board[13] += sum(board[7:13])
                u = board[6] - board[13]
                if board[6] > board[13]:
                    l+=1
                if board[6] < board[13]:
                    w+=1
                if board[6] == board[13]:
                    d+=1
                    
                break
    
            if side:
                #print("NORTH TURN")
                i = randomF(board,1)
                board,side = traverse(board,True,i-1)
            #if north
            else:
                #print("South TURN")
                #i = userInput()
                i = makeAChoice(board,side)
                board,side = traverse(board,False,i)
        print(w,d,l)
    res.append([w,d,l,time()-start])
    print(res)
    
 
    
rangeN = 10
southWins = 0;
northWins = 0;

'''
def userInput():
    while(True):
        try:
            i = input()
            if i=="'":
                sys.exit()
            i = int(i)
            if i>0 and i<7:
                print("\n")
                return i
            int("'")
        except ValueError:
            print("Please enter an integer from 1 to 6")
'''

#startTime = datetime.now()

'''
#for x in range(rangeN):
print("Game started. Round ", x)
c=4
board=[c,c,c,c,c,c,0,  c,c,c,c,c,c,0]
side = 1
#print("x = ", x)
northWins, southWins = evaluation(board,side, northWins, southWins)
 
'''
evaluation(1000)
'''timeToCompile = (datetime.now() - startTime).total_seconds()
print("Finished in ",timeToCompile*1000,"ms,  == ",timeToCompile," sec")    
print("North ",northWins,"  -  ", southWins, " South")
print ("Draws: ", rangeN-northWins-southWins)

'''