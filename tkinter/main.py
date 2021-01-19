from tkinter import *
from tkinter import filedialog

from PIL import Image, ImageTk

class Paparan(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Item")
        fileMenu.add_command(label='Buka imej', command=self.bukaImej)
        fileMenu.add_command(label="Keluar", command=self.keluarProgram)
        menu.add_cascade(label="File", menu=fileMenu)

        editMenu = Menu(menu)
        editMenu.add_command(label="Undo")
        editMenu.add_command(label="Redo")
        menu.add_cascade(label="Edit", menu=editMenu)

        aboutMenu = Menu(menu)
        aboutMenu.add_command(label='Hakcipta', command=self.hakCipta)
        menu.add_cascade(label="Informasi", menu=aboutMenu)

    def hakCipta(self):
        disedia = Label(
            text='__author__ = "Wan Ab Muadz Adzim\n__copyright__ = "Copyright (C) 2004 Matahelang\n__version__ = "1.0"',
            font=("arial italic", 18))
        disedia.pack()

    def bukaImej(self):
        namafile = filedialog.askopenfilename(initialdir='/',title='Pilih imej')
        load = Image.open(namafile)
        render = ImageTk.PhotoImage(load)
        img = Label(image=render)
        img.image = render
        # img.place(x=1, y=1)
        img.pack()

    def keluarProgram(self):
        exit()

if __name__ == "__main__":
    root = Tk()
    app = Paparan(root)
    
    root.wm_title("WMarked")
    root.geometry('500x500')
    root.mainloop()