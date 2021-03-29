#WE ASSUME THAT COMPUTER IS ALWAYS SOUTH 
import math
from numpy import log as ln
from random import randrange
#from termcolor import colored




class MCTS:
    
    def __init__(self,board_param, side_param, currentNode_param, numOfSimulations_param=10):
            self.current_Node = currentNode_param
            self.currentBoard = board_param
            self.currentSide = side_param
            self.numOfSimulations = numOfSimulations_param

            
    def iterateAndChoose(self, numOfIterations, theNode):   
        while (numOfIterations > 0 ):
            wins, losts = self.flow(theNode)
            numOfIterations -=1
        bestANode, bestANodeIndex = self.chooseBestChildren(theNode)
        
        return bestANodeIndex
 
    
    
    
    def chooseBestChildren(self,nodeToExplore):
        i = 0       
        maxChildN = None;
        maxChildNindex = None;
        actionsFromCN = nodeToExplore.getActionsFromNode()
        
        for childN in actionsFromCN:  
            #if len(childN.getBoard()) > 0 :
            if maxChildN == None:
                maxChildN = childN
                maxChildNindex = i
            else:
                if childN.countUCB(nodeToExplore.getVisits()) > maxChildN.countUCB(nodeToExplore.getVisits()):
                   maxChildN = childN    
                   maxChildNindex = i  
            i += 1
           
        return maxChildN, maxChildNindex     
                      
            
            
        
    def flow(self, nodeToExplore):
        cWins,cTries = 0,0
        
        # IS NOT LEAF
        if not (nodeToExplore.isLeaf):          
            bestChildrenNode, bestChildrenNodeIndex = self.chooseBestChildren(nodeToExplore)
            recurCwins, recurCtries = self.flow(bestChildrenNode)
            nodeToExplore.updateScoreVisits(recurCwins, recurCtries)
            return recurCwins, recurCtries
            
        # IS LEAF
        else:
            #NODE HASN'T BEEN VISITED
            if (nodeToExplore.visits == 0):
                cWins,cTries = self.simulation(nodeToExplore.currBoard.copy(), nodeToExplore.getNextTurnTakenBy(), self.numOfSimulations)
                nodeToExplore.updateScoreVisits(cWins,cTries)
                return  cWins,cTries

            #NODE HAS ALREADY BEEN VISITED 
            else:
                if self.expand(nodeToExplore):
                    bestChildrenNodeE, bestChildrenNodeIndexE = self.chooseBestChildren(nodeToExplore)
                    recurCwins, recurCtries = self.flow(bestChildrenNodeE)
                    nodeToExplore.updateScoreVisits(recurCwins, recurCtries)
                    return recurCwins, recurCtries
                else:
                    nodeToExplore.updateScoreVisits(0, 1)
                    return 0, 1

                  
        
        
        
    

    def expand(self,currentNode):
        boardToGetChildrenFrom = currentNode.getBoard().copy()
        if self.boardHasAmove(boardToGetChildrenFrom):
           
            for i in range(0,6):
                if (boardToGetChildrenFrom[i+7] != 0):   
                    childActionBoard, side = self.traverse(boardToGetChildrenFrom.copy(),0,i+7) #(board, side, pos)
                    currentNode.actionsFromNode.append(Node(childActionBoard.copy(),0,0,currentNode.visits, not currentNode.getNextTurnTakenBy() ))
                else:
                    childActionBoard = boardToGetChildrenFrom
                    currentNode.actionsFromNode.append(Node(childActionBoard.copy(),-9999,0,currentNode.visits, not currentNode.getNextTurnTakenBy() ))
            
            currentNode.hasChildren = True
            currentNode.isLeaf = False
            return True
        
        else:
            
            return False
        
        
        
        
    def boardHasAmove(self, board):
        possible_move_amount = 0
        for i in range(0,6):
            if (board[i+7] != 0): 
                possible_move_amount +=1
        if possible_move_amount > 0:
            return True
        else:
            return False
         
        
    def randomF(self,board,side):
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
        
        
# ROLLOUT    
    def simulation(self,board=[4,4,4,4,4,4,0,  4,4,4,4,4,4,0], side=False, numOfSimulations=10):
        northWins = 0
        southWins = 0
        for x in range(numOfSimulations):
            northWins, southWins = self.PlayRandomGame(board.copy(), side, northWins, southWins)

        return southWins,numOfSimulations


        
    def showBoard(self, board):
        print("\n")
        print(("6   5   4   3   2   1",'cyan'),'\n')
        print('   '.join(str(e) for e in list(reversed(board[0:6]))))
        print(board[6],"                 ",board[13])
        print('   '.join(str(e) for e in board[7:13]),'\n')
        print(("1   2   3   4   5   6",'red'))
    
    def PlayRandomGame (self, board, side, northWins, southWins):
         while(True):
            if sum(board[0:6])==0 or sum(board[7:13])==0:
                board[6] += sum(board[0:6])
                board[13] += sum(board[7:13])
                #u = board[6] - board[13]
                if board[6] > board[13]:
                    northWins+=1
                if board[6] < board[13]:
                    southWins+=1    
                break
            if side:
                i = self.randomF(board,1)
                board,side = self.traverse(board,True,i-1)
            else:
                i = self.randomF(board,0)
                board,side = self.traverse(board,False,i+6) 
         return northWins, southWins                 
                
 
        
    def traverse(self,board,side,pos):
        stack = board[pos]
        boardVar = board
        
        boardVar[pos] = 0
        
        if stack==0:
            return boardVar,side
        
        while(stack!=0): # To skip the opponents goal
            pos = self.move(pos)
            if pos==6 and side==0:
                continue
            if pos==13 and side==1:
                continue
            boardVar[pos]+=1
            stack-=1
        
        if boardVar[pos]==1 and (not pos==6) and (not pos==13) and boardVar[12-pos]>0 :  # Stealing implimentation
            if side and pos in range(0,6):
                    boardVar[6]+=boardVar[12-pos]+1
                    boardVar[12-(pos)]=0
                    boardVar[pos]=0
            if not side and pos in range(7,13):
                    boardVar[13]+=boardVar[12-pos]+1
                    boardVar[12-pos]=0
                    boardVar[pos]=0
            
        if (side and pos==6) or (not side and pos==13): # Players get another turn 
             return boardVar, side                          # if it ends in their goal
        else:  
            return boardVar, not side    
        
  
    def move(self,pos):
        if (pos+1 > 13):
            return 0
        else:
            return pos+1
        
        

    def gameOver(self, board):
        board[6] += sum(board[0:6])
        board[13] += sum(board[7:13])
        board[0:6] = [0,0,0,0,0,0]
        board[7:13] = [0,0,0,0,0,0]
        #print("Game over")
        if board[6] > board[13]:
            #print("North wins")
            return 1
        if board[6] < board[13]:
            #print("South wins")
            return 0
        if board[6] == board[13]:
            #print("Draw")
            return 2    
  
    
# ROLLOUT END



class Node:
    
    def __init__(self, currBoard_param, score_param=0, visits_param=0, parentNodeVisits_param=0, nextTurnTakenBy_param = False ):
        self.score = score_param
        self.visits = visits_param
        self.currBoard = currBoard_param;
        self.actionsFromNode = [] 
        self.parentNodeVisits = parentNodeVisits_param
        self.nextTurnTakenBy  = nextTurnTakenBy_param  #1 TRUE North,    0 FALSE South
        
        self.isLeaf = True
        self.hasChildren = False     
        self.nextChildsBoard = None
           
    
    def updateScoreVisits(self, addScore, addVisits):
        self.score += addScore
        self.visits += addVisits

   
    def countUCB(self, parentVisits_param = 0):
        if (self.visits == 0):
            return 99999
        else:
            return self.score / self.visits + 2 * math.sqrt( ln(parentVisits_param) / self.visits ) 
         
    def getBoard(self):
        return self.currBoard
    
    def getScore(self):
        return self.score
    
    def getVisits(self):
        return self.visits
    
    def getParentNodeVisits(self):
        return self.parentNodeVisits
    
    def getActionsFromNode(self):
        return self.actionsFromNode
    
    def getNextTurnTakenBy(self):
        return self.nextTurnTakenBy 

 


    

