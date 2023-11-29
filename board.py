from exceptions import InvalidMove

class Board:
    def __init__(self):
        self.xCoordinates = list()
        self.oCoordinates = list()
    
    def checkCoordinate(self, newMove):
        """
        This function purpose is prevent duplication
        Firstly looking at X and O coordinates
        Second checking X and O coordinates then return False
        Third return True
        """
        if len(self.xCoordinates) and len(self.oCoordinates) == 0:
            return True
        for move in self.xCoordinates: # loop in player X's coordinates
            if move == newMove:        # if newMove already exists in game board then return False
                return False
        for move in self.oCoordinates: # loop in player O's coordinates
            if move == newMove:        # if newMove already exists in game board then return False
                return False
        return True
    
    def makeMove(self, move, player):
        result = self.checkCoordinate(move)
        if result:
            if player == 'X':
                self.xCoordinates.append(move)
            else:
                self.oCoordinates.append(move)
        else:
            raise InvalidMove("Invalid move")
    
    def checkWinner(self):
        """
        This function purpose is check winner
        """
        if len(self.xCoordinates) < 3 and len(self.oCoordinates) < 3:
            return None
        if len(self.xCoordinates) >= 3:
            # check horizantal
            if 1 in self.xCoordinates and 2 in self.xCoordinates and 3 in self.xCoordinates:
                return 'X'
            if 4 in self.xCoordinates and 5 in self.xCoordinates and 6 in self.xCoordinates:
                return 'X'
            if 7 in self.xCoordinates and 8 in self.xCoordinates and 9 in self.xCoordinates:
                return 'X'
            # check vertical
            if 1 in self.xCoordinates and 4 in self.xCoordinates and 7 in self.xCoordinates:
                return 'X'
            if 2 in self.xCoordinates and 5 in self.xCoordinates and 8 in self.xCoordinates:
                return 'X'
            if 3 in self.xCoordinates and 6 in self.xCoordinates and 9 in self.xCoordinates:
                return 'X'
            # check diagonal
            if 1 in self.xCoordinates and 5 in self.xCoordinates and 9 in self.xCoordinates:
                return 'X'
            if 3 in self.xCoordinates and 5 in self.xCoordinates and 7 in self.xCoordinates:
                return 'X'
        if len(self.oCoordinates) >= 3:
            # check horizantal
            if 1 in self.oCoordinates and 2 in self.oCoordinates and 3 in self.oCoordinates:
                return 'O'
            if 4 in self.oCoordinates and 5 in self.oCoordinates and 6 in self.oCoordinates:
                return 'O'
            if 7 in self.oCoordinates and 8 in self.oCoordinates and 9 in self.oCoordinates:
                return 'O'
            # check vertical
            if 1 in self.oCoordinates and 4 in self.oCoordinates and 7 in self.oCoordinates:
                return 'O'
            if 2 in self.oCoordinates and 5 in self.oCoordinates and 8 in self.oCoordinates:
                return 'O'
            if 3 in self.oCoordinates and 6 in self.oCoordinates and 9 in self.oCoordinates:
                return 'O'
            # check diagonal
            if 1 in self.oCoordinates and 5 in self.oCoordinates and 9 in self.oCoordinates:
                return 'O'
            if 3 in self.oCoordinates and 5 in self.oCoordinates and 7 in self.oCoordinates:
                return 'O'
        return None
    
    def checkDraw(self):
        """
        This function purpose is check draw
        """
        if len(self.xCoordinates) + len(self.oCoordinates) == 9:
            return True
        return False

    def printBoard(self):
        """
        This function purpose is print game board
        """
        print('\n')

        for i in range(1, 10):
            # add line break after 3rd column
            # add a line after 3rd row
            if i % 3 == 0:
                if i in self.xCoordinates:
                    print('X')
                elif i in self.oCoordinates:
                    print('O')
                else:
                    print(i)
                if i != 9:
                    print('---------')
            else:
                if i in self.xCoordinates:
                    print('X', end=' | ')
                elif i in self.oCoordinates:
                    print('O', end=' | ')
                else:
                    print(i, end=' | ')
        print('\n')
    
    def get_possible_moves(self):
        """
        This function purpose is get possible moves
        """
        possible_moves = list()
        for i in range(1, 10):
            if i not in self.xCoordinates and i not in self.oCoordinates:
                possible_moves.append(i)
        return possible_moves