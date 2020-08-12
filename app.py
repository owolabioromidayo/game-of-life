import tkinter as tk
from Board import Board
import time, sys

class App:
    def __init__(self, path, cellsize=100, inverted=False, interval=0.5):
        self.path = path
        self.cellsize = cellsize
        self.inverted = inverted
        self.rect_index = []
        self.interval = interval
        self.running = True

        self.board = Board()
        self.board.load_state(path)
        self.build()
        self.update()


    
    def getColor(self,value):
        colors = ['white', 'black']
        inv_colors = ['black', 'white']

        value = int(value)
        if self.inverted: 
            return inv_colors[value]
        return colors[value]


    def configureCanvas(self,grid):
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                #topLeftCornerCoords 
                tp_x = x*self.cellsize
                tp_y = y*self.cellsize
                value = grid[y][x]
                color =  self.getColor(value)
                tag = '.r' + str(y*len(grid) + x)
                self.canvas.create_rectangle(tp_x,tp_y, tp_x+self.cellsize, tp_y+self.cellsize,fill=color, tag=tag)



    def updateCanvas(self, grid):
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                value = grid[y][x]
                color = self.getColor(value)
                tag = '.r' + str(y*len(grid) + x)
                self.canvas.itemconfig(tagOrId=tag ,fill=color)


    def update(self):
        self.configureCanvas(self.board.grid_2d)
        while self.running:
            self.updateCanvas(self.board.grid_2d)
            self.root.update()
            time.sleep(self.interval)
            self.board.update()


    def on_closing(self):
        self.running = False
        time.sleep(self.interval)
        self.root.destroy()
        sys.exit()


    def build(self):
        self.win_width = self.board.width*self.cellsize
        self.win_height = (self.board.len // self.board.width) * self.cellsize

        self.root = tk.Tk()
        self.root.title("Game of Life")
        self.root.geometry(f"{self.win_width}x{self.win_height}")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.resizable(width=False, height=False)
        self.canvas = tk.Canvas(width=self.win_width, height=self.win_height)
        self.canvas.pack()


        


if __name__ == "__main__":
    App('./oscillator.txt', 30, inverted=False, interval=0.05)




    
