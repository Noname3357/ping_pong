from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y, player_width, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed
    def update_l(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 395:
            self.rect.y += self.speed

bg_color = (150, 200, 255)
window = display.set_mode((700, 500))
display.set_caption("Ping Pong")
window.fill(bg_color)

L_Player = Player("racket.png", 4, 70, 200, 20, 100)
R_Player = Player("racket.png", 4, 610, 200, 20, 100)
Ball = GameSprite("tenis_ball.png", 5, 335, 5, 30, 30)

font.init()
font = font.SysFont(None, 60)
R_win = font.render("Player 2 is WINNER!", True, "darkblue")
L_win = font.render("Player 1 is WINNER!", True, "darkblue")

ball_xSpeed = 5
ball_ySpeed = 5
clock = time.Clock()
FPS = 60
game = True
finish = ""
while game:
    if finish != True:
        window.fill(bg_color)
        R_Player.reset()
        R_Player.update_r()
        L_Player.reset()
        L_Player.update_l()
        Ball.reset()

        Ball.rect.y += ball_ySpeed
        Ball.rect.x += ball_xSpeed
        if Ball.rect.y <= 5 or Ball.rect.y >= 465:
            ball_ySpeed *= -1
        if sprite.collide_rect(Ball, L_Player) or sprite.collide_rect(Ball, R_Player):
            ball_xSpeed *= -1
        
        if Ball.rect.x <= 0:
            finish = True
            window.blit(R_win,(150, 200))
        if Ball.rect.x >= 670:
            finish = True
            window.blit(L_win,(150, 200))

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)
