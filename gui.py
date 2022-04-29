from tkinter import *

root = Tk()
root.geometry('330x370')
  
# Sudoku solver class

class SudokuSolver():

    def __init__(self):
        self.setZero()
        self.solve()
        
    # Sets the empty cells to 0

    def setZero(self):
        for i in range(9):
            for j in range(9):
                if filledBoard[i][j].get() not in ['1','2','3','4','5','6','7','8','9']:
                    filledBoard[i][j].set(0)

    # Backtracking    
    
    def solve(self):
        
        # Finds the next empty cell
        findEmpty = self.emptyCell()
        
        if not findEmpty:
            return True   
        else:
            row, column = findEmpty
        
        for i in range(1,10):
            if self.isValid(i, (row, column)):
                filledBoard[row][column].set(i)

                if self.solve():
                    return True

                filledBoard[row][column].set(0)
        
        return False

    # Checks the row, column and the subgrid to see if it is possible to place a number in the cell          
    
    def isValid (self, num, pos):
        
        # Checks the row
        for i in range(9):
            if filledBoard[pos[0]][i].get() == str(num):
                return False
        
        # Checks the column 
        for i in range(9):
            if filledBoard[i][pos[1]].get() == str(num):
                return False

        # Checks the subgrid
        row = pos[0] // 3 
        column = pos[1] // 3 

        for i in range(row * 3, (row * 3) + 3):
            for j in range(column * 3, (column * 3) + 3):
                if filledBoard[i][j].get() == str(num):
                    return False 
        return True

    # Finds empty cells, previously defined as cells with a zero

    def emptyCell(self):
        for row in range(9):
            for column in range(9):
                if filledBoard[row][column].get() == '0':
                    return (row,column)
        return None

# GUI class

class Interface():
    def __init__(self, window):
        self.window = window
        window.title("Sudoku Solver")

        font = ('Arial', 20)
        color = 'white'

        # Creates a button to solve and another to clear the grid, linked to solve and clear methods

        solve = Button(window, text = 'Solve', command = self.Solve)
        solve.grid(column=3,row=20)
        clear = Button(window, text = 'Clear', command = self.Clear)
        clear.grid(column = 5,row=20)

        # Initializes an empty 2D list

        self.board  = []
        for row in range(9):
            self.board += [["","","","","","","","",""]]

        for row in range(9):
            for col in range(9):

                # Changes the color of the cells depending on the position in the grid
                
                if (row < 3 or row > 5) and (col < 3 or col > 5):
                    color = 'white' 
                elif (row >= 3 and row < 6) and (col >=3 and col < 6):
                    color = 'white'
                else:
                    color = 'grey'
                
                # Makes each cell an entry box and stores each entry into the filledBoard 2D list

                self.board[row][col] = Entry(window, width = 2, font = font, bg = color, cursor = 'arrow', borderwidth = 2,
                                          highlightcolor = 'yellow', highlightthickness = 0, highlightbackground = 'black', 
                                          textvariable = filledBoard[row][col]) 
                self.board[row][col].bind('<FocusIn>', self.gridChecker) 
                self.board[row][col].bind('<Motion>', self.gridChecker)                        
                self.board[row][col].grid(row = row, column = col)

    # Check if the placed value by the user is an integer between 1 and 9. If not valid it clears the value.

    def gridChecker(self, event):
        for row in range(9):
            for col in range(9):
                if filledBoard[row][col].get() not in ['1','2','3','4','5','6','7','8','9']:
                    filledBoard[row][col].set('')

    # Calls the sudoku solver class
    def Solve(self):
        SudokuSolver()

    # Calls the sudoku clear class 
    def Clear(self):
        for row in range(9):
            for col in range(9):
                filledBoard[row][col].set('')

# 2D list

filledBoard = []
for row in range(9): 
    filledBoard += [["","","","","","","","",""]]
for row in range(9):
    for col in range(9):
        filledBoard[row][col] = StringVar(root)    

# Loop

Interface(root)
root.mainloop()



