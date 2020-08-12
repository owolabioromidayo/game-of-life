import time, random, copy

class Board:
    def __init__(self):
        self.grid_2d = None
        self.grid = None
        self.width = None
        self.len = None
        self.pause = True


    def load_state(self,path):
        """Load automata state from file and run simulation"""
        with open(path,'r') as f:
            #get 1d self.grid from 2d txt representation
            self.grid_2d= [list(line.strip()) for line in f.readlines() if '0' in line or '1' in line]
            self.grid = [j for i in self.grid_2d for j in i]

        self.width = len(self.grid_2d[0])
        self.len = len(self.grid)
        self.loop()


    def render(self):
        for row in self.grid_2d:
            print(" ".join(row))
        print('\n')


    def refresh_2d(self):
        """Rebuild the 2d grid representation after 1d update"""
        self.grid_2d= [[]]
        y = 0
        for idx in range(self.len):
            if idx in range(self.width, self.len, self.width): #create new row 
                y += 1
                self.grid_2d.append([])
            self.grid_2d[y].append(self.grid[idx])


    def make_random_state(self):
        """Generate a random state and watch it change"""

        self.width = random.choice(range(5,30))
        height = random.choice(range(5,20))
        self.len = self.width*height

        for i in range(self.len):
            idx = random.choice(range(self.len))
            self.grid[idx] = '1'

        print('State Created... Initializing loop')
        self.loop()


    def get_neighbors(self, idx):
        """Get neighbors of self.grid at index """

        # convert flattened array index to 2d index
        y = idx // self.width
        x = idx - y*self.width
       
        #get neightbour values and total value of neighbors
        neighbor_vals = []
        neighbor_index = [[y,x-1],[y,x+1],[y+1,x],
                            [y+1,x-1],[y+1,x+1],[y-1,x],
                            [y-1,x-1],[y-1,x+1]]

        for neighbor in neighbor_index:
            y,x = neighbor
            try:
                neighbor_vals.append(self.grid_2d[y][x])
            except IndexError as e:
                pass #for edge and corner blocks

        neighbor_count = len([i for i in neighbor_vals if i=='1'])
        return neighbor_count


    def update(self):
        """Move to next game state"""

        grid = self.grid[:] #copy grid, prevent altering game state during state change

        for idx in range(self.len):
            neighbor_count = self.get_neighbors(idx)

            #game update rules
            if neighbor_count in [0,1] and grid[idx]=='1': grid[idx] = '0'
            elif neighbor_count in [2,3] and grid[idx] == '1': pass 
            elif neighbor_count > 3 and grid[idx] == '1': grid[idx] = '0'
            elif neighbor_count == 3 and grid[idx] == '0': grid[idx] = '1'
            else : pass


        self.grid = grid
        self.refresh_2d()
        

    def loop(self):
        """Watch updates"""

        if self.pause:
            return
        else:
            while True:
                self.render()
                time.sleep(0.7)
                self.update()


if __name__ == "__main__":
    b = Board()
    b.load_state('./blinker.txt')
