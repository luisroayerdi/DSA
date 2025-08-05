import collections


def numIslands(self, grid):

        '''
        return 0 if the grid is empty
        define rows and columns

        create a set for visited nodes
        start number of islands at 0
        Breadth first search function takes in variables for row and column of where we starting 
            create queue
            append the variables to the queue
            add the variables to the vsited nodes
        
        while queue is not empty:
            

        '''

        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(i, j):
            queue = collections.deque()
            queue.append((i,j))
            visited.add((i,j))


            while queue:
                row, col = queue.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]] #directions of adjacent nodes

                for dr, dc in directions:
                    i, j = row + dr, col + dc
                    if (i in range(rows) and j in range(cols) and grid[i][j] == "1" and (i,j) not in visited):
                        queue.append((i,j))
                        visited.add((i,j))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i,j)
                    islands += 1
        return islands






