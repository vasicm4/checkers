import pygame

pygame.init()
screen = pygame.display.set_mode((400, 500))
pygame.display.set_caption("Checkers")
clock = pygame.time.Clock()
scoreboard = pygame.Surface((400,100))
scoreboard.fill("dark green")
# game_title = pygame.font.Font(None, 50).render("Checkers", False, "Red")

cell = 50
board = pygame.Surface((cell * 8, cell * 8))
board.fill((181, 136, 99))
for x in range(0, 8, 1):
    if x % 2 == 0:
        for y in range(0, 8, 2):
            pygame.draw.rect(board, (240, 217, 181), (x*cell, y*cell, cell, cell))
    else:
        for y in range(1, 8, 2):
            pygame.draw.rect(board, (240, 217, 181), (x*cell, y*cell, cell, cell))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        screen.blit(board, board.get_rect())
        screen.blit(scoreboard, (0,400))
    pygame.display.update()
    clock.tick(60)
