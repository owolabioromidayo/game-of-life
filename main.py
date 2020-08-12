import time, random, copy

class Board:
    def __init__(self):
        self.L = 100
        self.grid = ['0' for i in range(self.L)]
        self.W = 10




    def load_state(self,path):
        with open(path,'r') as f:
            grid= [list(line.strip()) for line in f.readlines()]
            self.grid = [j for i in grid for j in i]

        self.W = len(grid[0])
        self.L = len(self.grid)
        self.loop()
          

            




    def printArr(self, arr, w, l, flat=True):
        if flat:
            str_self = ''
            for idx in range(l):
                str_self = str_self + ' ' + arr[idx]

                if idx in range(w-1,l,w):
                    str_self = str_self + '\n'

            print(str_self)

        else:
            for a in arr:
                print(str(a))
        


    def make_random_state(self):
        num = random.choice(range(self.L))
        for i in range(num):
            idx = random.choice(range(self.L))
            self.grid[idx] = '1'
            time.sleep(0.7)
            self.printArr(self.grid, self.W, self.L)

        print('State Created... Initializing loop')
        
        self.loop()


    def get_neighbors(self, idx):
        #conv to 2d
        y = idx // self.W
        x = idx - y*self.W
        idx_2d = y,x


        new_ls = [[]]
        count = 0
        for idx in range(self.L):
            if idx in range(self.W,self.L,self.W):
                count += 1
                new_ls.append([])
            new_ls[count].append(self.grid[idx])



        neighbor_vals = []

        n_idxs = [[y,x-1],[y,x+1],[y+1,x],[y+1,x-1],[y+1,x+1],[y-1,x],[y-1,x-1],[y-1,x+1]]

        for idx in n_idxs:
            y,x = idx
            try:
                neighbor_vals.append(new_ls[y][x])
            except:
                pass


        neighbor_count = len([i for i in neighbor_vals if i=='1'])
        return neighbor_count


    def update(self):

        grid = copy.deepcopy(self.grid)

        for idx in range(self.L):
            neighbor_count = self.get_neighbors(idx)
            if neighbor_count in [0,1] and grid[idx]=='1': grid[idx] = '0'
            elif neighbor_count in [2,3] and grid[idx] == '1': pass 
            elif neighbor_count > 3 and grid[idx] == '1': grid[idx] = '0'
            elif neighbor_count == 3 and grid[idx] == '0': grid[idx] = '1'
            else : pass


        self.grid = copy.deepcopy(grid)
        




    def loop(self):
        while True:
            self.printArr(self.grid, self.W, self.L)
            time.sleep(0.7)
            self.update()







if __name__ == "__main__":
    b = Board()
    # b.make_random_state()
    # b.load_state('./toad.txt')
    b.load_state('./ggg.txt')
