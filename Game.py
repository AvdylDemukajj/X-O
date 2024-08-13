from Gameboard import Gameboard

class Game():
    def game_start(self):
        self.controllBoard = Gameboard()
        self.game_board = self.controllBoard.gameBoard
        self.playerOne = 'O'
        self.playerTwo = 'X'
        print('Welcome to X-O Game')
        print("Please enter player one's name: ")
        self.player_one = input(' : ')
        print("Please enter player two's name: ")
        self.player_two = input(' : ')
        print("Here is the game board, each place is represented by 1-9, starting from the left column each time and moving along the row")
        self.controllBoard.printBoard(self.game_board)
        self.turn = 1

    def game_end(self):
        if self.game_running == False:
            replay = input('Press 0 to quit the game and 1 to play again!')
            try:
                if int(replay):
                    self.game_running = True
                    self.game_start()
            except ValueError:
                print('Invalid input. Please enter 0 or 1.')
                self.game_end()
    
    def takeTurn(self, user, item):
        print(user + ' choose a place, 1-9')
        try:
            position = int(input(': '))
            if position > 9 or position < 1:
                raise ValueError
            
        except ValueError:
            print('Invalid input. Please enter a number between 1 and 9.')
            return self.takeTurn(user, item)
        
        if self.controllBoard.is_place_taken(self.game_board, position):
            print('This place is already taken. Please choose another one.')
            return self.takeTurn(user, item)
        else:
            self.controllBoard.set_items(item, position, self.game_board)
            self.controllBoard.printBoard(self.game_board)
            if self.controllBoard.is_game_won(self.game_board):
                print(user + ' wins!')
                self.game_running = False

    def main(self):
        self.game_running = True
        self.game_start()
        while self.game_running:
            if self.turn % 2 != 0:
                self.takeTurn(self.player_one, 'O')
            else:
                self.takeTurn(self.player_two, 'X')
            
            if self.controllBoard.is_board_full(self.game_board):
                print('It\'s a tie!! You both lose!')
                self.game_running = False
            self.turn += 1

            if not self.game_running:
                self.game_end()

if __name__ == '__main__':
    Game().main()
