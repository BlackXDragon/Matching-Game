import pygame
import game_config as gc
from pygame import display, event, image
from animal import Animal
from time import sleep, time

pygame.init()

display.set_caption('My Game')
screen = display.set_mode((512, 512))
matched = image.load('other_assets/matched.png')
font = pygame.font.SysFont('Times New Roman', 24)

running = True
tiles = [Animal(i) for i in range(0, gc.NUM_TILES_TOTAL)]

current_images = []

def find_index(x, y):
    row = y // gc.IMAGE_SIZE
    col = x // gc.IMAGE_SIZE
    return row * gc.NUM_TILES + col

start = time()
won = False

while running:
    current_events = event.get()

    for e in current_events:
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            index = find_index(mouse_x, mouse_y)
            if not (index in current_images or tiles[index].skip):
                current_images.append(index)
                if len(current_images) > 2:
                    current_images = current_images[1:]
    
    screen.fill((255, 255, 255))
    for tile in tiles:
        if not tile.skip:
            screen.blit(tile.image if tile.index in current_images else tile.box, (tile.col * gc.IMAGE_SIZE + gc.MARGIN, tile.row * gc.IMAGE_SIZE + gc.MARGIN))

    if len(current_images) == 2:
        i1, i2 = current_images
        if tiles[i1].name == tiles[i2].name:
            tiles[i1].skip = True
            tiles[i2].skip = True
            sleep(0.4)
            screen.blit(matched, (0, 0))
            display.flip()
            sleep(0.4)
            current_images = []
    
    if sum([tile.skip for tile in tiles]) == gc.NUM_TILES_TOTAL:
        running = False
        won = True
        end = time()
    
    display.flip()

if won:
    txt1 = font.render('Great! You won!'.format(end-start), True, (0, 0, 255))
    txt2 = font.render('You took {:.2f} seconds!'.format(end-start), True, (0, 0, 255))
    txt3 = font.render('Press ESC to exit!'.format(end-start), True, (0, 0, 255))
    w1 = txt1.get_rect().w
    w3 = txt3.get_rect().w
    rect = txt2.get_rect()
    w2, h = rect.w, rect.h
    screen.fill((200, 200, 255))
    screen.blit(txt1, ((gc.SCREEN_SIZE - w1)/2, (gc.SCREEN_SIZE - 3*h)/2))
    screen.blit(txt2, ((gc.SCREEN_SIZE - w2)/2, (gc.SCREEN_SIZE - h)/2))
    screen.blit(txt3, ((gc.SCREEN_SIZE - w3)/2, (gc.SCREEN_SIZE + h)/2))
    display.flip()
    wait = True
    while wait:
        current_events = event.get()

        for e in current_events:
            if e.type == pygame.QUIT:
                wait = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    wait = False

print('Goodbye!')