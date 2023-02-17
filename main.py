import pygame;

pygame.init();


screen_width, screen_height = 600, 600;
screen = pygame.display.set_mode((screen_width, screen_height));
clock = pygame.time.Clock();
timer = 0;
i = 0;


def draw_lines():
    pygame.draw.line(screen, (255, 0, 0), (screen_width // 2, 0), (screen_width // 2, screen_height), 5)
    pygame.draw.line(screen, (255, 0, 0), (0, screen_height // 2), (screen_width, screen_height // 2), 5)


def draw_point(m, x, b):
    funcY = m * x + b
    funcX = x
    pygame.draw.circle(screen, (255, 0, 0), ( screen_width // 2 + funcX, screen_height // 2 - funcY), 5)
    return funcX, funcY




run = True;
screen.fill((255, 255, 255));
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            run = False;
    

    
    timer +=1;
    

    
    draw_lines()
    if (timer > 1):
        timer = 0;
        i += 1;
        draw_point(1, i, 0)
    
        
    pygame.display.update();
    clock.tick(60);