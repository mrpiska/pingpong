from pygame import *

img_back = ''

win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('пингпонг')
back = 'aquamarine'
window.fill(back)


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y ,player_speed, size_y, size_x):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.rect = self.image.get_rect()
        self.speed = player_speed
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move_right(self):
        kays = key.get_pressed()
        if kays[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if kays[K_DOWN] and self.rect.y < win_width - 70:
            self.rect.y += self.speed


    def move_left(self):
        kays = key.get_pressed()
        if kays[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if kays[K_s] and self.rect.y < win_width - 70:
            self.rect.y += self.speed



racked1 = Player('racket.png', 30, 200, 4, 150, 30)
racked2 = Player('racket.png', 520, 200, 4, 150, 30)

ball = Player('tenis_ball.png', 200, 200, 4, 30, 30)



game = True
finish = False
clock = time.Clock()
FPS = 60


font.init()
font = font.Font(None, 35)

lose1 = font.render('тигрок 1 проиграл', True, 'red')
lose2 = font.render('тигрок 2 проиграл', True, 'red')


speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.fill(back)


        racked1.move_left()
        racked2.move_right()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racked1, ball) or sprite.collide_rect(racked2, ball):
            speed_x *= -1
            speed_y *= -1

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x > win_height:
            finish = True
            window.blit(lose2, (200, 200))
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))



        ball.reset()
        racked1.reset()
        racked2.reset()


    display.update()
    clock.tick(FPS)






















