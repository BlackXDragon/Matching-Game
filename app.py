import pygame
import game_config as gc
from pygame import display, event, image
from animal import Animal, reset
from time import sleep, time

pygame.init()

display.set_caption('Matching Game')
screen = display.set_mode((512, 512))
matched = image.load(gc.OTHER_ASSETS_DIR+'/matched.png')
font1 = pygame.font.SysFont('Times New Roman', 24)
font2 = pygame.font.Font(gc.FONT_DIR+'/KidsAlphabet.ttf', 42)
font3 = pygame.font.Font(gc.FONT_DIR+'/dreamwish.ttf', 36)

current_images = []

def find_index(x, y):
    row = y // gc.IMAGE_SIZE
    col = x // gc.IMAGE_SIZE
    return row * gc.NUM_TILES + col


won = False
replay = True

while replay:
    running = True
    tiles = [Animal(i) for i in range(0, gc.NUM_TILES_TOTAL)]

    txt1 = font2.render('Matching Game', True, (0, 0, 255))
    txt2 = font3.render('Match the tiles!', True, (0, 0, 255))
    txt3 = font1.render('Press ENTER to start!', True, (0, 0, 255))
    txt4 = font1.render('Press ESC to exit!', True, (0, 0, 255))
    rect = txt1.get_rect()
    w1, h1 = rect.w, rect.h
    rect = txt2.get_rect()
    w2, h2 = rect.w, rect.h
    rect = txt3.get_rect()
    w3, h3 = rect.w, rect.h
    rect = txt4.get_rect()
    w4, h4 = rect.w, rect.h
    screen.fill((200, 200, 255))
    screen.blit(txt1, ((gc.SCREEN_SIZE - w1)/2, (gc.SCREEN_SIZE/2 - h1)/2))
    screen.blit(txt2, ((gc.SCREEN_SIZE - w2)/2, (gc.SCREEN_SIZE/2 + 2*h1 - h2)/2))
    screen.blit(txt3, ((gc.SCREEN_SIZE - w3)/2, (gc.SCREEN_SIZE + h3)/2))
    screen.blit(txt4, ((gc.SCREEN_SIZE - w4)/2, (gc.SCREEN_SIZE*1.5 - h4)/2))
    display.flip()
    wait = True
    while wait:
        current_events = event.get()

        for e in current_events:
            if e.type == pygame.QUIT:
                wait = False
                replay = False
                running = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    wait = False
                    replay = False
                    running = False
                if e.key == pygame.K_RETURN:
                    wait = False

    start = time()

    while running:
        current_events = event.get()

        for e in current_events:
            if e.type == pygame.QUIT:
                running = False
                replay = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    running = False
                    replay = False
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
            replay = False
            won = True
            end = time()
        
        display.flip()

    if won:
        txt1 = font1.render('Great! You won!', True, (0, 0, 255))
        txt2 = font1.render('You took {:.2f} seconds!'.format(end-start), True, (0, 0, 255))
        txt3 = font1.render('Press ESC to exit!', True, (0, 0, 255))
        txt4 = font1.render('Press ENTER to play again!', True, (0, 0, 255))
        w1 = txt1.get_rect().w
        w3 = txt3.get_rect().w
        w4 = txt4.get_rect().w
        rect = txt2.get_rect()
        w2, h = rect.w, rect.h
        screen.fill((200, 200, 255))
        screen.blit(txt1, ((gc.SCREEN_SIZE - w1)/2, (gc.SCREEN_SIZE - 3*h)/2))
        screen.blit(txt2, ((gc.SCREEN_SIZE - w2)/2, (gc.SCREEN_SIZE - h)/2))
        screen.blit(txt3, ((gc.SCREEN_SIZE - w3)/2, (gc.SCREEN_SIZE + h)/2))
        screen.blit(txt4, ((gc.SCREEN_SIZE - w4)/2, (gc.SCREEN_SIZE + 3*h)/2))
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
                    if e.key == pygame.K_RETURN:
                        print("Replay!")
                        wait = False
                        replay = True
                        reset()
                        won = False
