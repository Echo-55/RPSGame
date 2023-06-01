import os
import random

import pygame as pg
from pygame.locals import *

WINDOWX = 1920 / 2
WINDOWY = 1080 / 2

pg.init()
pg.font.init()

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")


def load_image(name, colorkey=None, scale=1):
    fullname = os.path.join(data_dir, name)
    image = pg.image.load(fullname)

    size = image.get_size()
    size = (size[0] * scale, size[1] * scale)
    image = pg.transform.scale(image, size)

    image = image.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pg.RLEACCEL)
    return image, image.get_rect()


def load_sound(name):
    class NoneSound:
        def play(self):
            pass

    if not pg.mixer or not pg.mixer.get_init():
        return NoneSound()

    fullname = os.path.join(data_dir, name)
    sound = pg.mixer.Sound(fullname)

    return sound


class Rock(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("rock.png", -1, 0.2)
        self.rock_offset = (-235, -80)
        screen = pg.display.get_surface()
        self.area = screen.get_rect()

    def update(self):
        self.x_speed = 1
        self.y_speed = 1

    def move(self, x, y):
        pass


class Paper(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("paper.png", -1, 0.2)
        self.paper_offset = (-235, -80)
        screen = pg.display.get_surface()
        self.area = screen.get_rect()

    def update(self):
        self.x_speed = 1
        self.y_speed = 1
        # self.rect.x += self.x_speed
        # self.rect.y += self.y_speed
        # self.rect.x = random.randrange(300)
        # self.rect.y = random.randrange(300)

    def move(self, x, y):
        pass


class Scissors(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("scissors.png", -1, 0.2)
        # self.scissors_offset = (235, 80)
        self.scissors_offset = (0, 0)
        screen = pg.display.get_surface()
        self.area = screen.get_rect()

    def update(self):
        self.x_speed = 1
        self.y_speed = 1

    def move(self, x, y):
        pass


def main():
    pg.init()
    screen = pg.display.set_mode((WINDOWX, WINDOWY), pg.SCALED)
    pg.display.set_caption("Rock, Paper, Scissors Battlefield")
    # pg.mouse.set_visible(False)

    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((170, 238, 187))
    screen.blit(background, (0, 0))
    pg.display.flip()

    # rock = Rock()
    # paper = Paper()
    # scissors = Scissors()
    # all_sprites = pg.sprite.RenderPlain((rock, paper, scissors))

    all_sprites = []
    rock_sprites = []
    paper_sprites = []
    scissors_sprites = []

    for i in range(5):
        i = Rock()
        i.rect.x = random.randint(400, 550)
        i.rect.y = random.randint(350, 450)
        rock_sprites.append(i)
    for i in range(5):
        i = Paper()
        i.rect.x = random.randint(100, 300)
        i.rect.y = random.randint(100, 250)
        paper_sprites.append(i)
    for i in range(5):
        i = Scissors()
        i.rect.x = random.randint(500, 700)
        i.rect.y = random.randint(50, 200)
        scissors_sprites.append(i)

    rock_group = pg.sprite.Group(rock_sprites)
    paper_group = pg.sprite.Group(paper_sprites)
    scissors_group = pg.sprite.Group(scissors_sprites)

    all_sprites_list = pg.sprite.Group()
    all_sprites_list.add(rock_group, paper_group, scissors_group)

    clock = pg.time.Clock()

    direction = 1
    speed_x = 1
    speed_y = 0.5
    screen_w, screen_h = pg.display.get_surface().get_size()
    print(screen_w, screen_h)

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False

        for i in rock_group:
            if i.rect.left <= 20 or i.rect.right >= 940:
                direction *= 1
                # speed_x = random.randint(0, 8) * direction
                # speed_y = random.randint(0, 8) * direction
                speed_x = 1 * direction
                speed_y = 1 * direction
                if speed_x == 0 and speed_y == 0:
                    # speed_x = random.randint(0, 8) * direction
                    # speed_y = random.randint(0, 8) * direction
                    speed_x = 1 * direction
                    speed_y = 1 * direction
            if i.rect.top <= 20 or i.rect.bottom >= 540:
                direction *= -1
                # speed_x = random.randint(0, 8) * direction
                # speed_y = random.randint(0, 8) * direction
                speed_x = 1 * direction
                speed_y = 1 * direction
                if speed_x == 0 and speed_y == 0:
                    # speed_x = random.randint(2, 8) * direction
                    # speed_y = random.randint(2, 8) * direction
                    speed_x = 1 * direction
                    speed_y = 1 * direction
            i.rect.left += speed_x
            i.rect.top += speed_y
            rp_hit_list = pg.sprite.spritecollide(i, paper_group, False)
            rs_hit_list = pg.sprite.spritecollide(i, scissors_group, False)

        for i in paper_group:
            pr_hit_list = []
            ps_hit_list = []

        for i in scissors_group:
            sr_hit_list = []
            sp_hit_list = []

        all_sprites_list.update()

        screen.blit(background, (0, 0))
        all_sprites_list.draw(screen)
        pg.display.flip()
        clock.tick(60)

    pg.quit()


if __name__ == "__main__":
    main()
