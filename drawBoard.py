import pygame

wking = pygame.image.load('./assets/Chess_klt60.png')
wqueen = pygame.image.load('./assets/Chess_qlt60.png')
wbishop = pygame.image.load('./assets/Chess_blt60.png')
wknight = pygame.image.load('./assets/Chess_nlt60.png')
wrook = pygame.image.load('./assets/Chess_kdl45.png')
wpawn = pygame.image.load('./assets/Chess_plt60.png')

bking = pygame.image.load('./assets/Chess_kdt60.png')
bqueen = pygame.image.load('./assets/Chess_qdt60b.png')
bbishop = pygame.image.load('./assets/Chess_bdt60.png')
bknight = pygame.image.load('./assets/Chess_ndt60.png')
brook = pygame.image.load('./assets/Chess_rdt60.png')
bpawn = pygame.image.load('./assets/Chess_pdt60.png')


board = []

id = 0
preMoves = []


def drawWhiteBoard(screen, BLACK, WHITE):
    pygame.display.set_caption('Play Chess!')
    # Assume 'screen' is your display Surface object
    screen.fill((0, 0, 0))  # This will fill the entire screen with black color
    # Update the full display Surface to the screen

    square_color = WHITE
    for y in range(8):
        if (y+1) % 2 == 0:
            square_color = BLACK
        else:
            square_color = WHITE
        for x in range(8):
            pygame.draw.rect(screen, square_color, (x*100, y*100, 100, 100))
            if square_color == BLACK:
                square_color = WHITE
            else:
                square_color = BLACK

    updateBoard(screen)

    
        

def drawBlackBoard(screen, BLACK, WHITE):
    pygame.display.set_caption('Play Chess!')
    # Assume 'screen' is your display Surface object
    screen.fill((0, 0, 0))  # This will fill the entire screen with black color
    # Update the full display Surface to the screen

    square_color = WHITE
    for y in range(8):
        if (y+1) % 2 == 0:
            square_color = BLACK
        else:
            square_color = WHITE
        for x in range(8):
            pygame.draw.rect(screen, square_color, (x*100, y*100, 100, 100))
            if square_color == BLACK:
                square_color = WHITE
            else:
                square_color = BLACK

    updateBoard(screen)

def checkWhiteKingMove():
    for move in preMoves:
        if 'wk' in move['piece'][5]:
            return True
    return False
        
def checkBlackKingMove():
    for move in preMoves:
        if 'bk' in move['piece'][5]:
            return True
    return False
        
def checkWhiteLeftRookMove():
    for move in preMoves:
        if 'wr1' in move['piece'][5]:
            return True
    return False
        
def checkWhiteRightRookMove():
    for move in preMoves:
        if 'wr2' in move['piece'][5]:
            return True
    return False
        
def checkBlackLeftRookMove():
    for move in preMoves:
        if 'br1' in move['piece'][5]:
            return True
    return False
        
def checkBlackRightRookMove():
    for move in preMoves:
        if 'br2' in move['piece'][5]:
            return True
    return False

def makeBoardB():
    board.append([[wrook, 5, "r", [0, 0], "w", "wr1"], [wknight, 3, "n", [0, 1], "w", "wn1"], [wbishop, 3, "b", [0, 2], "w", "wb1"], [wking, float('inf'), "k", [0, 3], "w", "wk"], [wqueen, 9, "q", [0, 4], "w", "wq"], [wbishop, 3, "b", [0, 5], "w", "wb2"], [wknight, 3, "n", [0, 6], "w", "wn2"], [wrook, 5, "r", [0, 7], "w", "wr2"]])
    board.append([[wpawn, 1, "p", [1, 0], "w", "wp1"], [wpawn, 1, "p", [1, 1], "w", "wp2"], [wpawn, 1, "p", [1, 2], "w", "wp3"], [wpawn, 1, "p", [1, 3], "w", "wp4"], [wpawn, 1, "p", [1, 4], "w", "wp5"], [wpawn, 1, "p", [1, 5], "w", "wp6"], [wpawn, 1, "p", [1, 6], "w", "wp7"], [wpawn, 1, "p", [1, 7], "w", "wp8"]])

    for y in range(4):
        board.append([[None], [None], [None], [None], [None], [None], [None], [None]])

    board.append([[bpawn, 1, "p", [6, 0], "b", "bp1"], [bpawn, 1, "p", [6, 1], "b", "bp2"], [bpawn, 1, "p", [6, 2], "b", "bp3"], [bpawn, 1, "p", [6, 3], "b", "bp4"], [bpawn, 1, "p", [6, 4], "b", "bp5"], [bpawn, 1, "p", [6, 5], "b", "bp6"], [bpawn, 1, "p", [6, 6], "b", "bp7"], [bpawn, 1, "p", [6, 7], "b", "bp8"]])
    board.append([[brook, 5, "r", [7, 0], "b", "br1"], [bknight, 3, "n", [7, 1], "b", "bn1"], [bbishop, 3, "b", [7, 2], "b", "bb1"], [bking, float('inf'), "k", [7, 3], "b", "bk"], [bqueen, 9, "q", [7, 4], "b", "bq"], [bbishop, 3, "b", [7, 5], "b", "bb2"], [bknight, 3, "n", [7, 6], "b", "bn2"], [brook, 5, "r", [7, 7], "b", "br2"]])


def makeBoardW():
    board.append([[brook, 5, "r", [0, 0], "b", "br1"], [bknight, 3, "n", [0, 1], "b", "bn1"], [bbishop, 3, "b", [0, 2], "b", "bb1"], [bqueen, 9, "q", [0, 3], "b", "bq"], [bking, float('inf'), "k", [0, 4], "b", "bk"], [bbishop, 3, "b", [0, 5], "b", "bb2"], [bknight, 3, "n", [0, 6], "b", "bn2"], [brook, 5, "r", [0, 7], "b", "br2"]])
    board.append([[bpawn, 1, "p", [1, 0], "b", "bp1"], [bpawn, 1, "p", [1, 1], "b", "bp2"], [bpawn, 1, "p", [1, 2], "b", "bp3"], [bpawn, 1, "p", [1, 3], "b", "bp4"], [bpawn, 1, "p", [1, 4], "b", "bp5"], [bpawn, 1, "p", [1, 5], "b", "bp6"], [bpawn, 1, "p", [1, 6], "b", "bp7"], [bpawn, 1, "p", [1, 7], "b", "bp8"]])

    for y in range(4):
        board.append([[None], [None], [None], [None], [None], [None], [None], [None]])

    board.append([[wpawn, 1, "p", [6, 0], "w", "wp1"], [wpawn, 1, "p", [6, 1], "w", "wp2"], [wpawn, 1, "p", [6, 2], "w", "wp3"], [wpawn, 1, "p", [6, 3], "w", "wp4"], [wpawn, 1, "p", [6, 4], "w", "wp5"], [wpawn, 1, "p", [6, 5], "w", "wp6"], [wpawn, 1, "p", [6, 6], "w", "wp7"], [wpawn, 1, "p", [6, 7], "w", "wp8"]])
    board.append([[wrook, 5, "r", [7, 0], "w", "wr1"], [wknight, 3, "n", [7, 1], "w", "wn1"], [wbishop, 3, "b", [7, 2], "w", "wb1"], [wqueen, 9, "q", [7, 3], "w", "wq"], [wking, float('inf'), "k", [7, 4], "w", "wk"], [wbishop, 3, "b", [7, 5], "w", "wb2"], [wknight, 3, "n", [7, 6], "w", "wn2"], [wrook, 5, "r", [7, 7], "w", "wr2"]])

def updateBoard(screen):
    h = 0
    w = 0
    for y in board:
        w = 0
        for x in y:
            if x[0] != None:
                screen.blit(x[0], (w*100, h*100))
            w += 1
        h +=1

    pygame.display.flip()



def legalMovesWhite(piece, playerPosition):
    squares = []
    if piece[0] != None and piece[4] == "w":

        if piece[2] == "p" and playerPosition == "front":

            if piece[3][0] == 6:
                if board[piece[3][0]-1][piece[3][1]][0] == None:
                    squares.append([piece[3][0]-1, piece[3][1]])
                if board[piece[3][0]-1][piece[3][1]][0] == None and board[piece[3][0]-2][piece[3][1]][0] == None:
                    squares.append([piece[3][0]-2, piece[3][1]])


            if (piece[3][0]-1 >= 0):
                if board[piece[3][0]-1][piece[3][1]][0] == None:
                    squares.append([piece[3][0]-1, piece[3][1]])

            
            if (piece[3][0]-1 >= 0 and piece[3][1]-1 >= 0):
                if board[piece[3][0]-1][piece[3][1]-1][0] is not None and board[piece[3][0]-1][piece[3][1]-1][4] == "b":
                    squares.append([piece[3][0]-1, piece[3][1]-1])

            if (piece[3][0]-1 >= 0 and piece[3][1]+1 < 8):
                if board[piece[3][0]-1][piece[3][1]+1][0] is not None and board[piece[3][0]-1][piece[3][1]+1][4] == "b":
                    squares.append([piece[3][0]-1, piece[3][1]+1])

            if len(preMoves) != 0:
                if (preMoves[len(preMoves)-1]["piece"][2] == "p" and abs(preMoves[len(preMoves)-1]["from"][0]-preMoves[len(preMoves)-1]["to"][0]) == 2):
                    if (piece[3][1]-preMoves[len(preMoves)-1]["to"][1] == 1 and piece[3][0]-preMoves[len(preMoves)-1]["to"][0] == 0):
                        squares.append([piece[3][0]-1, piece[3][1]-1])

                if (preMoves[len(preMoves)-1]["piece"][2] == "p" and abs(preMoves[len(preMoves)-1]["from"][0]-preMoves[len(preMoves)-1]["to"][0]) == 2):
                    if (piece[3][1]-preMoves[len(preMoves)-1]["to"][1] == -1 and piece[3][0]-preMoves[len(preMoves)-1]["to"][0] == 0):
                        squares.append([piece[3][0]-1, piece[3][1]+1])

        if piece[2] == "p" and playerPosition == "back":

            if piece[3][0] == 1:
                if board[piece[3][0]+1][piece[3][1]][0] == None:
                    squares.append([piece[3][0]+1, piece[3][1]])
                if board[piece[3][0]+1][piece[3][1]][0] == None and board[piece[3][0]+2][piece[3][1]][0] == None:
                    squares.append([piece[3][0]+2, piece[3][1]])


            if (piece[3][0]+1 < 8):
                if board[piece[3][0]+1][piece[3][1]][0] == None:
                    squares.append([piece[3][0]+1, piece[3][1]])

            
            if (piece[3][0]+1 < 8 and piece[3][1]-1 >= 0):
                if board[piece[3][0]+1][piece[3][1]-1][0] is not None and board[piece[3][0]+1][piece[3][1]-1][4] == "b":
                    squares.append([piece[3][0]+1, piece[3][1]-1])

            if (piece[3][0]+1 < 8 and piece[3][1]+1 < 8):
                if board[piece[3][0]+1][piece[3][1]+1][0] is not None and board[piece[3][0]+1][piece[3][1]+1][4] == "b":
                    squares.append([piece[3][0]+1, piece[3][1]+1])

            if len(preMoves) != 0:
                if (preMoves[len(preMoves)-1]["piece"][2] == "p" and abs(preMoves[len(preMoves)-1]["from"][0]-preMoves[len(preMoves)-1]["to"][0]) == 2):
                    if (piece[3][1]-preMoves[len(preMoves)-1]["to"][1] == 1 and piece[3][0]-preMoves[len(preMoves)-1]["to"][0] == 0):
                        squares.append([piece[3][0]+1, piece[3][1]-1])

                if (preMoves[len(preMoves)-1]["piece"][2] == "p" and abs(preMoves[len(preMoves)-1]["from"][0]-preMoves[len(preMoves)-1]["to"][0]) == 2):
                    if (piece[3][1]-preMoves[len(preMoves)-1]["to"][1] == -1 and piece[3][0]-preMoves[len(preMoves)-1]["to"][0] == 0):
                        squares.append([piece[3][0]+1, piece[3][1]+1])

        if piece[2] == 'n':
            if (piece[3][0]-2 >= 0 and piece[3][1]-1 >= 0):
                if (board[piece[3][0]-2][piece[3][1]-1][0] == None or board[piece[3][0]-2][piece[3][1]-1][4] == "b"):
                    squares.append([piece[3][0]-2, piece[3][1]-1])

            if (piece[3][0]-2 >= 0 and piece[3][1]+1 < 8):
                if (board[piece[3][0]-2][piece[3][1]+1][0] == None or board[piece[3][0]-2][piece[3][1]+1][4] == "b"):
                    squares.append([piece[3][0]-2, piece[3][1]+1])

            if (piece[3][0]-1 >= 0 and piece[3][1]-2 >= 0):
                if (board[piece[3][0]-1][piece[3][1]-2][0] == None or board[piece[3][0]-1][piece[3][1]-2][4] == "b"):
                    squares.append([piece[3][0]-1, piece[3][1]-2])

            if (piece[3][0]-1 >= 0 and piece[3][1]+2 < 8):
                if (board[piece[3][0]-1][piece[3][1]+2][0] == None or board[piece[3][0]-1][piece[3][1]+2][4] == "b"):
                    squares.append([piece[3][0]-1, piece[3][1]+2])

            if (piece[3][0]+1 < 8 and piece[3][1]+2 < 8):
                if (board[piece[3][0]+1][piece[3][1]+2][0] == None or board[piece[3][0]+1][piece[3][1]+2][4] == "b"):
                    squares.append([piece[3][0]+1, piece[3][1]+2])
            
            if (piece[3][0]+1 < 8 and piece[3][1]-2 >= 0):
                if (board[piece[3][0]+1][piece[3][1]-2][0] == None or board[piece[3][0]+1][piece[3][1]-2][4] == "b"):
                    squares.append([piece[3][0]+1, piece[3][1]-2])
            
            if (piece[3][0]+2 < 8 and piece[3][1]+1 < 8):
                if (board[piece[3][0]+2][piece[3][1]+1][0] == None or board[piece[3][0]+2][piece[3][1]+1][4] == "b"):
                    squares.append([piece[3][0]+2, piece[3][1]+1])

            if (piece[3][0]+2 < 8 and piece[3][1]-1 >= 0):
                if (board[piece[3][0]+2][piece[3][1]-1][0] == None or board[piece[3][0]+2][piece[3][1]-1][4] == "b"):
                    squares.append([piece[3][0]+2, piece[3][1]-1])

        if piece[2] == 'k':
            if (piece[3][0]-1 >= 0):
                if board[piece[3][0]-1][piece[3][1]][0] == None or board[piece[3][0]-1][piece[3][1]][4] == 'b':
                    squares.append([piece[3][0]-1, piece[3][1]])

            if (piece[3][0]+1 < 8):
                if board[piece[3][0]+1][piece[3][1]][0] == None or board[piece[3][0]+1][piece[3][1]][4] == 'b':
                    squares.append([piece[3][0]+1, piece[3][1]])

            if (piece[3][1]-1 >= 0):
                if board[piece[3][0]][piece[3][1]-1][0] == None or board[piece[3][0]][piece[3][1]-1][4] == 'b':
                    squares.append([piece[3][0], piece[3][1]-1])

            if (piece[3][1]+1 < 8):
                if board[piece[3][0]][piece[3][1]+1][0] == None or board[piece[3][0]][piece[3][1]+1][4] == 'b':
                    squares.append([piece[3][0], piece[3][1]+1])
                
            if (piece[3][0]+1 < 8 and piece[3][1]+1 < 8):
                if board[piece[3][0]+1][piece[3][1]+1][0] == None or board[piece[3][0]+1][piece[3][1]+1][4] == 'b':
                    squares.append([piece[3][0]+1, piece[3][1]+1])
                
            if (piece[3][0]+1 < 8 and piece[3][1]-1 >= 0):
                if board[piece[3][0]+1][piece[3][1]-1][0] == None or board[piece[3][0]+1][piece[3][1]-1][4] == 'b':
                    squares.append([piece[3][0]+1, piece[3][1]-1])

            if (piece[3][0]-1 >= 0 and piece[3][1]+1 < 8):
                if board[piece[3][0]-1][piece[3][1]+1][0] == None or board[piece[3][0]-1][piece[3][1]+1][4] == 'b':
                    squares.append([piece[3][0]-1, piece[3][1]+1])
                
            if (piece[3][0]-1 >= 0 and piece[3][1]-1 >= 0):
                if board[piece[3][0]-1][piece[3][1]-1][0] == None or board[piece[3][0]-1][piece[3][1]-1][4] == 'b':
                    squares.append([piece[3][0]-1, piece[3][1]-1])

            if not checkWhiteKingMove() and not checkWhiteLeftRookMove():
                if playerPosition == "front":
                    if board[7][1][0] is None and board[7][2][0] is None and board[7][3][0] is None:
                        squares.append([7, 2])

            if not checkWhiteKingMove() and not checkWhiteRightRookMove():
                if playerPosition == "front":
                    if board[7][6][0] is None and board[7][5][0] is None:
                        squares.append([7, 6])

            if not checkWhiteKingMove() and not checkWhiteLeftRookMove():
                if playerPosition == "back":
                    if board[0][1][0] is None and board[0][2][0] is None and board[0][3][0] is None:
                        squares.append([0, 2])

            if not checkWhiteKingMove() and not checkWhiteRightRookMove():
                if playerPosition == "back":
                    if board[0][6][0] is None and board[0][5][0] is None:
                        squares.append([0, 6])

        if piece[2] == 'b':
            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][0]-v >= 0 and piece[3][1]-v >= 0):
                    if board[piece[3][0]-v][piece[3][1]-v][0] == None:
                        squares.append([piece[3][0]-v, piece[3][1]-v])
                    elif board[piece[3][0]-v][piece[3][1]-v][4] == 'b':
                        squares.append([piece[3][0]-v, piece[3][1]-v])
                        di = False
                    else:
                        di = False
                else:
                    di = False

            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][0]-v >= 0 and piece[3][1]+v < 8):
                    if board[piece[3][0]-v][piece[3][1]+v][0] == None:
                        squares.append([piece[3][0]-v, piece[3][1]+v])
                    elif board[piece[3][0]-v][piece[3][1]+v][4] == 'b':
                        squares.append([piece[3][0]-v, piece[3][1]+v])
                        di = False
                    else:
                        di = False
                else:
                    di = False


            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][0]+v < 8 and piece[3][1]+v < 8):
                    if board[piece[3][0]+v][piece[3][1]+v][0] == None:
                        squares.append([piece[3][0]+v, piece[3][1]+v])
                    elif board[piece[3][0]+v][piece[3][1]+v][4] == 'b':
                        squares.append([piece[3][0]+v, piece[3][1]+v])
                        di = False
                    else:
                        di = False
                else:
                    di = False


            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][0]+v < 8 and piece[3][1]-v >= 0):
                    if board[piece[3][0]+v][piece[3][1]-v][0] == None:
                        squares.append([piece[3][0]+v, piece[3][1]-v])
                    elif board[piece[3][0]+v][piece[3][1]-v][4] == 'b':
                        squares.append([piece[3][0]+v, piece[3][1]-v])
                        di = False
                    else:
                        di = False
                else:
                    di = False

        if piece[2] == 'r':
            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][0]-v >= 0):
                    if board[piece[3][0]-v][piece[3][1]][0] == None:
                        squares.append([piece[3][0]-v, piece[3][1]])
                    elif board[piece[3][0]-v][piece[3][1]][4] == 'b':
                        squares.append([piece[3][0]-v, piece[3][1]])
                        di = False
                    else:
                        di = False
                else:
                    di = False

            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][1]+v < 8):
                    if board[piece[3][0]][piece[3][1]+v][0] == None:
                        squares.append([piece[3][0], piece[3][1]+v])
                    elif board[piece[3][0]][piece[3][1]+v][4] == 'b':
                        squares.append([piece[3][0], piece[3][1]+v])
                        di = False
                    else:
                        di = False
                else:
                    di = False


            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][0]+v < 8):
                    if board[piece[3][0]+v][piece[3][1]][0] == None:
                        squares.append([piece[3][0]+v, piece[3][1]])
                    elif board[piece[3][0]+v][piece[3][1]][4] == 'b':
                        squares.append([piece[3][0]+v, piece[3][1]])
                        di = False
                    else:
                        di = False
                else:
                    di = False


            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][1]-v >= 0):
                    if board[piece[3][0]][piece[3][1]-v][0] == None:
                        squares.append([piece[3][0], piece[3][1]-v])
                    elif board[piece[3][0]][piece[3][1]-v][4] == 'b':
                        squares.append([piece[3][0], piece[3][1]-v])
                        di = False
                    else:
                        di = False
                else:
                    di = False

        if piece[2] == 'q':

            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][0]-v >= 0):
                    if board[piece[3][0]-v][piece[3][1]][0] == None:
                        squares.append([piece[3][0]-v, piece[3][1]])
                    elif board[piece[3][0]-v][piece[3][1]][4] == 'b':
                        squares.append([piece[3][0]-v, piece[3][1]])
                        di = False
                    else:
                        di = False
                else:
                    di = False

            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][1]+v < 8):
                    if board[piece[3][0]][piece[3][1]+v][0] == None:
                        squares.append([piece[3][0], piece[3][1]+v])
                    elif board[piece[3][0]][piece[3][1]+v][4] == 'b':
                        squares.append([piece[3][0], piece[3][1]+v])
                        di = False
                    else:
                        di = False
                else:
                    di = False


            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][0]+v < 8):
                    if board[piece[3][0]+v][piece[3][1]][0] == None:
                        squares.append([piece[3][0]+v, piece[3][1]])
                    elif board[piece[3][0]+v][piece[3][1]][4] == 'b':
                        squares.append([piece[3][0]+v, piece[3][1]])
                        di = False
                    else:
                        di = False
                else:
                    di = False


            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][1]-v >= 0):
                    if board[piece[3][0]][piece[3][1]-v][0] == None:
                        squares.append([piece[3][0], piece[3][1]-v])
                    elif board[piece[3][0]][piece[3][1]-v][4] == 'b':
                        squares.append([piece[3][0], piece[3][1]-v])
                        di = False
                    else:
                        di = False
                else:
                    di = False
            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][0]-v >= 0 and piece[3][1]-v >= 0):
                    if board[piece[3][0]-v][piece[3][1]-v][0] == None:
                        squares.append([piece[3][0]-v, piece[3][1]-v])
                    elif board[piece[3][0]-v][piece[3][1]-v][4] == 'b':
                        squares.append([piece[3][0]-v, piece[3][1]-v])
                        di = False
                    else:
                        di = False
                else:
                    di = False

            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][0]-v >= 0 and piece[3][1]+v < 8):
                    if board[piece[3][0]-v][piece[3][1]+v][0] == None:
                        squares.append([piece[3][0]-v, piece[3][1]+v])
                    elif board[piece[3][0]-v][piece[3][1]+v][4] == 'b':
                        squares.append([piece[3][0]-v, piece[3][1]+v])
                        di = False
                    else:
                        di = False
                else:
                    di = False


            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][0]+v < 8 and piece[3][1]+v < 8):
                    if board[piece[3][0]+v][piece[3][1]+v][0] == None:
                        squares.append([piece[3][0]+v, piece[3][1]+v])
                    elif board[piece[3][0]+v][piece[3][1]+v][4] == 'b':
                        squares.append([piece[3][0]+v, piece[3][1]+v])
                        di = False
                    else:
                        di = False
                else:
                    di = False


            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][0]+v < 8 and piece[3][1]-v >= 0):
                    if board[piece[3][0]+v][piece[3][1]-v][0] == None:
                        squares.append([piece[3][0]+v, piece[3][1]-v])
                    elif board[piece[3][0]+v][piece[3][1]-v][4] == 'b':
                        squares.append([piece[3][0]+v, piece[3][1]-v])
                        di = False
                    else:
                        di = False
                else:
                    di = False

                    




    print(squares)
    return squares

def legalMovesBlack(piece, playerPosition):
    print("test", piece)
    squares = []
    if piece[0] != None and piece[4] == "b":

        if piece[2] == "p" and playerPosition == "front":

            if piece[3][0] == 6:
                if board[piece[3][0]-1][piece[3][1]][0] == None:
                    squares.append([piece[3][0]-1, piece[3][1]])
                if board[piece[3][0]-1][piece[3][1]][0] == None and board[piece[3][0]-2][piece[3][1]][0] == None:
                    squares.append([piece[3][0]-2, piece[3][1]])


            if (piece[3][0]-1 >= 0):
                if board[piece[3][0]-1][piece[3][1]][0] == None:
                    squares.append([piece[3][0]-1, piece[3][1]])

            
            if (piece[3][0]-1 >= 0 and piece[3][1]-1 >= 0):
                if board[piece[3][0]-1][piece[3][1]-1][0] is not None and board[piece[3][0]-1][piece[3][1]-1][4] == "w":
                    squares.append([piece[3][0]-1, piece[3][1]-1])

            if (piece[3][0]-1 >= 0 and piece[3][1]+1 < 8):
                if board[piece[3][0]-1][piece[3][1]+1][0] is not None and board[piece[3][0]-1][piece[3][1]+1][4] == "w":
                    squares.append([piece[3][0]-1, piece[3][1]+1])

            if len(preMoves) != 0:
                if (preMoves[len(preMoves)-1]["piece"][2] == "p" and abs(preMoves[len(preMoves)-1]["from"][0]-preMoves[len(preMoves)-1]["to"][0]) == 2):
                    if (piece[3][1]-preMoves[len(preMoves)-1]["to"][1] == 1 and piece[3][0]-preMoves[len(preMoves)-1]["to"][0] == 0):
                        squares.append([piece[3][0]-1, piece[3][1]-1])

                if (preMoves[len(preMoves)-1]["piece"][2] == "p" and abs(preMoves[len(preMoves)-1]["from"][0]-preMoves[len(preMoves)-1]["to"][0]) == 2):
                    if (piece[3][1]-preMoves[len(preMoves)-1]["to"][1] == -1 and piece[3][0]-preMoves[len(preMoves)-1]["to"][0] == 0):
                        squares.append([piece[3][0]-1, piece[3][1]+1])

        if piece[2] == "p" and playerPosition == "back":

            if piece[3][0] == 1:
                if board[piece[3][0]+1][piece[3][1]][0] == None:
                    squares.append([piece[3][0]+1, piece[3][1]])
                if board[piece[3][0]+1][piece[3][1]][0] == None and board[piece[3][0]+2][piece[3][1]][0] == None:
                    squares.append([piece[3][0]+2, piece[3][1]])


            if (piece[3][0]+1 < 8):
                if board[piece[3][0]+1][piece[3][1]][0] == None:
                    squares.append([piece[3][0]+1, piece[3][1]])

            
            if (piece[3][0]+1 < 8 and piece[3][1]-1 >= 0):
                if board[piece[3][0]+1][piece[3][1]-1][0] is not None and board[piece[3][0]+1][piece[3][1]-1][4] == "w":
                    squares.append([piece[3][0]+1, piece[3][1]-1])

            if (piece[3][0]+1 < 8 and piece[3][1]+1 < 8):
                if board[piece[3][0]+1][piece[3][1]+1][0] is not None and board[piece[3][0]+1][piece[3][1]+1][4] == "w":
                    squares.append([piece[3][0]+1, piece[3][1]+1])

            if len(preMoves) != 0:
                if (preMoves[len(preMoves)-1]["piece"][2] == "p" and abs(preMoves[len(preMoves)-1]["from"][0]-preMoves[len(preMoves)-1]["to"][0]) == 2):
                    if (piece[3][1]-preMoves[len(preMoves)-1]["to"][1] == 1 and piece[3][0]-preMoves[len(preMoves)-1]["to"][0] == 0):
                        squares.append([piece[3][0]+1, piece[3][1]-1])

                if (preMoves[len(preMoves)-1]["piece"][2] == "p" and abs(preMoves[len(preMoves)-1]["from"][0]-preMoves[len(preMoves)-1]["to"][0]) == 2):
                    if (piece[3][1]-preMoves[len(preMoves)-1]["to"][1] == -1 and piece[3][0]-preMoves[len(preMoves)-1]["to"][0] == 0):
                        squares.append([piece[3][0]+1, piece[3][1]+1])

        if piece[2] == 'n':
            if (piece[3][0]-2 >= 0 and piece[3][1]-1 >= 0):
                if (board[piece[3][0]-2][piece[3][1]-1][0] == None or board[piece[3][0]-2][piece[3][1]-1][4] == "w"):
                    squares.append([piece[3][0]-2, piece[3][1]-1])

            if (piece[3][0]-2 >= 0 and piece[3][1]+1 < 8):
                if (board[piece[3][0]-2][piece[3][1]+1][0] == None or board[piece[3][0]-2][piece[3][1]+1][4] == "w"):
                    squares.append([piece[3][0]-2, piece[3][1]+1])

            if (piece[3][0]-1 >= 0 and piece[3][1]-2 >= 0):
                if (board[piece[3][0]-1][piece[3][1]-2][0] == None or board[piece[3][0]-1][piece[3][1]-2][4] == "w"):
                    squares.append([piece[3][0]-1, piece[3][1]-2])

            if (piece[3][0]-1 >= 0 and piece[3][1]+2 < 8):
                if (board[piece[3][0]-1][piece[3][1]+2][0] == None or board[piece[3][0]-1][piece[3][1]+2][4] == "w"):
                    squares.append([piece[3][0]-1, piece[3][1]+2])

            if (piece[3][0]+1 < 8 and piece[3][1]+2 < 8):
                if (board[piece[3][0]+1][piece[3][1]+2][0] == None or board[piece[3][0]+1][piece[3][1]+2][4] == "w"):
                    squares.append([piece[3][0]+1, piece[3][1]+2])
            
            if (piece[3][0]+1 < 8 and piece[3][1]-2 >= 0):
                if (board[piece[3][0]+1][piece[3][1]-2][0] == None or board[piece[3][0]+1][piece[3][1]-2][4] == "w"):
                    squares.append([piece[3][0]+1, piece[3][1]-2])
            
            if (piece[3][0]+2 < 8 and piece[3][1]+1 < 8):
                if (board[piece[3][0]+2][piece[3][1]+1][0] == None or board[piece[3][0]+2][piece[3][1]+1][4] == "w"):
                    squares.append([piece[3][0]+2, piece[3][1]+1])

            if (piece[3][0]+2 < 8 and piece[3][1]-1 >= 0):
                if (board[piece[3][0]+2][piece[3][1]-1][0] == None or board[piece[3][0]+2][piece[3][1]-1][4] == "w"):
                    squares.append([piece[3][0]+2, piece[3][1]-1])

        if piece[2] == 'k':
            if (piece[3][0]-1 >= 0):
                if board[piece[3][0]-1][piece[3][1]][0] == None or board[piece[3][0]-1][piece[3][1]][4] == 'w':
                    squares.append([piece[3][0]-1, piece[3][1]])

            if (piece[3][0]+1 < 8):
                if board[piece[3][0]+1][piece[3][1]][0] == None or board[piece[3][0]+1][piece[3][1]][4] == 'w':
                    squares.append([piece[3][0]+1, piece[3][1]])

            if (piece[3][1]-1 >= 0):
                if board[piece[3][0]][piece[3][1]-1][0] == None or board[piece[3][0]][piece[3][1]-1][4] == 'w':
                    squares.append([piece[3][0], piece[3][1]-1])

            if (piece[3][1]+1 < 8):
                if board[piece[3][0]][piece[3][1]+1][0] == None or board[piece[3][0]][piece[3][1]+1][4] == 'w':
                    squares.append([piece[3][0], piece[3][1]+1])
                
            if (piece[3][0]+1 < 8 and piece[3][1]+1 < 8):
                if board[piece[3][0]+1][piece[3][1]+1][0] == None or board[piece[3][0]+1][piece[3][1]+1][4] == 'w':
                    squares.append([piece[3][0]+1, piece[3][1]+1])
                
            if (piece[3][0]+1 < 8 and piece[3][1]-1 >= 0):
                if board[piece[3][0]+1][piece[3][1]-1][0] == None or board[piece[3][0]+1][piece[3][1]-1][4] == 'w':
                    squares.append([piece[3][0]+1, piece[3][1]-1])

            if (piece[3][0]-1 >= 0 and piece[3][1]+1 < 8):
                if board[piece[3][0]-1][piece[3][1]+1][0] == None or board[piece[3][0]-1][piece[3][1]+1][4] == 'w':
                    squares.append([piece[3][0]-1, piece[3][1]+1])
                
            if (piece[3][0]-1 >= 0 and piece[3][1]-1 >= 0):
                if board[piece[3][0]-1][piece[3][1]-1][0] == None or board[piece[3][0]-1][piece[3][1]-1][4] == 'w':
                    squares.append([piece[3][0]-1, piece[3][1]-1])

            if not checkBlackKingMove() and not checkBlackLeftRookMove():
                if playerPosition == "front":
                    if board[7][1][0] is None and board[7][2][0] is None:
                        squares.append([7, 1])

            if not checkBlackKingMove() and not checkBlackRightRookMove():
                if playerPosition == "front":
                    if board[7][6][0] is None and board[7][5][0] is None and board[7][4][0] is None:
                        squares.append([7, 5])

            if not checkBlackKingMove() and not checkBlackLeftRookMove():
                if playerPosition == "back":
                    if board[0][1][0] is None and board[0][2][0] is None and board[0][3][0] is None:
                        squares.append([0, 2])

            if not checkBlackKingMove() and not checkBlackRightRookMove():
                if playerPosition == "back":
                    if board[0][6][0] is None and board[0][5][0] is None:
                        squares.append([0, 6])

        if piece[2] == 'b':
            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][0]-v >= 0 and piece[3][1]-v >= 0):
                    if board[piece[3][0]-v][piece[3][1]-v][0] == None:
                        squares.append([piece[3][0]-v, piece[3][1]-v])
                    elif board[piece[3][0]-v][piece[3][1]-v][4] == 'w':
                        squares.append([piece[3][0]-v, piece[3][1]-v])
                        di = False
                    else:
                        di = False
                else:
                    di = False

            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][0]-v >= 0 and piece[3][1]+v < 8):
                    if board[piece[3][0]-v][piece[3][1]+v][0] == None:
                        squares.append([piece[3][0]-v, piece[3][1]+v])
                    elif board[piece[3][0]-v][piece[3][1]+v][4] == 'w':
                        squares.append([piece[3][0]-v, piece[3][1]+v])
                        di = False
                    else:
                        di = False
                else:
                    di = False


            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][0]+v < 8 and piece[3][1]+v < 8):
                    if board[piece[3][0]+v][piece[3][1]+v][0] == None:
                        squares.append([piece[3][0]+v, piece[3][1]+v])
                    elif board[piece[3][0]+v][piece[3][1]+v][4] == 'w':
                        squares.append([piece[3][0]+v, piece[3][1]+v])
                        di = False
                    else:
                        di = False
                else:
                    di = False


            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][0]+v < 8 and piece[3][1]-v >= 0):
                    if board[piece[3][0]+v][piece[3][1]-v][0] == None:
                        squares.append([piece[3][0]+v, piece[3][1]-v])
                    elif board[piece[3][0]+v][piece[3][1]-v][4] == 'w':
                        squares.append([piece[3][0]+v, piece[3][1]-v])
                        di = False
                    else:
                        di = False
                else:
                    di = False

        if piece[2] == 'r':
            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][0]-v >= 0):
                    if board[piece[3][0]-v][piece[3][1]][0] == None:
                        squares.append([piece[3][0]-v, piece[3][1]])
                    elif board[piece[3][0]-v][piece[3][1]][4] == 'w':
                        squares.append([piece[3][0]-v, piece[3][1]])
                        di = False
                    else:
                        di = False
                else:
                    di = False

            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][1]+v < 8):
                    if board[piece[3][0]][piece[3][1]+v][0] == None:
                        squares.append([piece[3][0], piece[3][1]+v])
                    elif board[piece[3][0]][piece[3][1]+v][4] == 'w':
                        squares.append([piece[3][0], piece[3][1]+v])
                        di = False
                    else:
                        di = False
                else:
                    di = False


            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][0]+v < 8):
                    if board[piece[3][0]+v][piece[3][1]][0] == None:
                        squares.append([piece[3][0]+v, piece[3][1]])
                    elif board[piece[3][0]+v][piece[3][1]][4] == 'w':
                        squares.append([piece[3][0]+v, piece[3][1]])
                        di = False
                    else:
                        di = False
                else:
                    di = False


            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][1]-v >= 0):
                    if board[piece[3][0]][piece[3][1]-v][0] == None:
                        squares.append([piece[3][0], piece[3][1]-v])
                    elif board[piece[3][0]][piece[3][1]-v][4] == 'w':
                        squares.append([piece[3][0], piece[3][1]-v])
                        di = False
                    else:
                        di = False
                else:
                    di = False

        if piece[2] == 'q':

            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][0]-v >= 0):
                    if board[piece[3][0]-v][piece[3][1]][0] == None:
                        squares.append([piece[3][0]-v, piece[3][1]])
                    elif board[piece[3][0]-v][piece[3][1]][4] == 'w':
                        squares.append([piece[3][0]-v, piece[3][1]])
                        di = False
                    else:
                        di = False
                else:
                    di = False

            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][1]+v < 8):
                    if board[piece[3][0]][piece[3][1]+v][0] == None:
                        squares.append([piece[3][0], piece[3][1]+v])
                    elif board[piece[3][0]][piece[3][1]+v][4] == 'w':
                        squares.append([piece[3][0], piece[3][1]+v])
                        di = False
                    else:
                        di = False
                else:
                    di = False


            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][0]+v < 8):
                    if board[piece[3][0]+v][piece[3][1]][0] == None:
                        squares.append([piece[3][0]+v, piece[3][1]])
                    elif board[piece[3][0]+v][piece[3][1]][4] == 'w':
                        squares.append([piece[3][0]+v, piece[3][1]])
                        di = False
                    else:
                        di = False
                else:
                    di = False


            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][1]-v >= 0):
                    if board[piece[3][0]][piece[3][1]-v][0] == None:
                        squares.append([piece[3][0], piece[3][1]-v])
                    elif board[piece[3][0]][piece[3][1]-v][4] == 'w':
                        squares.append([piece[3][0], piece[3][1]-v])
                        di = False
                    else:
                        di = False
                else:
                    di = False
            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][0]-v >= 0 and piece[3][1]-v >= 0):
                    if board[piece[3][0]-v][piece[3][1]-v][0] == None:
                        squares.append([piece[3][0]-v, piece[3][1]-v])
                    elif board[piece[3][0]-v][piece[3][1]-v][4] == 'w':
                        squares.append([piece[3][0]-v, piece[3][1]-v])
                        di = False
                    else:
                        di = False
                else:
                    di = False

            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][0]-v >= 0 and piece[3][1]+v < 8):
                    if board[piece[3][0]-v][piece[3][1]+v][0] == None:
                        squares.append([piece[3][0]-v, piece[3][1]+v])
                    elif board[piece[3][0]-v][piece[3][1]+v][4] == 'w':
                        squares.append([piece[3][0]-v, piece[3][1]+v])
                        di = False
                    else:
                        di = False
                else:
                    di = False


            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][0]+v < 8 and piece[3][1]+v < 8):
                    if board[piece[3][0]+v][piece[3][1]+v][0] == None:
                        squares.append([piece[3][0]+v, piece[3][1]+v])
                    elif board[piece[3][0]+v][piece[3][1]+v][4] == 'w':
                        squares.append([piece[3][0]+v, piece[3][1]+v])
                        di = False
                    else:
                        di = False
                else:
                    di = False


            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][0]+v < 8 and piece[3][1]-v >= 0):
                    if board[piece[3][0]+v][piece[3][1]-v][0] == None:
                        squares.append([piece[3][0]+v, piece[3][1]-v])
                    elif board[piece[3][0]+v][piece[3][1]-v][4] == 'w':
                        squares.append([piece[3][0]+v, piece[3][1]-v])
                        di = False
                    else:
                        di = False
                else:
                    di = False


    print(squares)
    return squares


def returnPiece(x, y):
    return board[y][x]

def drawMoves(screen, squares):

    if len(squares) != 0:

        RED = (255, 0, 0)
        # Create a new Surface with the size of the rectangle you want to draw
        rect_surface = pygame.Surface((100, 100))

        # Fill the new Surface with the color you want (here, WHITE)
        rect_surface.fill(RED)

        # Set the alpha value of the Surface (0 is fully transparent, 255 is opaque)
        rect_surface.set_alpha(128)  # Semi-transparent

        for x in squares:
            screen.blit(rect_surface, (x[1]*100, x[0]*100))

    pygame.display.flip()

def playerMoved(index, piece):
    global preMoves, id

    if index[0] == 0 and piece[2] == "p" and piece[4] == "w":
        piece[0] = wqueen
        piece[1] = 9
        piece[2] = 'q'

    if index[0] == 0 and piece[2] == "p" and piece[4] == "b":
        piece[0] = bqueen
        piece[1] = 9
        piece[2] = 'q'

    if index[0] == 7 and piece[2] == "p" and piece[4] == "b":
        piece[0] = bqueen
        piece[1] = 9
        piece[2] = 'q'

    if index[0] == 7 and piece[2] == "p" and piece[4] == "w":
        piece[0] = wqueen
        piece[1] = 9
        piece[2] = 'q'




    current_piece = piece[3]
    board[current_piece[0]][current_piece[1]] = [None]
    piece[3] = index
    oldPiece = board[index[0]][index[1]]
    board[index[0]][index[1]] = piece

    if piece[2] == "k" and piece[4] == "w" and current_piece[1]-index[1] == 2:
        print("cas")
        rookShort = returnPiece(current_piece[1]-4, current_piece[0])
        
        current_rook = rookShort[3]
        board[current_rook[0]][current_rook[1]] = [None]
        rookShort[3] = [piece[3][0], piece[3][1]+1]
        board[piece[3][0]][piece[3][1]+1] = rookShort

    if piece[2] == "k" and piece[4] == "w" and index[1]-current_piece[1] == 2:
        print("cas")
        rookShort = returnPiece(current_piece[1]+3, current_piece[0])
        
        current_rook = rookShort[3]
        board[current_rook[0]][current_rook[1]] = [None]
        rookShort[3] = [piece[3][0], piece[3][1]-1]
        board[piece[3][0]][piece[3][1]-1] = rookShort

    if piece[2] == "k" and piece[4] == "b" and index[1]-current_piece[1] == 2:
        print("cas")
        rookShort = returnPiece(current_piece[1]+4, current_piece[0])
        
        current_rook = rookShort[3]
        board[current_rook[0]][current_rook[1]] = [None]
        rookShort[3] = [piece[3][0], piece[3][1]-1]
        board[piece[3][0]][piece[3][1]-1] = rookShort

    if piece[2] == "k" and piece[4] == "b" and current_piece[1]-index[1] == 2:
        print("cas")
        print("short")
        rookShort = returnPiece(current_piece[1]-3, current_piece[0])
        print(rookShort)
        current_rook = rookShort[3]
        board[current_rook[0]][current_rook[1]] = [None]
        rookShort[3] = [piece[3][0], piece[3][1]+1]
        board[piece[3][0]][piece[3][1]+1] = rookShort

    if len(preMoves) != 0:
        if oldPiece[0] is None and piece[2] == "p" and current_piece[1]-index[1] != 0:
            if current_piece[0] - index[0] == -1:
                print("enpassant")
                print([index[0]-1, index[1]])
                board[index[0]-1][index[1]] = [None]
            if index[0] - current_piece[0] == -1:
                print("enpassant")
                print([index[0]+1, index[1]])
                board[index[0]+1][index[1]] = [None]



    preMoves.append({"id": id,
                     "piece": piece,
                     "from": current_piece,
                     "to": index})
    id += 1
    



def getBoard():
    return board