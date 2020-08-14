import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_RIGHT = True
    elif event.key == pygame.K_LEFT:
        ship.moving_LEFT = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_RIGHT = False
    elif event.key == pygame.K_LEFT:
        ship.moving_LEFT = False


def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_setting, screen, ship, aliens, bullets):
    # 每次循环，重绘屏幕
    screen.fill(ai_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    pygame.display.flip()


# 开火
def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullet_allow:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


# 更新子弹
def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


# 创建敌人
def create_fleet(ai_settings, screen, aliens):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height

    number_alien_x = get_number_alien_x(ai_settings, alien_width)
    number_alien_y = get_number_alien_y(ai_settings, alien_height)

    for alien_num_x in range(number_alien_x):
        for alien_num_y in range(number_alien_y):
            creat_alien(ai_settings, screen, aliens, alien_num_x, alien_num_y)


# 获取x轴敌人数量
def get_number_alien_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - alien_width
    number_alien_x = int(available_space_x / alien_width)
    return number_alien_x


# 获取y轴敌人数量
def get_number_alien_y(ai_settings, alien_height):
    available_space_y = ai_settings.screen_height - alien_height
    number_alien_y = int(available_space_y / alien_height)
    return number_alien_y


# 创建一个敌人放在当前行
def creat_alien(ai_settings, screen, aliens, alien_number_x,alien_number_y):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height=alien.rect.height
    alien.x = alien_width / 4 + alien_width * alien_number_x + ai_settings.alien_distance * alien_number_x
    alien.rect.x = alien.x
    alien.y= alien_height * alien_number_y + ai_settings.alien_distance * alien_number_y
    alien.rect.y=alien.y
    aliens.add(alien)
