#constants
PIECE_X = 'X'
PIECE_O = 'O'

EMPTY_CELL = ' '

#variable
game_board = [
  [' ', ' ', ' '],
  [' ', ' ', ' '],
  [' ', ' ', ' ']
]


def print_board():
  for i in range(3):
    for j in range(3):
      print("[" + game_board[i][j] +"]", end="")#print elements without new line
    print()#print empty line after each row
  print('--------------')

def invalid(errorcode):
  if errorcode == 1:
    print('username cannot start with a password')
  if errorcode == 2:
    print('username contains invalid character')
  if errorcode == 3:
    print('username length must be between 3 and 12')
  
  
def user_name_validation(username):
  numbers = '0123456789'
  allowed_chars = set('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-')
  if username[0] not in numbers:
    if len(username) >= 3 and len(username) <= 12:
      for chars in username:
        validation = set((username))
        if validation.issubset(allowed_chars):
          return username
        else:
          return invalid(2)
    else:
      return invalid(3)
  else:
    return invalid(1)


def get_username():  
  player1_name = input('Player1 Enter username: ')
  player1_validated = user_name_validation(player1_name) 
  
  while player1_name != player1_validated:
    player1_name = input('Player1 Enter username: ')
    player1_validated = user_name_validation(player1_name) 
  
  player2_name = input('Player2 Enter username: ')
  player2_valitated = user_name_validation(player2_name) 
  
  while player2_name != player2_valitated:
    player2_name = input('Player2 Enter username: ')
    player2_valitated = user_name_validation(player2_name)

  return (player1_validated,player2_valitated)
  
  

def game_play(player, x, y):
  if game_board[x][y] == EMPTY_CELL: #check if position empty
    game_board[x][y] = player
    print_board()
  else:
    print("Position is not empty, you loose a turn")

def game_winner():
  for row in game_board: #each row separately
    #check all rows first
    if row[0] != ' ' and row[0] == row[1] == row[2]: #If all the items in row are the same
      return row[0] #X or O
  
  for i in range(3): #check all columns 
      if game_board[0][i]!= ' ' and game_board[0][i] == game_board[1][i] == game_board [2][i]: 
        return game_board[0][i]  
        
  #check cross items
  if game_board[0][0] ==  game_board[1][1] ==  game_board[2][2] != EMPTY_CELL:
    if game_board [0][0] == 'X':
      return "X"
    else:
      return "O"
  
  if game_board[2][0] ==  game_board[1][1] ==  game_board[0][2] != EMPTY_CELL:
    if game_board [2][0] == 'X':
      return "X"
    else:
      return "O"
      
def game_draw():
  for i in range(3):
    for j in range(3):
      if game_board[i][j] == ' ':
        return False
  return True

def user_pieces(player1_name,player2_name):
  PIECE_X = 'X'
  PIECE_O = 'O'
  player1_piece = input(f"{player1_name}, Choose 'X' or 'O': ").upper()
  if player1_piece == PIECE_X:
    player2_piece = PIECE_O
  else:
    player1_piece = PIECE_O
    player2_piece = PIECE_X
    
  return {player1_piece:player1_name,player2_piece:player2_name }


def create_game_history(game_result):
  with open("game_history.txt", mode='a', encoding = 'utf-8') as myfile:
    myfile.write(f"{game_result}\n")

def print_record():
  with open("game_history.txt",mode='r', encoding = 'utf-8') as myfile:
    records = myfile.readlines()
    for lines in records:
      print(lines)

def player_record(player_username):
  user_game_history = []
  with open("game_history.txt", mode='r', encoding = 'utf-8') as myfile:
    for lines in myfile:
      if player_username in lines:
        user_game_history.append(lines)
    return user_game_history

#clears board for new game
def clear_board():
  for i in range(3):
    for j in range(3):
      game_board[i][j]= ' '