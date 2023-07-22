from datetime import datetime
from tkinter import *
from tkinter import font
from  puzzle_creator import *
import keyboard
from functools import partial

root = Tk()
root.title('Stop-Watch')
root.geometry('314x327')
#A3EEDC #D5FBF1
#E4FF8B #F5FBC8
board = [[0 for i in range(9)] for j in range(9)]
gui_board = [[0 for i in range(9)] for j in range(9)]
fixed_values = []
wrong_values = []
counter = 66600
current = None
current_color = None
current_posn = None
mist = 0


def incorrect_nunber(bo, num, pos):    
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and i != pos[1]:
            return pos[0],i

    # Check col
    for i in range(len(bo[0])):
        if bo[i][pos[1]] == num and i != pos[0]:
            return i,pos[1] 
    
    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    
    for i in range(box_y * 3, box_y * 3 + 3): 
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return i,j
    
    return True

def enter_value(value,bo):
    global current, current_posn, mist
    current['text'] = value
    bo[current_posn[0]][current_posn[1]] = value
    print_board(bo)
    verify(bo)

def verify(bo,correct=0):
    global mist
    for i in range(len(bo)):
            for j in range(len(bo[0])):
                num = board[i][j]
                check = valid(board,num,(i,j))
                if not check:
                    print(check)
                    mistakes['text'] = f"Mistakes:{mist+1}/5" 
                
def key_is_presseded():
    keyboard.add_hotkey('1', lambda: enter_value('1',board))
    keyboard.add_hotkey('2', lambda: enter_value('2',board))
    keyboard.add_hotkey('3', lambda: enter_value('3',board))
    keyboard.add_hotkey('4', lambda: enter_value('4',board))
    keyboard.add_hotkey('5', lambda: enter_value('5',board))
    keyboard.add_hotkey('6', lambda: enter_value('6',board))
    keyboard.add_hotkey('7', lambda: enter_value('7',board))
    keyboard.add_hotkey('8', lambda: enter_value('8',board))
    keyboard.add_hotkey('9', lambda: enter_value('9',board))
    keyboard.add_hotkey('Space', lambda: enter_value('  ',board))

def button_focus(pos):
    i = pos[0]
    j = pos[1]
    global current, current_color, current_posn
    if current:
        current['bg'] = current_color

    if pos not in fixed_values:
        current = gui_board[i][j]
        current_color = current['bg']
        current_posn = (i,j)
        current['bg'] = '#F72F33'

def decolor(vacant_values):
    for (i,j) in vacant_values:
        if ((i in (6,7,8) or i in (0,1,2)) and (j in (0,1,2) or j in (6,7,8))) or (i in (3,4,5) and j in (3,4,5)):
            gui_board[i][j]['bg'] = '#D5FBF1'
        else:
            gui_board[i][j]['bg'] = '#EFFFBA'

def gui_maker(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if ((i in (6,7,8) or i in (0,1,2)) and (j in (0,1,2) or j in (6,7,8))) or (i in (3,4,5) and j in (3,4,5)):
                gui_board[i][j] = Button(root,bg='#A3EEDC', borderwidth=1, text = bo[i][j], padx=11, pady=6,
                command= partial(button_focus, (i,j)))
            else:
                gui_board[i][j] = Button(root,bg='#E4FF8B', borderwidth=1, text = bo[i][j], padx=11, pady=6,
                command= partial(button_focus, (i,j)))
            
            gui_board[i][j].grid(row=i+1, column=j)
    
def stop_watch(label):
    def count():    
        global counter
        tt = datetime.fromtimestamp(counter)
        string = tt.strftime("%M:%S")
        display=string
        label['text']=display
        label.after(1000, count) 
        counter += 1

    count()     

generate_sudoku(board)
print_board(board)
fixed_values,vacant_values = unsolve(board,(75,80))
print_board(board)

watch = Label(root,text = '00:00', anchor = 'e')
watch.grid(column=8, row=0)
mistakes = Label(root,text = 'Mistakes: 0/5')
mistakes.grid(columnspan=3, row=0)
gui_maker(board)
decolor(vacant_values)
stop_watch(watch)
key_is_presseded()


root.mainloop()