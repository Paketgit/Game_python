import os
import random
import sys

import pygame


class Board:
    def __init__(self, settings, map):
        with open(settings, 'r') as f:
            datasettings = f.readlines()
            for i in range(len(datasettings)):
                datasettings[i] = datasettings[i][:-1]
        with open(map, 'r') as f:
            datamap = f.readlines()
            for i in range(len(datamap)):
                datamap[i] = datamap[i][:-1]

        self.width, self.height = [int(i) for i in datasettings[0].split()]
        self.tile_box_scale = int(datasettings[1])
        self.board = [i.split() for i in datamap]
        #print(self.width, self.height, self.tile_box_scale, self.board)

    def rander(self, screen):
        wall_image = load_image("texture\environment\wall.png")
        floor_image = load_image("texture\environment\mud.png")
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x] == '1':
                # можно сразу создавать спрайты с указанием группы
                    wall = pygame.sprite.Sprite(wall_sprites)
                    wall.image = wall_image
                    wall.rect = wall.image.get_rect()

                    # задаём случайное местоположение бомбочке
                    wall.rect.x = x * self.tile_box_scale
                    wall.rect.y = y * self.tile_box_scale
                else:
                    floor = pygame.sprite.Sprite(floor_sprites)
                    floor.image = floor_image
                    floor.rect = floor.image.get_rect()

                    # задаём случайное местоположение бомбочке
                    floor.rect.x = x * self.tile_box_scale
                    floor.rect.y = y * self.tile_box_scale
        wall_sprites.draw(screen)
        floor_sprites.draw(screen)

    def get_sreen_size(self):
        return self.width * self.tile_box_scale, self.height * self.tile_box_scale


def load_image(name, colorkey=None):
    fullname = os.path.join('.', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Player:
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.hp = 0
        self.pl_sprite = load_image("texture\entity\player\player.png")
        #self.pl = pygame.sprite.Sprite(pl_group)
        #self.pl.image = self.pl_sprite
        #self.pl.rect = self.pl.image.get_rect()
        self.pl_sprite.blit(screen, (500, -500))

    def move(self, event):
        if pygame.K_w:
            self.pos_y += 10
        if pygame.K_s:
            self.pos_y -= 10
        if pygame.K_a:
            self.pos_x -= 10
        if pygame.K_d:
            self.pos_x += 10

    def update(self):
        #pl_sprite = load_image('texture\entity\player\player_32x32.png')
        #pl.image = self.pl_sprite
        #self.pl.rect = self.pl.image.get_rect()
        #self.pl.rect.x = self.pos_x
        #self.pl.rect.y = self.pos_y
        pl_group.draw(entity_screen)




pygame.init()
board = Board('settings.txt', 'map.txt')
wall_sprites = pygame.sprite.Group()
floor_sprites = pygame.sprite.Group()
pl_group = pygame.sprite.Group()

size = width, height = board.get_sreen_size()

screen = pygame.display.set_mode(size)
entity_screen = pygame.display.set_mode(size)

screen.fill('WHITE')
player = Player(500, -500)
#board.rander(screen)

running = True
while running:
    #board.rander(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        player.move(event)
        player.update()
    pygame.display.flip()
