from functions import print_board, user_name_validation, get_username, game_play, game_board, game_winner, game_draw, create_game_history, print_record, clear_board, player_record,user_pieces

PIECE_X = 'X'
PIECE_O = 'O'

print('welcome to Tic Tac Toe')

#game menu
menu = ['New Game', 'Game History', 'Player Record', 'Exit']

while True:
  for (i, choice) in enumerate(menu):
    print(f'{i+1}. {choice}')
  
  player_menu_choice = input('pick a number from the menu: ')
  if player_menu_choice.isdigit():
    validated_player_menu_choice = int(player_menu_choice)
    if validated_player_menu_choice >= 1 and validated_player_menu_choice <= 4:

      if validated_player_menu_choice == 1:
        
        # gets username
        usernames = get_username()
        player1_name = usernames[0]
        player2_name = usernames[1]
        
        #gets userpiece
        pieces = user_pieces(player1_name,player2_name)
        piece = list(pieces.keys())
        player1_piece = piece[0]
        player2_piece = piece[1]

        print("----------------------")
        print("Welcome to Tic Tac Toe")

        print("Lets start!\n")
        print_board()
             
          
        while True:
      
          #get player X position
          player_x_position = input(f'{player1_name}, Enter play position (i.e. 0,1): ')
          
          pos_x = int(player_x_position.split(',')[0])
          pos_y = int(player_x_position.split(',')[1])
          
          game_play('X', pos_x,pos_y)

          #check for win or draw after every move
          if(game_winner()):
            print(f"{pieces['X']} Wins, {pieces['O']} Looses")
            result = f"{pieces['X']} Won against {pieces['O']}"
            create_game_history(result)
            break;
          elif game_draw():
            print(f"{pieces['X']} vs {pieces['O']}: DRAW")
            result = f"{pieces['X']} vs {pieces['O']}: DRAW"
            create_game_history(result)
            break
        
           #get player O position
          #another shorter way to get the input
          pos_x,pos_y = input(f'{player2_name}, Enter play position (i.e. 0,1): ').split(',')
          
          game_play('O', int(pos_x),int(pos_y))

          #check for win or draw after every move
          if(game_winner()):
            print(f"{pieces['O']} Wins, {pieces['X']} Looses")
            result = f"{pieces['O']} Won against {pieces['X']}"
            create_game_history(result)
            break
      
          elif game_draw():
            print(f"{pieces['O']} vs {pieces['X']}: DRAW")
            result = f"{pieces['O']} vs {pieces['X']}: DRAW"
            create_game_history(result)
            break

        play_again = int(input('Enter 1 to view menu or 2 to exit: '))
  
        if play_again == 1:
          clear_board()
        else:
          exit("Goodbye")

      elif validated_player_menu_choice == 2:
        print('-----------------------------')
        print_record()

      elif validated_player_menu_choice == 3:
        print('-----------------------------')
        check_record_name = input("Enter player name to view player record: ")  
        check_records = player_record(check_record_name)
        for user_record in check_records:
          print('-----------------------------')
          print(user_record)

      elif validated_player_menu_choice == 4:
        exit("Goodbye")
      
    else:
      print('enter a number between 1 amd 4')
  else:
    print('enter an integer')

    
  

  

  
