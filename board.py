import pygame

from pieces import Piece
from sprite_sheet import SpriteSheet

class Board:
    def __init__(self) -> None:
        self.sprite_sheet = SpriteSheet(filename=r'assets/board.jpg')
        self.board_texture = self.sprite_sheet.board_at()

        self.pieces: list = []
        self.dummy_board = [
            [5, 4, 3, 1, 2, 3, 4, 5],
            [6, 6, 6, 6, 6, 6, 6, 6],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [-6,-6,-6,-6,-6,-6,-6,-6],
            [-5,-4,-3,-1,-2,-3,-4,-5],
        ]

    def initialize_board(self) -> None:
        for i in range(8):
            for j in range(8):
                # get piece id 
                n = self.dummy_board[i][j]
                # x coordinates (white pieces)
                x = abs(n) - 1
                # y coordinates (1/0 white/black pieces)
                y = 1 if n > 0 else 0
                # create piece
                piece = Piece(pos=(x * 100, y * 100), _id=n)
                # update the pieces' rects position
                piece.p_rect.x = j * 100
                piece.p_rect.y = i * 100
                # add piece
                self.pieces.append(piece)

    def is_position_empty(self, *, pos: tuple[int]) -> bool:
        for piece in self.pieces:
            if piece.p_rect == pygame.Rect(*pos, 100, 100):
                return False
        return True

    def make_move(self, *, old_pos: tuple[int], new_pos: tuple[int]) -> None:
        old_index = (old_pos[1] // 100) * 8 + (old_pos[0] // 100)
        new_index = (new_pos[1] // 100) * 8 + (new_pos[0] // 100)
        if self.is_valid_move(old_pos=old_pos, new_pos=new_pos):
            piece_at_old_pos = self.pieces[old_index]
            piece_at_new_pos = self.pieces[new_index]

            self.pieces[old_index], self.pieces[new_index] = self.pieces[new_index], self.pieces[old_index]
            self.pieces[new_index].p_rect = pygame.Rect(*new_pos, 100, 100)
            # del self.pieces[old_index]
            # self.pieces[new_index] = piece
            # self.pieces[new_index].p_rect = pygame.Rect(*new_pos, 100, 100)
        else:
            self.pieces[old_index].p_rect = pygame.Rect(*old_pos, 100, 100)

    def is_within_bounds(self, *, new_pos: tuple[int]) -> bool:
        to_x, to_y = new_pos
        if to_x < 0 or to_x > 700:
            return False
        if to_y < 0 or to_y > 700:
            return False
        return True

    def is_valid_move(self, *, old_pos: tuple[int], new_pos: tuple[int]) -> bool:
        old_index = (old_pos[1] // 100) * 8 + (old_pos[0] // 100)
        new_index = (new_pos[1] // 100) * 8 + (new_pos[0] // 100)
        if self.is_within_bounds(new_pos=new_pos):
            piece: Piece = self.pieces[old_index]
            if abs(piece._id) == 6 and piece.pawn(old_pos=old_pos, new_pos=new_pos):    return True
            if abs(piece._id) == 4 and piece.knight(old_pos=old_pos, new_pos=new_pos):  return True
            if abs(piece._id) == 3 and piece.bishop(old_pos=old_pos, new_pos=new_pos):  return True
            if abs(piece._id) == 5 and piece.rook(old_pos=old_pos, new_pos=new_pos):    return True
            if abs(piece._id) == 2 and piece.queen(old_pos=old_pos, new_pos=new_pos):   return True
            if abs(piece._id) == 1 and piece.king(old_pos=old_pos, new_pos=new_pos):    return True
        return False

    def capture(self, * new_pos: tuple[int]):
        pass

    def draw_board(self, *, surface: pygame.surface) -> None:
        surface.blit(self.board_texture, (0, 0))
        for piece in self.pieces:
            piece.draw_piece(surface=surface)