import pygame
import time
from plane_sprites import *

'''初始化pygame模块'''
pygame.init()
#创建屏幕
screen = pygame.display.set_mode((480,700))

'''创建背景'''
#读取背景图片
bg = pygame.image.load('./images/background.png')

#重新绘制背景，并将图片加载进来，指定到原点位置
screen.blit(bg,(0,0))

'''创建飞机'''
#读取飞机图片
hero = pygame.image.load('./images/me1.png')

#加载飞机图片，指定到固定位置
screen.blit(hero,(240,500))


'''绘制所有图形'''
pygame.display.update()

'''创建时钟对象'''
clock = pygame.time.Clock()

# 1.定义rect记录飞机的初始位置
hero_rect = pygame.Rect(240,500,102,126)

#创建敌机的精灵
enemy = GameSprite('./images/enemy1.png')
enemy1 = GameSprite('./images/enemy1.png',2)

#创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy,enemy1)


#循环开始 -> 意味着游戏的开始！
while True:
    # 1.指定刷新频率
    clock.tick(60)

    # 2.修改飞机的位置
    hero_rect.y -= 1
    if hero_rect.y==0:
        hero_rect.y=700
    # 3.调用blit方法绘制图像

    # 3.1重新绘制背景
    screen.blit(bg,(0,0 ))

    # 3.2重新绘制飞机
    screen.blit(hero,hero_rect)

    # 3.3敌机的绘制
    #调用精灵组的update方法，精灵组中的所有对象将执行各自的update方法
    enemy_group.update()

    #调用精灵组的draw方法，需要将screen作为参数传递进去
    enemy_group.draw(screen)

    # 4.调用update方法更新显示
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

