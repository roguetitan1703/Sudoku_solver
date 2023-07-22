import tkinter as tk

class MainWindow(tk.Frame):

    def __init__(self, master):

        tk.Frame.__init__(self, master)
        self.pack()
        btn_new_element = tk.Button(self, text='new', command=self.new_element)
        btn_new_element.pack()
        self.master = master
        self.pack()

    def new_element(self):
        popup = Popup(self.master, 1, 0)


class Popup(tk.Toplevel):
    def __init__(self, master, var1, var2):
        super().__init__(master)
        #some widgets
        btn = tk.Button(self, text='Enter', command=lambda a=var1, b=var2: self.foo(a,b))
        btn.pack()

    def foo(self, a, b):
        self.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    window = MainWindow(root)
    root.mainloop()