import random

import pygame

pygame.init()
red = (255, 255, 0)

size = (1000, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Move cube")

# 检查窗口是否关闭
cube_x = 0
cube_y = 0
cube_color = (0, 0, 0)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))  # 填充背景
    pygame.draw.rect(screen, cube_color, [cube_x, cube_y, 30, 30])
    clock = pygame.time.Clock()
    clock.tick(60)


    class MySprite(pygame.sprite.Sprite):
        def __int__(self):
            super().__init__()
            self.image = pygame.Surface([50, 50])
            self.image.fill((255, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.x = 50
            self.rect.y = 50


    my_group = pygame.sprite.Group()
    my_sprite = MySprite()
    my_group.add(my_sprite)


    class other_Sprite(pygame.sprite.Sprite):
        # 定义一个精灵类，继承自pygame.sprite.Sprite
        def __int__(self):
            super().__init__()
            self.image = pygame.Surface([50, 50])  # 定义一个高50 宽50的表面
            self.image.fill(red)  # 设置颜色
            self.rect2 = self.image.get_rect()
            self.rect2.x = 0
            self.rect2.y = 0


    other_Sprite = other_Sprite()
    my_group.add(other_Sprite)

    # 检测键盘输入
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            cube_x -= 1
            print("向左移动")
        elif event.key == pygame.K_RIGHT:
            cube_x += 1
            print("向右移动")
        elif event.key == pygame.K_DOWN:
            cube_y += 1
            print("向下移动")
        elif event.key == pygame.K_UP:
            cube_y -= 1
            print("向上移动")

    # 检测鼠标输入
    if event.type == pygame.MOUSEBUTTONDOWN:
        cube_color = (random.randint(0, 250), random.randint(0, 250), random.randint(0, 250))
        print("鼠标点击")

    pygame.display.update()
