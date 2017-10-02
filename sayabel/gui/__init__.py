import tkinter as tk


class SayAbelTkWindow(tk.Frame):
    def __init__(self):
        super().__init__()
        self.pack(fill=tk.BOTH, expand=True)

        self.master.title("SayAbel Client")

        #Create GUI
        generateButton = tk.Button(self, text="Click Me")
        generateButton.grid(row=0, column=1)



        area = tk.Text(self)
        area.grid(row=0, column=0, rowspan=1)

    def initialize(self):
        pass

def initialize_window():
    root = tk.Tk()
    root.geometry("900x600+0+0")
    window_instance = SayAbelTkWindow()
    window_instance.mainloop()