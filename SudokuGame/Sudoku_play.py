import numpy as np
from datetime import datetime
from tkinter import *
import keyboard
from functools import partial
from tkinter import simpledialog, Toplevel

class SudokuGame:
    def __init__(self):
        self.root = Tk()
        self.gui_board = [[0 for i in range(9)] for j in range(9)]
        self.fixed_values = []
        self.counter = 66600
        self.current = None
        self.current_color = None
        self.current_posn = None
        self.mist = 0
        self.count = True
        self.watch = Label(self.root, text='00:00', anchor='e')
        self.solve = Button(self.root, text='Solve',bg="#FF6B6B", command=self.solve_game)
        self.quit = Button(self.root, text='Quit',bg="#FF6B6B", command=self.root.destroy)
        self.mistakes = Label(self.root, text='Mistakes: 0/5')

        
    def create_difficulty_window(self):
        self.root.title('Choose Difficulty')
        
        # Create buttons for each difficulty level with corresponding colors
        self.easy_btn = Button(self.root, text="Easy", bg="#A3EEDC", command=lambda: self.select_difficulty((20, 29)))
        self.easy_btn.pack(pady=10)

        self.medium_btn = Button(self.root, text="Medium", bg="#E4FF8B", command=lambda: self.select_difficulty((30, 40)))
        self.medium_btn.pack(pady=10)

        self.hard_btn = Button(self.root, text="Hard", bg="#F72F33", command=lambda: self.select_difficulty((41, 55)))
        self.hard_btn.pack(pady=10)
    
    def destroy_difficulty_window(self):
        self.easy_btn.destroy()
        self.medium_btn.destroy()
        self.hard_btn.destroy()        

    def select_difficulty(self, difficulty):
        self.generate_game(difficulty)

    def generate_game(self,difficulty):
        self.sudoku_static = SudokuStatic(difficulty)        
        self.sudoku_static.new_board()

        self.destroy_difficulty_window()    
        self.root.title('Sudoku')
        self.root.geometry('314x327')
        self.root.resizable(0, 0)
        self.watch['text'] = '00:00'
        self.watch.grid(column=8, row=0)
        self.solve.grid(columnspan=2, row=0)
        self.quit.grid(columnspan=4, row=0)
        # self.mistakes['text'] = 'Mistakes: 0/5'
        # self.mistakes.grid(columnspan=3, row=0)
        self.key_is_presseded()
        self.gui_maker()
        self.decolor()


    def solve_game(self):
        self.sudoku_static.solve()
        self.gui_maker()
        self.decolor()
        self.count = False        


    def enter_value(self, value):
        self.current['text'] = value
        self.sudoku_static.board[self.current_posn[0]][self.current_posn[1]] = int(value)
        if self.sudoku_static.is_solved():
            self.count = False        
            self.solve['text'] = 'Solved'
            self.solve['bg'] = 'white'
            self.root.title('Solved! Congratulations!')
            
    def verify(self, correct=0):
        for i in range(len(self.sudoku_static.board)):
            for j in range(len(self.sudoku_static.board[0])):
                num = self.sudoku_static.board[i][j]
                check = self.sudoku_static.is_valid(num, (i, j))
                if not check:
                    self.mist += 1
                    # self.mistakes['text'] = f"Mistakes: {self.mist}/5"

    def key_is_presseded(self):
        keyboard.add_hotkey('1', lambda: self.enter_value('1'))
        keyboard.add_hotkey('2', lambda: self.enter_value('2'))
        keyboard.add_hotkey('3', lambda: self.enter_value('3'))
        keyboard.add_hotkey('4', lambda: self.enter_value('4'))
        keyboard.add_hotkey('5', lambda: self.enter_value('5'))
        keyboard.add_hotkey('6', lambda: self.enter_value('6'))
        keyboard.add_hotkey('7', lambda: self.enter_value('7'))
        keyboard.add_hotkey('8', lambda: self.enter_value('8'))
        keyboard.add_hotkey('9', lambda: self.enter_value('9'))
        keyboard.add_hotkey('Space', lambda: self.enter_value('  '))

    def button_focus(self, pos):
        i = pos[0]
        j = pos[1]
        if self.current:
            self.current['bg'] = self.current_color

        if pos not in self.sudoku_static.fixed_values:
            self.current = self.gui_board[i][j]
            self.current_color = self.current['bg']
            self.current_posn = (i, j)
            self.current['bg'] = '#F72F33'

    def decolor(self):
        vacant_values = self.sudoku_static.vacant_values
        for (i, j) in vacant_values:
            if ((i in (6, 7, 8) or i in (0, 1, 2)) and (j in (0, 1, 2) or j in (6, 7, 8))) or (i in (3, 4, 5) and j in (3, 4, 5)):
                self.gui_board[i][j]['bg'] = '#D5FBF1'
            else:
                self.gui_board[i][j]['bg'] = '#EFFFBA'

    def gui_maker(self):
        for i in range(len(self.sudoku_static.board)):
            for j in range(len(self.sudoku_static.board[0])):
                if self.sudoku_static.board[i][j] == 0:
                    if ((i in (6, 7, 8) or i in (0, 1, 2)) and (j in (0, 1, 2) or j in (6, 7, 8))) or (i in (3, 4, 5) and j in (3, 4, 5)):
                        self.gui_board[i][j] = Button(self.root, bg='#A3EEDC', borderwidth=1, text='  ', padx=11, pady=6,
                                                    command=partial(self.button_focus, (i, j)))
                    else:
                        self.gui_board[i][j] = Button(self.root, bg='#E4FF8B', borderwidth=1, text='  ', padx=11, pady=6,
                                                    command=partial(self.button_focus, (i, j)))
                else:
                    if ((i in (6, 7, 8) or i in (0, 1, 2)) and (j in (0, 1, 2) or j in (6, 7, 8))) or (i in (3, 4, 5) and j in (3, 4, 5)):
                        self.gui_board[i][j] = Button(self.root, bg='#A3EEDC', borderwidth=1, text=self.sudoku_static.board[i][j], padx=11, pady=6,
                                                    command=partial(self.button_focus, (i, j)))
                    else:
                        self.gui_board[i][j] = Button(self.root, bg='#E4FF8B', borderwidth=1, text=self.sudoku_static.board[i][j], padx=11, pady=6,
                                                    command=partial(self.button_focus, (i, j)))

                self.gui_board[i][j].grid(row=i + 1, column=j)


    def stop_watch(self):
        def count():
            tt = datetime.fromtimestamp(self.counter)
            string = tt.strftime("%M:%S")
            display = string
            self.watch['text'] = display
            self.root.after(1000, count)
            self.counter += 1
        if self.count:
            count()

    def start_game(self):
        self.create_difficulty_window()
        self.stop_watch()
        self.root.mainloop()


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


if __name__ == "__main__":
    game = SudokuGame()
    game.start_game()
