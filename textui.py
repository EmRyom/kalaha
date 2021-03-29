from termcolor import colored
from sys import exit
from minimax import judge
from alt import random
from kalaha import traverse
import mctsAlg

def makeMctsAIChoice(board, side):
    theNode = mctsAlg.Node(board) 
    algoInstance = mctsAlg.MCTS(board,0,theNode, 200)
    indexToChoose = algoInstance.iterateAndChoose(20, theNode)
    #done due to parameter specification that is passed to 'traverse' function in evaluation
    return indexToChoose+1

def showBoard(board):
    print(colored("6   5   4   3   2   1",'red'),'\n')
    print('   '.join(str(e) for e in list(reversed(board[0:6]))))
    n=str(board[6])
    s=str(board[13])
    print(n," "*(19-len(n)-len(s)),s)
    print('   '.join(str(e) for e in board[7:13]),'\n')
    print(colored("1   2   3   4   5   6",'cyan'),"\n")
    
  
def userInput():
    while(True):
        try:
            i = input()
            if i=="'":
                exit()
            i = int(i)
            if i>0 and i<7:
                return i
            int("'")
        except ValueError:
            print("Please enter an integer from 1 to 6")

def aiInput(board,side):
    if side:         
        print("yes")
        choice = judge(board,side,6) # 6 = depth of minimax 
    else:
        choice = random(board,side)
    print("AI:",choice,end="")
    if input()=="'": exit()
    return choice

def gameOver(board):
    board[6] += sum(board[0:6])
    board[13] += sum(board[7:13])
    board[0:6] = [0,0,0,0,0,0]
    board[7:13] = [0,0,0,0,0,0]
    showBoard(board)
    print("Game over")
    if board[6] > board[13]:
        print("North wins")
    if board[6] < board[13]:
        print("South wins")
    if board[6] == board[13]:
        print("Draw")
    return board[6] - board[13]


print("\n\n\nStart!\n")

c=4                                     # Amount of stones per house
#     [4,4,4,4,4,4,0,  4,4,4,4,4,4,0]     
board=[c,c,c,c,c,c,0,  c,c,c,c,c,c,0]   # Initial state
#      N houses    ^   S houses    ^ 
#                goal            goal

# Starting player (True : North)
side = True                            
# AI switch for North (minimax)
aiN = False                                 
# AI switch for South (random)
aiS = True        
# switch to choose the algorithm. TRUE = Minimax, FALSE = MCTS. 
# MCTS is active only for South player
algorithm = True                        

while(True):
    if sum(board[0:6])==0 or sum(board[7:13])==0:
        gameOver(board)
        break
    showBoard(board)
    if side:
        print(colored("North","red"),"players turn")
        if aiN:
            i = aiInput(board,True)
        else:
            i = userInput()
        board,side = traverse(board,True,i-1)
    else:
        print(colored("South","cyan"),"players turn")
        if aiS:
            if algorithm:
                i = aiInput(board,False)
            else:
                i = makeMctsAIChoice(board,side)
        else:
            i = userInput()
        board,side = traverse(board,False,i+6)

    
    