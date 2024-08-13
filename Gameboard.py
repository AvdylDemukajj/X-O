class Gameboard():
    def __init__(self):
        self.game_bard = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
    
    def set_items(self, user, position, game_board):
        game_board[position] = user
        return game_board
    
    @property
    def gameBoard(self):
        return self.game_bard
    
    def clearboard(self):
        self.game_bard = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
    
    def is_place_taken(self, game_board, index):
        return game_board[index] != ' '
    
    def is_board_full(self, game_board):
        for i in range(1, 10):
            if game_board[i] == ' ':
                return False
        return True
    
    def is_game_won(self, game_board):
        winning_combinations = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
        for combination in winning_combinations:
            if game_board[combination[0]] == game_board[combination[1]] and game_board[combination[1]] == game_board[combination[2]] and game_board[combination[0]] != ' ':
                return True
        return False
    
    def printBoard(self, game_board):
        index = 0
        for row in range(1, 4):
            for col in range(1, 4):
                index += 1
                if col != 3:
                    print(game_board[index], end=' | ')
                else:
                    print(game_board[index])
            if row != 3:
                print('--+---+--')
