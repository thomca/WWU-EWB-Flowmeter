import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import ttk

matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

# py -m tkinter for example GUI
# https://docs.python.org/3/library/tkinter.html
# https://pythongeeks.org/gui-programming-in-python/
# https://www.pythontutorial.net/tkinter/tkinter-matplotlib/

# win = tk.Tk(screenName=None,  baseName=None,  className='Tk',  useTk=1)

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter Matplotlib Demo')
        
#####################################################
        mb =  Menubutton ( self, text = 'Menu') 
        mb.grid() 
        mb.menu  =  Menu ( mb, tearoff = 0 ) 
        mb['menu']  =  mb.menu
        var1 = IntVar() 
        var2 = IntVar() 
        var3 = IntVar()
        mb.menu.add_checkbutton ( label ='Home', variable = var1 ) 
        mb.menu.add_checkbutton ( label = 'Profile', variable = var2 ) 
        mb.menu.add_checkbutton ( label = 'Sign Out', variable = var3 ) 
        mb.pack() # puts it at top

        #self.geometry('500x200') #setting the size of the window

######################################################
        # make data
        x = np.linspace(0, 10, 100)
        y = 4 + 2 * np.sin(2 * x)


        # create a figure
        figure = Figure(figsize=(6, 4), dpi=100)

        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(figure, self)

        # create the toolbar
        NavigationToolbar2Tk(figure_canvas, self)

        graph = figure.add_subplot()
        graph.plot(x, y, linewidth=2.0)
        graph.set(xlim=(0, 8), xticks=np.arange(1, 8),
        ylim=(0, 8), yticks=np.arange(1, 8))

        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


if __name__ == '__main__':
    app = App()
    app.mainloop()

