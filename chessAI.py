import random
import drawBoard

moves = []

white_pieces = []
black_pieces = []


def getColorPieces(board):
    global white_pieces, black_pieces

    white_pieces = []
    black_pieces = []
    for row in board:
        for piece in row:
            if piece[0] is not None and piece[4] == 'w':  # Check if the piece exists and is white
                white_pieces.append(piece)

    for row in board:
        for piece in row:
            if piece[0] is not None and piece[4] == 'b':  # Check if the piece exists and is white
                black_pieces.append(piece)




def move(board, ai_color, screen, BLACK, WHITE):
    global moves

    moves = []

    random_white_piece = None
    random_black_piece = None

    getColorPieces(board)

    while len(moves) == 0:
        if ai_color == "White":
            random_white_piece = random.choice(white_pieces)
            moves = drawBoard.legalMovesWhite(random_white_piece, "back")
        elif ai_color == "Black":  
            random_black_piece = random.choice(black_pieces)
            moves = drawBoard.legalMovesBlack(random_black_piece, "back")

    print("We are moving: ", random_white_piece, moves)

    if ai_color == "White":
        drawBoard.playerMoved(moves[random.randint(0, len(moves) - 1)], random_white_piece)
        drawBoard.drawBlackBoard(screen, BLACK, WHITE)
    elif ai_color == "Black":  
        drawBoard.playerMoved(moves[random.randint(0, len(moves) - 1)], random_black_piece)
        drawBoard.drawWhiteBoard(screen, BLACK, WHITE) 
        
        