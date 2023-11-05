
# number of rows and number of columns
BOARD_SIZE = 3
# this is the reward of winning a game
REWARD = 10


class TicTacToe:

    def __init__(self, board):
        self.board = board
        self.player = 'O'
        self.computer = 'X'

    def run(self):
        print("Computer starts...")

        while True:
            self.move_computer()
            self.move_player()

    def print_board(self):
        print(self.board[1] + '|' + self.board[2] + '|' + self.board[3])
        print('-+-+-')
        print(self.board[4] + '|' + self.board[5] + '|' + self.board[6])
        print('-+-+-')
        print(self.board[7] + '|' + self.board[8] + '|' + self.board[9])
        print('\n')

    def is_cell_free(self, position):
        if self.board[position] == ' ':
            return True

        return False

    def update_player_position(self, player, position):
        if self.is_cell_free(position):
            self.board[position] = player
            self.check_game_state()
        else:
            print("Can't insert there!")
            self.move_player()

    def check_game_state(self):
        self.print_board()

        if self.is_draw():
            print("Draw!")
            exit()

        if self.is_winning(self.player):
            print("Player wins!")
            exit()

        if self.is_winning(self.computer):
            print("Computer wins!")
            exit()

    def is_winning(self, player):
        # checking the diagonals (top left to bottom right)
        if self.board[1] == player and self.board[5] == player and self.board[9] == player:
            return True
        # checking the diagonals (top right to bottom left)
        if self.board[3] == player and self.board[5] == player and self.board[7] == player:
            return True

        # checking the rows and columns
        for i in range(BOARD_SIZE):
            if self.board[3*i+1] == player and self.board[3*i+2] == player and self.board[3*i+3] == player:
                return True

            if self.board[i+1] == player and self.board[i+4] == player and self.board[i+7] == player:
                return True

        return False

    def is_draw(self):
        for key in board.keys():
            if self.board[key] == ' ':
                return False

        return True

    def move_player(self):
        position = int(input("Enter the position for 'O':  "))
        self.update_player_position(self.player, position)

    def move_computer(self):
        best_score = -float('inf')
        # best position (best next move) for the computer
        best_move = 0

        # the computer considers all the empty cells on the board and calculates the
        # minimax score (10, -10 or 0)
        for position in board.keys():
            if self.board[position] == ' ':
                self.board[position] = self.computer
                score = self.minimax(0, -float('inf'), float('inf'), False)
                board[position] = ' '

                if score > best_score:
                    best_score = score
                    best_move = position

        # make the next move according to the minimax algorithm result
        self.board[best_move] = self.computer
        self.check_game_state()

    def minimax(self, depth, alpha, beta, is_maximizer):
        # we can make the algorithm greedy: if it is possible to win the game
        # then the algorithm favors that move
        if self.is_winning(self.computer):
            return REWARD - depth

        if self.is_winning(self.player):
            return -REWARD + depth

        if self.is_draw():
            return 0

        # depth-first search but we have to track the layers
        # this is the maximizer layer
        # computer's turn
        if is_maximizer:
            best_score = -float('inf')

            for position in board.keys():
                if self.board[position] == ' ':
                    self.board[position] = self.computer
                    score = self.minimax(depth + 1, alpha, beta, False)
                    self.board[position] = ' '

                    if score > best_score:
                        best_score = score

                    alpha = max(alpha, score)
                    # pruning if necessary
                    if alpha >= beta:
                        break

            return best_score
        # this is the minimizer layer (player's turn)
        else:
            best_score = float('inf')

            for position in board.keys():
                if self.board[position] == ' ':
                    self.board[position] = self.player
                    score = self.minimax(depth + 1, alpha, beta, True)
                    self.board[position] = ' '

                    if score < best_score:
                        best_score = score

                    beta = min(beta, score)
                    # pruning if necessary
                    if alpha >= beta:
                        break

            return best_score


if __name__ == '__main__':
    board = {1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '}

    game = TicTacToe(board)
    game.run()