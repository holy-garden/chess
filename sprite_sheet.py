import os
import pygame


class SpriteSheet:
    def __init__(self, filename: str):
        try:
            self.sprite = pygame.image.load(os.path.join(os.path.dirname(__file__), filename))
        except FileNotFoundError as e:
            print(str(e))

    def piece_at(self, pos: tuple[int, int]):
        # Loads image from x,y,x+offset,y+offset
        image = pygame.Surface((100, 100), pygame.SRCALPHA).convert_alpha()
        image.blit(self.sprite, (0, 0), (*pos, 100, 100))
        return image

    def board_at(self):
        image = pygame.Surface((800, 800))
        image.blit(self.sprite, (0, 0))
        return image
