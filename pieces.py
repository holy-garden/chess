import pygame

from typing import Tuple, Self

from sprite_sheet import SpriteSheet

class Piece:
    def __init__(self, *, pos: Tuple[int], _id: int) -> None:
        self.pos = pos
        self._id = _id
        self.p_sprite = SpriteSheet(filename=r"assets/pieces.png")
        self.p_texture = self.p_sprite.piece_at(pos=pos)
        self.p_rect = self.p_texture.get_rect()

    def rook(self, *, old_pos: Tuple[int], new_pos: Tuple[int]) -> bool:
        from_x, from_y = old_pos
        to_x, to_y = new_pos
        # black and white rook
        if (from_x != to_x and from_y != to_y) or (from_y != to_y and from_x != to_x):
            return False
        elif from_x > to_x and from_y == to_y:
            for i in range(0, abs(from_x - to_x), 100):
                if from_x - i < 0:
                    return False
        elif from_x < to_x and from_y == to_y:
            for i in range(0, abs(from_x - to_x), 100):
                if from_x + i > 700:
                    return False
        elif from_x == to_x and from_y > to_y:
            for i in range(0, abs(from_y - to_y), 100):
                if from_y - i < 0:
                    return False
        elif from_x == to_x and from_y < to_y:
            for i in range(0, abs(from_y - to_y), 100):
                if from_y + i > 700:
                    return False
        return True

    def knight(self, *, old_pos: Tuple[int], new_pos: Tuple[int]) -> bool:
        from_x, from_y = old_pos
        to_x, to_y = new_pos
        # white and black knight
        if abs(from_x - to_x) == 200 and abs(from_y - to_y) == 100:
            return True
        if abs(from_y - to_y) == 200 and abs(from_x - to_x) == 100:
            return True
        return False

    def bishop(self, *, old_pos: Tuple[int], new_pos: Tuple[int]) -> bool:
        from_x, from_y = old_pos
        to_x, to_y = new_pos
        # white and black bishop:
        if abs(from_x - to_x) != abs(from_y - to_y):
            return False
        if from_x > to_x and from_y > to_y:
            for i in range(0, abs(from_x - to_x), 100):
                if from_x - i < 0 and from_y - i < 0:
                    return False
        if from_x > to_x and from_y < to_y:
            for i in range(0, abs(from_x - to_x), 100):
                if from_x - i < 0 and from_y + i > 700:
                    return False
        if from_x < to_x and from_y > to_y:
            for i in range(0, abs(from_x - to_x), 100):
                if from_x + i > 700 and from_y - i < 0:
                    return False
        if from_x < to_x and from_y < to_y:
            for i in range(0, abs(from_x - to_x), 100):
                if from_x + i > 700 and from_y + i > 800:
                    return False
        return True

    def queen(self, *, old_pos: Tuple[int], new_pos: Tuple[int]) -> bool:
        _queen = self.rook(old_pos=old_pos, new_pos=new_pos) or self.bishop(old_pos=old_pos, new_pos=new_pos) 
        if _queen:
            return True
        return False

    def king(self, *,  old_pos: Tuple[int], new_pos: Tuple[int]) -> bool:
        from_x, from_y = old_pos
        to_x, to_y = new_pos
        # white and black king
        if abs(from_x - to_x) != 100 and abs(from_y - to_y) != 100:
            return False
        return True 

    def pawn(self, *, old_pos: Tuple[int], new_pos: Tuple[int]) -> bool:
        from_x, from_y = old_pos
        to_x, to_y = new_pos
        # white pawn
        if to_y < from_y and from_x == to_x:
            # move one square up
            if from_y - to_y == 100 and from_x == to_x:
                return True
            # from starting position
            if from_y == 600 and from_x == to_x:
                # move two squares
                if from_y - to_y == 200 and from_x == to_x:
                    return True
        # black pawn
        if to_y > from_y and from_x == to_x:
            # move one square down
            if to_y - from_y == 100 and from_x == to_x:
                return True
            # from starting position
            if from_y == 100 and from_x == to_x:
                # move two squares
                if to_y - from_y == 200 and from_x == to_x:
                    return True
        return False

    def draw_piece(self, *, surface: pygame.surface.Surface) -> None:
        surface.blit(self.p_texture, self.p_rect)