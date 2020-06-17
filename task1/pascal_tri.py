'''
Created on 2 Jun 2020

@author: blarico
'''

def pascal_triangle_row(n):
    #pascals_triangle=[]
    def pascalSpot(row,col):
        if (col==1): return 1
        if (col==row): return 1
        upLeft= pascalSpot(row -1, col -1)
        upright= pascalSpot(row -1, col)
        return upLeft + upright
    
    for r in range(1, n + 1):
        for c in range(1, r + 1):
            print(pascalSpot(r, c), end=" ")
        print("")

pascal_triangle_row(15)

    
