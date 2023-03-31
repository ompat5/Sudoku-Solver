import pygame
from Sudoku import solve, valid
pygame.font.init()

class Grid:
    # To change the starting board change this
    board = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
        self.width = width
        self.height = height
        self.model = None
        self.selected = None

    def update_model(self):
        self.model = [[self.cubes[i][j].value for j in range(self.cols)] for i in range(self.rows)]
    
    def place(self, val):
        row, col = self.selected
        prev_val = self.cubes[row][col].value
        self.cubes[row][col].set(val)
        self.update_model()
        if valid(self.model, val, (row,col)) and solve(self.model):
            return True
        else:
            self.cubes[row][col].set(prev_val)
            self.update_model()
            return False

    def draw(self, win):
        # Draw Grid Lines
        gap = self.width / 9
        for i in range(self.rows+1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(win, (0,0,0), (0, i*gap), (self.width, i*gap), thick)
            pygame.draw.line(win, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thick)

        # Draw Cubes
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(win)

    def select(self, row, col):
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected = False

        self.cubes[row][col].selected = True
        self.selected = (row, col)

    def clear(self):
        row, col = self.selected
        self.cubes[row][col].set(0)

    def click(self, pos):
        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width / 9
            x = pos[0] // gap
            y = pos[1] // gap
            return (int(y),int(x))
        else:
            return None

    
class Cube:
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width ,height):
        self.value = value
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, win):
        fnt = pygame.font.SysFont("dejavusans", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if not(self.value == 0):
            text = fnt.render(str(self.value), 1, (0, 0, 0))
            win.blit(text, (x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height()/2)))

        if self.selected:
            pygame.draw.rect(win, (255,0,0), (x,y, gap ,gap), 3)

    def set(self, val):
        self.value = val

def redraw_window(win, board):
    win.fill((255,255,255))

    pygame.draw.rect(win,(200,200,200),[300,552,140,40])
    smallfont = pygame.font.SysFont('Corbel',35)
    text = smallfont.render('Solve' , True , (0,0,0))
    win.blit(text , (340,562))

    fnt = pygame.font.SysFont("dejavusans", 20)
    text = fnt.render("Enter your Sudoku Puzzle:", 1, (0,0,0))
    win.blit(text, (10, 560))

    board.draw(win)

def showfinal(board, model):
    for i in range(0,9):
        for j in range(0,9):
            board.cubes[i][j].set(model[i][j])

def main():
    win = pygame.display.set_mode((540,700))
    pygame.display.set_caption("Sudoku")
    board = Grid(9, 9, 540, 540)
    key = None
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_BACKSPACE:
                    board.clear()
                    key = None

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if 300 <= pos[0] <= 440 and 552 <= pos[1] <= 592:
                    showfinal(board, board.model)
                    redraw_window(win, board)
                    pygame.display.update()

                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None

        if board.selected and key != None:
            if board.place(key):
                print("Success")
                key = None
            else:
                print("Wrong")
                key = None

        redraw_window(win, board)
        pygame.display.update()

main()
pygame.quit()