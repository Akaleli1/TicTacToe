from exceptions import InvalidMove
from game import Game
from AI_player import ArtificialPlayer

f = open("tictactoe.txt", "w")

game = Game()
aiPlayer = ArtificialPlayer('O')
while True:
    try:
        move = int(input("Enter move: "))
        if move < 1 or move > 9:
            raise InvalidMove("Invalid move")
        game.makeMove(move)
        print("Your move: " + str(move))
        f.write('X:' + str(move) + ', ')
        game.printBoard()
        winner = game.checkWinner()
        if winner:
            print(f"{winner} is winner")
            f.close()
            with open('tictactoe.txt', 'rb+') as f: 
                f.seek(-2, 2) 
                f.truncate() 
            break
        if game.checkDraw():
            print("Draw")
            f.close()
            with open('tictactoe.txt', 'rb+') as f: 
                f.seek(-2, 2) 
                f.truncate() 
            break
        move = aiPlayer.get_move(game.board)
        game.makeMove(move)
        f.write('O:' + str(move) + ', ')
        print("AI move: " + str(move))
        game.printBoard()
        winner = game.checkWinner()
        if winner:
            print(f"{winner} is winner")
            f.close()
            with open('tictactoe.txt', 'rb+') as f: 
                f.seek(-2, 2) 
                f.truncate() 
            break
        if game.checkDraw():
            print("Draw")
            f.close()
            with open('tictactoe.txt', 'rb+') as f: 
                f.seek(-2, 2) 
                f.truncate() 
            break
        
    except InvalidMove as e:
        print(e)
    except ValueError:
        print("Invalid move")
