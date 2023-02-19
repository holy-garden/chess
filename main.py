import pygame

from board import Board

pygame.init()
surface = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Chess')


dragged = False
dir_x, dir_y = 0, 0
n = 0
old_pos = None
new_pos = None

clock = pygame.time.Clock()

board = Board()
board.initialize_board()
pieces = board.pieces

while True:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i, piece in enumerate(pieces):
                    if piece.p_rect.collidepoint(event.pos):
                        # Start dragging the piece
                        dragged = True
                        n = i
                        dir_x = mouse_x - piece.p_rect.x
                        dir_y = mouse_y - piece.p_rect.y
                        old_pos = (piece.p_rect.x, piece.p_rect.y)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragged = False
                px = pieces[n].p_rect.x + 100 / 2
                py = pieces[n].p_rect.y + 100 / 2
                new_pos = (100 * (int(px / 100)), 100 * (int(py / 100)))
                # move the piece
                board.make_move(old_pos=old_pos, new_pos=new_pos)
                for i in range(8):
                    for j in range(8):
                        p = pieces[i * 8 + j]
                        print(p._id, end=" ")
                    print()
                print()
        elif event.type == pygame.MOUSEMOTION:
            if dragged:
                rect = pygame.Rect(mouse_x - dir_x, mouse_y - dir_y, 100, 100)
                pieces[n].p_rect = rect
    board.draw_board(surface=surface)
    clock = pygame.time.Clock()
    pygame.display.flip()
