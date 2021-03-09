# https://www.mathplayground.com/mancala.html
from termcolor import colored
import sys

#board = [4,4,4,4,4,4,0,  4,4,4,4,4,4,0]
#         N houses    ^   S houses    ^ 

def showBoard(board):
    print(colored("6   5   4   3   2   1",'red'),'\n')
    print('   '.join(str(e) for e in list(reversed(board[0:6]))))
    print(board[6],"                 ",board[13])
    print('   '.join(str(e) for e in board[7:13]),'\n')
    print(colored("1   2   3   4   5   6",'cyan'),"\n")
    

def move(pos):
    if (pos+1 > 13):
        return 0
    else:
        return pos+1

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


def gameOver(board):
    board[6] += sum(board[0:6])
    board[13] += sum(board[7:13])
    board[0:6] = [0,0,0,0,0,0]
    board[7:13] = [0,0,0,0,0,0]
    showBoard(board)
    print("Game over")
    if board[6] > board[13]:
        print("North wins")
        return 1
    if board[6] < board[13]:
        print("South wins")
        return 0
    if board[6] == board[13]:
        print("Draw")
        return 2


print("\n\n\nStart!\n")

c=4
board=[c,c,c,c,c,c,0,  c,c,c,c,c,c,0]
side = 1

while(True):
    if sum(board[0:6])==0 or sum(board[7:13])==0:
        gameOver(board)
        break
    showBoard(board)
    if side:
        print(colored("North","red"),"players turn")
        board,side = traverse(board,1,userInput()-1)
    else:
        print(colored("South","cyan"),"players turn")
        board,side = traverse(board,0,userInput()+6)
    
    
