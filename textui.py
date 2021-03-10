from termcolor import colored
from sys import exit
from minimax import judge
from kalaha import traverse

#board = [4,4,4,4,4,4,0,  4,4,4,4,4,4,0]
#         N houses    ^   S houses    ^ 
#                   goal            goal

def showBoard(board):
    print(colored("6   5   4   3   2   1",'red'),'\n')
    print('   '.join(str(e) for e in list(reversed(board[0:6]))))
    print(board[6],"                 ",board[13])
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
side = True
aiN = True
aiS = True

while(True):
    if sum(board[0:6])==0 or sum(board[7:13])==0:
        gameOver(board)
        break
    showBoard(board)
    if side:
        print(colored("North","red"),"players turn")
        if aiN:
            choice = judge(board,True)
            print("\nAI:",(choice),end='')
            #if input()=="'":
            #    exit()
            board,side = traverse(board,1,choice-1)
        else:
            board,side = traverse(board,1,userInput()-1)
    else:
        print(colored("South","cyan"),"players turn")
        if aiS:
            choice = judge(board,False)
            print("\nAI:",(choice),end='')
            #if input()=="'":
            #    exit()
            board,side = traverse(board,0,choice+6)
        else:
            board,side = traverse(board,0,userInput()+6)
    
    