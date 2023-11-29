from board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.player = 'X'
    
    def makeMove(self, move):
        """
        This function purpose is make move
        """
        self.board.makeMove(move, self.player)
        self.player = 'O' if self.player == 'X' else 'X'
    
    def checkWinner(self):
        """
        This function purpose is check winner
        """
        return self.board.checkWinner()
    
    def checkDraw(self):
        """
        This function purpose is check draw
        """
        return self.board.checkDraw()
    
    def printBoard(self):
        """
        This function purpose is print game board
        """
        self.board.printBoard()
