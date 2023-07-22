import random


class SudokuStatic:
    def __init__(self, difficulty=None):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.difficulty = difficulty or (30, 40)

    def new_board(self):
        # Generate a solved Sudoku board
        self.solve()
        self.vacant_values = []
        # Remove some cells to create the puzzle
        empty_cells = random.randint(self.difficulty[0], self.difficulty[1])  # Adjust the range based on the desired difficulty
        for _ in range(empty_cells):
            row, col = random.randint(0, 8), random.randint(0, 8)
            while self.board[row][col] == 0:
                row, col = random.randint(0, 8), random.randint(0, 8)
            self.board[row][col] = 0
            self.vacant_values.append((row, col))
        self.fixed_values = [(i, j) for i in range(9) for j in range(9) if self.board[i][j] != 0]

    def is_valid(self, num, pos):
        # Check row
        if num in self.board[pos[0]]:
            return False

        # Check column
        if num in [self.board[i][pos[1]] for i in range(9)]:
            return False

        # Check 3x3 box
        box_x = pos[1] // 3
        box_y = pos[0] // 3
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.board[i][j] == num:
                    return False

        return True

    def is_solved(self):
        # Check rows
        for row in self.board:
            if sorted(row) != list(range(1, 10)):
                return False

        # Check columns
        for col in range(9):
            if sorted([self.board[i][col] for i in range(9)]) != list(range(1, 10)):
                return False

        # Check 3x3 boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = [self.board[i][j] for i in range(box_row, box_row + 3) for j in range(box_col, box_col + 3)]
                if sorted(box) != list(range(1, 10)):
                    return False

        return True

    def solve(self):
        find = [(i, j) for i in range(9) for j in range(9) if self.board[i][j] == 0]
        if not find:
            return True
        else:
            row, col = find[0]

        for num in range(1, 10):
            if self.is_valid(num, (row, col)):
                self.board[row][col] = num

                if self.solve():
                    return True

                self.board[row][col] = 0

        return False

    def print_board(self):
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - -")

            for j in range(len(self.board[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + " ", end="")
