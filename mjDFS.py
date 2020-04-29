class Soln:
    def noOfIsland(self, grid):
        nol = 0
        for i in range(grid.__len__()):
            for j in range(grid[0].__len__()):
                #print(grid[i][j])
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    nol += 1

        return nol


    def dfs(self, grid, i, j):
        # if out of bound return
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'

# ------PRINTING GRID-------------------------------------------------------------

        self.printGrid(grid)

# ------END OF PRINTING GRID -----------------------------------------------------

        # recurse dfs to four corner in this sequence: up, down, left, right
        self.dfs(grid, i-1, j)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i, j-1)
        self.dfs(grid, i, j+1)


    def printGrid(self, grid):
        for x in range(len(grid)):
            print(grid[x])
        print('NEXT')



    # TESTING
s = Soln()
myinput = [['1','0','1'],['1','0','1'],['0','0','1']]
s.printGrid(myinput)
print('The number of island is: ', s.noOfIsland(myinput))



