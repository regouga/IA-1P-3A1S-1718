
####################################################################################################
#																								   #
# 									  Inteligencia Artificial									   #
# 								  Projeto - Entrega 1 - 2017-2018								   #
# 					   Grupo 44 - Mariana Mendes, 83521 - Miguel Regouga, 83530					   #
#																								   #
####################################################################################################

import copy
from search import *
from utils import *



####################################################################################################
# 											  TAI Color											   #
####################################################################################################

# sem cor = 0
# com cor > 0

def get_no_color():
       return 0


def no_color (c):
       return c==0


def color (c):
       return c > 0



####################################################################################################
# 											  TAI Pos											   #
####################################################################################################

# Tuplo (l, c)

def  make_pos (l, c):
       return (l, c)


def pos_l (pos):
       return pos[0]


def pos_c (pos):
       return pos[1]




####################################################################################################
# 											  TAI Group											   #
####################################################################################################

def make_group():
       return []


def add_element(group, pos):
       group.append(pos)
       return group


def remove_element(group, pos):
       group.remove(pos)
       return group


def get_element(group, index):
       return group[index]





####################################################################################################
# 											  TAI Board											   #
####################################################################################################

def print_board(board): 					# Impressao do tabuleiro
       for row in board:
              for elem in row:
                     print(elem, end=' ')
              print()  


def make_copy(board): 						# Copia do tabuleiro
       new_board = copy.deepcopy(board)
       return new_board


def get_line(board, line):					# Obtencao de uma linha do tabuleiro
       return board[line]


def get_color_by_board(board, pos):			# Obtencao da cor de uma posicao de um tabuleiro
       line = pos_l(pos)
       collumn = pos_c(pos)
       return board[line][collumn]

                       
def get_color(line, collumn):				# Obtencao da cor de uma posicao de uma linha
       return line[collumn]


def change_color(board, pos, color):		# Alteracao da cor de um elemento do tabuleiro
       line = pos_l(pos)
       collumn = pos_c(pos)       
       board[line][collumn] = color
       return board


def remove(board, group):					# Remocao de um elemento do tabuleiro
       for i in range(0, len(group)):
              pos = get_element(group, i)
              board = change_color(board, pos, 0)
       return board


def get_collumn(board, collumn):			# Obtencao de uma coluna
       col = []
       for line in board:
              col.append(line[collumn])
       return col


def number_collumns(board): 				# Numero de colunas do tabuleiro
       return len(board[0])


def number_lines(board): 					# Numero de linhas do tabuleiro
       return len(board)


def has_zeros(listAnnalise): 				# Verificacao se tem zeros
       for color in listAnnalise:
              if color == 0:
                     return True
       return False


def has_only_zeros(listAnnalise): 			# Verificacao se so tem zeros
       for color in listAnnalise:
              if color != 0:
                     return False
       return True     




####################################################################################################
#																								   #
# 										  Funcoes auxiliares									   #
#																								   #
####################################################################################################

def compacta(obj, prev):
       lengh = len(obj)
       aux = 0
       i = 1
       flag = 0
       while(i <= lengh):
              if no_color(obj[-i]):
                     aux +=1
                     flag = 1
              else:
                     if flag:
                            color = obj[-i]
                            obj[-i + aux] = color
                            obj[-i] = 0
                     
              i+=1
       return obj


def update_collumn(board, collumn, col_index):	# Compatcacao vertical
       nLines = number_lines(board)
       for line in range(0, nLines):
              board[line][col_index] = collumn[line] 
       return board


def compactV(board):							# Compatcacao vertical
       nCollumns = number_collumns(board)
       for i in range(0, nCollumns):
              collumn = get_collumn(board, i)
              if (has_zeros(collumn)):
                     collumn = compacta(collumn, 0)
                     board = update_collumn(board, collumn, i)

       return board


def invert(obj):								# Inversao de uma lista
       aux = 0
       for i in range(0, len(obj)):
              if obj[i] != 0:
                     obj[aux] = obj[i]
                     aux += 1
                     obj[i] = 0
       return obj


def update_line(board, line, line_index):		# Atualizacao de uma linha do tabuleiro
       board[line_index] = line
       return board


def compactH(board, empty_col): 				# Compatcacao horizontal
       nCollumns = number_collumns(board)
       newBoardCollumn = []
       nLines = number_lines(board)
       auxCol = [0]*nLines
       aux = 0
       for i in range(0, nCollumns):
              col = get_collumn(board, i)
              if has_only_zeros(col):
                     aux +=1
              else:
                     newBoardCollumn.append(col)        
       for i in range(0,aux):
              newBoardCollumn.append(auxCol)
       newFinal = []
       for l in range(0, nLines):
              line =[]
              for c in range(0, nCollumns):
                     line.append(newBoardCollumn[c][l])
              newFinal.append(line)
       return newFinal


def col_empty(board):							# Verificacao de uma coluna que so tem zeros (vazia)
       flag = 0
       nCollumns = number_collumns(board)
       for i in range(0, nCollumns):
              collumn = get_collumn(board, i)
              if (has_only_zeros(collumn)):
                     return True, i
       return False, -1


def verifica(board, color, pos, group): 		# Analise de cores do tabuleiro
       posVector = []
       nLines = number_lines(board)
       nCollumns = number_collumns(board)
       L = pos_l(pos)
       col = pos_c(pos)
       colorAnalise = get_color_by_board(board, pos)
       if(colorAnalise == color):
              group.append(pos)
              new_board = change_color(board, pos, get_no_color())
              if (col == nCollumns-1):
                     if(L == 0):
                            #analisa canto superior direito
                            posVector.append(make_pos(L, col-1))
                            posVector.append(make_pos(L+1, col))
                            
                     elif(L == nLines -1):
                            #analisa canto inferior direito
                            posVector.append(make_pos(L, col-1))
                            posVector.append(make_pos(L-1, col))                            
                     else:
                            #analisa ultima coluna da direita
                            posVector.append(make_pos(L, col-1))
                            posVector.append(make_pos(L+1, col)) 
                            posVector.append(make_pos(L-1, col)) 
              
              elif(col == 0):
                     if(L == 0):
                            #analisa canto superior esquerdo
                            posVector.append(make_pos(L, col+1))
                            posVector.append(make_pos(L+1, col))                            
                     elif(L == nLines -1):
                            #analisa canto inferior esquerdo
                            posVector.append(make_pos(L, col+1))
                            posVector.append(make_pos(L-1, col))                            
                     else:
                            #analisa primeira coluna da esquerda
                            posVector.append(make_pos(L, col+1))
                            posVector.append(make_pos(L+1, col)) 
                            posVector.append(make_pos(L-1, col))                            
              elif(L == 0):
                     #analisa primeira linha
                     posVector.append(make_pos(L+1, col))
                     posVector.append(make_pos(L, col+1)) 
                     posVector.append(make_pos(L, col-1))                     
              elif(L == nLines -1):
                     #analisa ultima linha
                     posVector.append(make_pos(L-1, col))
                     posVector.append(make_pos(L, col+1)) 
                     posVector.append(make_pos(L, col-1))                       
              else:
                     # analisa interior do tabuleiro
                     posVector.append(make_pos(L-1, col))
                     posVector.append(make_pos(L+1, col)) 
                     posVector.append(make_pos(L, col-1))  
                     posVector.append(make_pos(L, col+1))                       
                     
              for pos in posVector:
                     c = get_color_by_board(board, pos)
                     if c != get_no_color():
                            verifica(new_board, color, pos, group) 
              
              return group
       else:
              return group
             

def getNumberOfZeros(board):
       zeros = 0
       nLines = number_lines(board)
       nCollumns = number_collumns(board)
       for i in range(0, nLines):
              for j in range(0, nCollumns):
                     if get_color_by_board(board, make_pos(i, j)) == get_no_color():
                            zeros += 1
       return zeros

####################################################################################################
#																								   #
# 									Funcao board_find_groups									   #
#																								   #
####################################################################################################

def board_find_groups(board):
       groups = []
       new = make_copy(board)
       nLines = number_lines(board)
       nCollumns = number_collumns(board)
       for i in range(0, nLines):
              for j in range(0, nCollumns):
                     pos = make_pos(i, j)
                     c = get_color_by_board(new, pos) 
                     if c != get_no_color():
                            groups.append(verifica (new, c, pos, []))
       return groups 
       




####################################################################################################
#																								   #
# 									Funcao board_remove_group									   #
#																								   #
####################################################################################################

def board_remove_group(board, group):
       new_board = make_copy(board)
       new_board = remove(new_board, group)
       new_board = compactV(new_board)
       logic, col = col_empty(new_board)
       if(logic):
              new_board = compactH(new_board, col)                
       return new_board





####################################################################################################
#																								   #
# 									  	 Classe sg_state										   #
#																								   #
####################################################################################################

class sg_state:
       
       def __init__(self, board):
              self.board = board
       
       def __lt__(self, other_state):
              selfZeros = getNumberOfZeros(self.board)
              otherStateZeros = getNumberOfZeros(other_state.board)
              return selfZeros > otherStateZeros




####################################################################################################
#																								   #
# 									  	 Classe same_game										   #
#																								   #
####################################################################################################

class same_game(Problem):
       
       def __init__(self, board):
              # init
              super().__init__(sg_state(board), [])
              
       def actions(self, state):
              # actions
              groups = board_find_groups(state.board)
              moves = []
              for group in groups:
                     if len(group) > 1:
                            moves.append(group)
              return moves
              
       def result (self, state, action):
              #result
              return sg_state(board_remove_group(state.board, action))
       
              
       def goal_test(self, state):
              return board_find_groups(state.board) == self.goal

              
       def h(self, node):
              return len(board_find_groups(node.state.board))
