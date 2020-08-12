import time, random

class Board:
    def __init__(self):
        self.L = 100
        self.grid = ['0' for i in range(self.L)]
        self.W = 10



    # def __str__(self):
    #     self.printArr(self.grid, self.W, self.L)

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
            time.sleep(0.1)
            self.printArr(self.grid, self.W, self.L)

        print('pre update')
        self.update()
        self.printArr(self.grid, self.W, self.L)


    def get_neighbors(self, idx):
        #conv to 2d
        y = idx // self.W
        x = idx - y*self.W
        idx_2d = x,y


        new_ls = [[]]
        count = 0
        for idx in range(self.L):
            if idx in range(self.W,self.L,self.W):
                count += 1
                new_ls.append([])
            new_ls[count].append(self.grid[idx])


        neighbor_vals = []

        for i in [y,y-1,y+1]:
            for j in [x,x-1,x+1]:
                try:
                    neighbor_vals.append(new_ls[i][j])
                except:
                    neighbor_vals.append('0')


        neighbor_count = len([i for i in neighbor_vals if i=='1'])
        return neighbor_count


    def update(self):

        for idx in range(self.L):
            if self.grid[idx] != '0':
                neighbor_count = self.get_neighbors(idx)
                if neighbor_count < 2 or neighbor_count > 3: self.grid[idx] = '0'





    def loop(self):
        while True:
            self.update()
            time.sleep(0.5)
            print(self)






if __name__ == "__main__":
    b = Board()

    # b.get_next_state()
    # b.loop()
    b.make_random_state()