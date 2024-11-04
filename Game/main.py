import pygame
import random
from db import create_db, update_score, get_score, update_coins, get_coins
from skins import skins, screen

create_db()

clock = pygame.time.Clock()
pygame.init()

icon = pygame.image.load('img/icon.png').convert_alpha()
pygame.display.set_icon(icon)

fireball = pygame.image.load('img/fireball.png').convert_alpha()
fireballs = []

coin = [
    pygame.image.load('img/Coin/Coin1.png').convert_alpha(),
    pygame.image.load('img/Coin/Coin2.png').convert_alpha(),
    pygame.image.load('img/Coin/Coin3.png').convert_alpha(),
    pygame.image.load('img/Coin/Coin4.png').convert_alpha(),
    pygame.image.load('img/Coin/Coin5.png').convert_alpha(),
    pygame.image.load('img/Coin/Coin6.png').convert_alpha(),
    pygame.image.load('img/Coin/Coin7.png').convert_alpha(),
    pygame.image.load('img/Coin/Coin8.png').convert_alpha(),
]
coin_in_game = []
coin_speed = 5
coin_anim_count = 0
coins = 0
coin_x = 1000
coin_y = [350, 200]

heart = pygame.image.load('img/heart.png').convert_alpha()
heart_in_start = 3
heart_x = 50

kills = 0
score = 0

add_fireball = 0

bg = pygame.image.load('img/bg.jpg').convert()
bg_x = 0

cat = pygame.image.load('img/cat.png').convert_alpha()
cat_in_game = []
cat_speed = 15

bat = pygame.image.load('img/bat.png').convert_alpha()
bat_in_game = []
bat_speed = 20

now_skin = 'base_dog'



skin_list = []

dog_speed = 8
dog_x = 150
dog_y = 280

is_jump = False
jump_count = 10

fireballs_in_start = 10

cat_time = 2000

cat_timer = pygame.USEREVENT + 1
pygame.time.set_timer(cat_timer, cat_time)

label = pygame.font.Font('fonts/main_font.ttf', 40)
lose_label = label.render("You lose!", False, (193, 196, 199))
restart_label = label.render("Play again", False, (193, 196, 199))
restart_label_rect = restart_label.get_rect(topleft=(380, 130))
shop_label = label.render('Shop', False, (193, 196, 199))
shop_label_rect = shop_label.get_rect(topleft=(380, 300))
label_score = label.render(f"Score: {score}", False, (193, 196, 199))
label_fireballs = label.render(f"Fireballs: {fireballs_in_start}", False, (193, 196, 199))
label_coins = label.render(f'Coins: {coins}', False, (193, 196, 199))
label_go_main = label.render('Back', False, (193, 196, 199))
label_go_main_rct = label_go_main.get_rect(topleft=(800, 450))
label_skins = label.render('All Skins', False, (193, 196, 199))

dog_anim_count = 0

skin_x = 50

gameplay = False

in_shop = False

run = True

insert_coin = False

while run:

    walk_right = skins[now_skin][0]

    walk_left = skins[now_skin][1]

    if gameplay:
        screen.blit(bg, (bg_x, 0))
        screen.blit(bg, (bg_x + 950, 0))

        dog_rect = walk_left[0].get_rect(topleft=(dog_x, dog_y))
        score += 0.1
        label_score = label.render(f"Score: {int(score)}", False, (193, 196, 199))
        screen.blit(label_score, (700, 30))
        label_fireballs = label.render(f"Fireballs: {fireballs_in_start}", False, (193, 196, 199))
        screen.blit(label_fireballs, (700, 80))
        label_coins = label.render(f'Coins: {coins}', False, (193, 196, 199))
        screen.blit(label_coins, (700, 130))

        heart_x = 30
        if heart_in_start >= 1:
            for i in range(heart_in_start):
                screen.blit(heart, (heart_x, 30))
                heart_x += 70
        else:
            gameplay = False
            insert_coin = True

        if cat_in_game:
            for index, i in enumerate(cat_in_game):
                screen.blit(cat, i)
                i.x -= cat_speed

                if i.x < -10:
                    cat_in_game.pop(index)

                if dog_rect.colliderect(i):
                    heart_in_start -= 1
                    cat_in_game.pop(index)

        if bat_in_game:
            for index, i in enumerate(bat_in_game):
                screen.blit(bat, i)
                i.x -= bat_speed

                if i.x < -10:
                    bat_in_game.pop(index)

                if dog_rect.colliderect(i):
                    heart_in_start -= 1
                    bat_in_game.pop(index)

        if coin_in_game:
            for index, i in enumerate(coin_in_game):
                screen.blit(coin[coin_anim_count], i)
                i.x -= coin_speed

                if i.x < -10:
                    coin_in_game.pop(index)

                if dog_rect.colliderect(i):
                    coins += 1
                    coin_in_game.pop(index)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            screen.blit(walk_left[dog_anim_count], (dog_x, dog_y))
        elif keys[pygame.K_p]:
            heart_in_start += 1
        elif keys[pygame.K_o]:
            fireballs_in_start += 1
        else:
            screen.blit(walk_right[dog_anim_count], (dog_x, dog_y))

        if keys[pygame.K_a] and dog_x > 50:
            dog_x -= dog_speed
        elif keys[pygame.K_d] and dog_x < 650:
            dog_x += dog_speed

        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
            if jump_count >= -10:
                if jump_count > 0:
                    dog_y -= (jump_count ** 2) / 2
                else:
                    dog_y += (jump_count ** 2) / 2
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 10

        if dog_anim_count == 3:
            dog_anim_count = 0
        else:
            dog_anim_count += 1

        if coin_anim_count == 7:
            coin_anim_count = 0
        else:
            coin_anim_count += 1

        bg_x -= 3

        if bg_x <= -950:
            bg_x = 0

        if fireballs:
            for index, i in enumerate(fireballs):
                screen.blit(fireball, (i.x, i.y))
                i.x += 4

                if i.x > 1000:
                    fireballs.pop(index)

                if cat_in_game:
                    for inx, item in enumerate(cat_in_game):
                        if i.colliderect(item):
                            cat_in_game.pop(inx)
                            fireballs.pop(index)
                            kills += 1
                            score += 10

                if bat_in_game:
                    for inx, item in enumerate(bat_in_game):
                        if i.colliderect(item):
                            bat_in_game.pop(inx)
                            fireballs.pop(index)
                            kills += 1
                            score += 10

        if score - add_fireball * 50 > 50:
            add_fireball += 1
            fireballs_in_start += 1
            if cat_speed < 50:
                cat_speed += 1
            if bat_speed < 80:
                bat_speed += 1.5
            if coin_speed < 40:
                coin_speed += 0.8
            if cat_time > 500:
                cat_time -= 50

    else:

        if not in_shop:
            update_score(int(score))
            score = get_score()[0]
            label_score = label.render(f"best Score: {int(score)}", False, (193, 196, 199))
            if insert_coin:
                update_coins(coins)
            insert_coin = False
            coins = get_coins()
            label_coins = label.render(f"Coins: {coins}", False, (193, 196, 199))
            screen.fill((87, 88, 89))
            screen.blit(restart_label, restart_label_rect)
            screen.blit(label_score, (380, 230))
            screen.blit(shop_label, (380, 300))
            screen.blit(label_coins, (380, 400))

        if restart_label_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and not in_shop:
            gameplay = True
            dog_x = 150
            cat_in_game.clear()
            bat_in_game.clear()
            fireballs.clear()
            coin_in_game.clear()
            bg_x = 0
            score = 0
            fireballs_in_start = 10
            heart_in_start = 3

        elif shop_label_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            in_shop = True
            screen.fill((32, 32, 32))
            screen.blit(label_go_main, (800, 450))
            screen.blit(label_skins, (380, 50))
            skin_x = 50
            for index, i in enumerate(skins):
                screen.blit(skins[i][0][0], (skin_x, 100))
                skin_list.append((skins[i][0][0].get_rect(topleft=(skin_x, 100)), i))
                skin_x += 250

        elif skin_list:
            for i in skin_list:
                if i[0].collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    now_skin = i[1]
                    in_shop = False


        elif label_go_main_rct.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            in_shop = False

    pygame.display.update()

    for i in pygame.event.get():

        if i.type == pygame.QUIT:
            run = False
            pygame.quit()

        if i.type == cat_timer:
            cat_in_game.append(cat.get_rect(topleft=(1000, 390)))
            pygame.time.set_timer(cat_timer, cat_time)

            if random.randint(1, 3) == 2:
                bat_in_game.append(bat.get_rect(topleft=(1000, 200)))

            if random.randint(1, 10) == 2:
                coin_in_game.append(coin[0].get_rect(topleft=(coin_x, random.choice(coin_y))))

        if gameplay and i.type == pygame.KEYUP and i.key == pygame.K_w and fireballs_in_start > 0:
            fireballs.append(fireball.get_rect(topleft=(dog_x + 200, dog_y + 100)))
            fireballs_in_start -= 1

    clock.tick(20)
