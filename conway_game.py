import matplotlib.pyplot as plt
import numpy as np
class GameOfLife():
    
    def __init__(self, x_dim, y_dim):
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.life_grid = [[0 for i in range(self.x_dim)] for j in range(self.y_dim)]
        
    def get_grid(self):
        '''
        Function that returns the current state of the grid.
        '''
        return self.life_grid
    
    def print_grid(self):
        '''
        Function that prints the current state of the grid.
        '''
        grid = self.get_grid()
        for y in grid:
            for x in y:
                print(x,'|', end = " ")
            print("\n", end = "")
            print('-'*len(y)*4, sep = " ")
    
    def populate_grid(self, coords):
        '''
        Function takes the list of co-ordinates as input, and the cells
        corresponding to the co-ordinates are set live.
        '''
        for c in coords:
            x,y = c
            if (0<= x <self.x_dim) and (0<= y <self.y_dim):
                self.life_grid[y][x]=1
        return self.life_grid
    
    def make_step(self):
        '''
        Performs one iteration of the game based on the rules of the game.
        '''
        #initializing sum_grid -> to store values of the total number of live neighbours of 
        #each inidividual cell in the grid.
        sum_grid = [[0 for i in range(self.x_dim)] for j in range(self.y_dim)]
        # calculating the total number of live neighbours for each individual cell.
        for i in range(self.y_dim):
            i_start = i-1
            i_end = i+1
            if (i-1)<0:
                i_start = i
            elif i+1>=self.y_dim:
                i_end = i           
            for j in range(self.x_dim):
                j_start = j-1
                j_end = j+1
                if (j-1)<0:
                    j_start = j
                elif j+1>=self.x_dim:
                    j_end = j
                live_n = 0
                for a in range(i_start, i_end+1):
                    for b in range(j_start, j_end+1):
                        if (a,b)!=(i,j):
                            live_n+= self.life_grid[a][b]
                
                sum_grid[i][j] = live_n
        
        #updating the state of cells as live or dead based on the number of live neighbours 
        #it has         
        for i in range(self.y_dim):
            for j in range(self.x_dim):
                if self.life_grid[i][j]==1:
                    if sum_grid[i][j]<2 or sum_grid[i][j]>3:
                        self.life_grid[i][j]=0
                else:
                    if (self.life_grid[i][j]==0) and (sum_grid[i][j]==3):
                        self.life_grid[i][j]=1
        
        return self.life_grid
    
    def make_n_steps(self, n):
        '''
        Function takes number of iterations 'n' as the input.
        Performs 'n' iterations of the game by implementing the make_step function 'n' times.
        Returns the final state of the grid after 'n' steps.
        '''
        for _ in range(n):
            self.life_grid = self.make_step()
            #self.draw_grid()
            
        return self.life_grid
    
    def draw_grid(self):
        '''
        Function to plot the grid. 
        '''
        x = []
        y = []
        for j in range(self.y_dim):
            for i in range(self.x_dim):
                x.append(i)
                y.append(j)
        plt.figure(figsize=(self.x_dim,self.y_dim))
        plt.scatter(x,y, c=np.array(self.life_grid))
        plt.ylim(self.y_dim, -1)
        plt.show()
                                                           
def main():
    '''
    Driver code
    '''
    x_dim = int(input("Enter x dimesion of the grid: "))
    y_dim = int(input("Enter y dimesion of the grid: "))
    gol = GameOfLife(x_dim, y_dim)
    #gol.print_grid()
    gol.populate_grid([(14, 16), (15, 16), (16, 16), (18, 16), (19, 16), (20, 16),
        (16, 14), (16, 15), (16, 17), (16, 18),
        (18, 14), (18, 15), (18, 17), (18, 18),
        (14, 18), (15, 18), (16, 18), (18, 18), (19, 18), (20, 18)])
    gol.make_n_steps(6)
    gol.draw_grid()
    
if __name__ == "__main__":
    main() 