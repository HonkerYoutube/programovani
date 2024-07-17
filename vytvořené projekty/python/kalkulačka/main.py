import tkinter


class MainWindow(tkinter.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title("kalkulačka")

button = tkinter.Button
root = tkinter.Tk()
app = MainWindow(root)
app.mainloop()
