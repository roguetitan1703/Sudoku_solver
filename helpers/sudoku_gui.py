import numpy as np
from datetime import datetime
from tkinter import *
import keyboard
from sudoku_static import SudokuStatic
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


        # Clear the previous GUI board and recreate the new GUI board with the updated puzzle.
        self.gui_maker()

        # Reset the watch and mistakes labels, and update the vacant values for decoloring.

        self.decolor()

    def solve_game(self):
        self.sudoku_static.solve()
        self.gui_maker()
        self.decolor()
        


    def enter_value(self, value):
        self.current['text'] = value
        self.sudoku_static.board[self.current_posn[0]][self.current_posn[1]] = int(value)
        if self.sudoku_static.is_solved():
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

        count()

    def start_game(self):
        self.create_difficulty_window()
        self.stop_watch()
        self.root.mainloop()

if __name__ == "__main__":
    game = SudokuGame()
    game.start_game()
