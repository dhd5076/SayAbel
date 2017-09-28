import tkinter as tk


class SayAbelTkWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()



    def initialize(self):
        pass

def initialize_window():
    root = tk.Tk()
    window_instance = SayAbelTkWindow(master=root)
    window_instance.mainloop()