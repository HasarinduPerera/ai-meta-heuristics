class MazeProblem:

    def __init__(self, maze):
        # this is the two-dimensional representation of the maze
        # 0: obstacle 1:valid cell
        self.maze = maze
        # it will store the solution (S represents the solution cells)
        self.solution = [['-' for _ in range(len(maze))] for _ in range(len(maze))]

    def find_solution(self):
        if self.solve(0, 0):
            self.show_solution()
        else:
            print('There is no solution...')

    def solve(self, row, col):
        # if we have found the destination (bottom right cell) then it is done
        if self.is_finished(row, col):
            return True

        # check if the given cell is valid or not
        if self.is_valid(row, col):
            # it is valid so it is part of the solution
            self.solution[row][col] = 'S'

            # GOING RIGHT !!!
            # go forward in the horizontal direction
            # note: we have to increment the col_index to move horizontally
            if self.solve(row, col + 1):
                return True

            # GOING DOWN !!!
            # go downwards in the vertical direction
            # note: we have to increment the row_index to move vertically
            if self.solve(row + 1, col):
                return True

            # BACKTRACK !!!
            self.solution[row][col] = '-'

        return False

    def is_valid(self, row, col):
        # we can not leave the maze horizontally
        if row < 0 or row >= len(self.maze):
            return False

        # we can not leave the maze vertically
        if col < 0 or col >= len(self.maze):
            return False

        # given location is an obstacle !!!
        if self.maze[row][col] != 1:
            return False

        return True

    def is_finished(self, row, col):
        if row == len(self.maze) - 1 and col == len(self.maze) - 1:
            self.solution[row][col] = 'S'
            return True

        return False

    def show_solution(self):
        print('\n'.join(' '.join(str(x) for x in row) for row in self.solution))


if __name__ == '__main__':
    m = [[1, 0, 0, 1],
         [1, 0, 0, 1],
         [1, 0, 0, 1],
         [1, 1, 1, 1]
         ]

    problem = MazeProblem(m)
    problem.find_solution()
