import math
import pygame
import random

pygame.init()
WIDTH = 1100
HEIGHT = 900
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Slither')
clock = pygame.time.Clock()
soundObj = pygame.mixer.Sound('slither/POP - Sound Effect.wav')
soundObj.set_volume(1)


class Slither:
    def __init__(self, x, y, color, radius):
        self.x = [x]
        self.y = [y]
        self.radius = radius
        self.length = 1
        self.color = color
        self.score = 0

    def move(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        mouse_position = pygame.mouse.get_pos()
        dx = mouse_position[0] - self.x[0]
        dy = mouse_position[1] - self.y[0]
        angle = math.atan2(dx, dy)
        mvx = math.sin(angle)
        mvy = math.cos(angle)
        self.x[0] += mvx
        self.y[0] += mvy

        pygame.display.flip()
        pygame.display.update()

    def draw(self):
        win.fill((60, 60, 60))
        for i in range(self.length):
            pygame.draw.circle(win, self.color, (self.x[i], self.y[i]), self.radius)

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)
        pygame.display.update()


class Ball:
    def __init__(self, radius):
        self.x = random.randrange(0, win.get_width())
        self.y = random.randrange(0, win.get_height())
        self.balls = []
        self.radius = radius

    def move(self):
        for _ in range(50):
            self.balls.append(Ball(3))

    def draw(self):
        r = random.randrange(0, 255)
        g = random.randrange(0, 255)
        b = random.randrange(0, 255)

        for j in self.balls:
            j.draw()
            if col(s.x[0], s.y[0], s.radius, j.x, j.y, j.radius) or col(s.x[0], s.y[0], s.radius, self.x, self.y,
                                                                        self.radius):
                s.increase_length()
                self.balls.remove(j)
                s.score += 1
                soundObj.play()

        pygame.draw.circle(win, (r, g, b), (self.x, self.y), 3)


def col(c1x, c1y, c1r, c2x, c2y, c2r):
    distX = c1x - c2x
    distY = c1y - c2y
    distance = math.sqrt((distX * distX) + (distY * distY))
    if (distance <= c1r + c2r):
        return True
    return False


s = Slither(50, 50, (255, 0, 0), 10)
b = Ball(3)


def redrawWindow():
    myfont = pygame.font.SysFont("monospace", 30)
    label = myfont.render(f"Score: {s.score}", 1, (0, 0, 0))
    win.blit(label, (900, 20))

    text = myfont.render("Generate", 1, (0, 0, 0))
    pygame.draw.rect(win, (100, 150, 250), [900, 70, 150, 40])
    win.blit(text, (900, 70))


def check_btn():
    mouse = pygame.mouse.get_pos()
    pygame.display.update()
    if 900 <= mouse[0] <= 900 + 150 and 70 <= mouse[1] <= 70 + 40:
        g.gen()
        return True
    return False


class Game:
    def __init__(self):
        b.move()
        b.x = 0
        b.y = 0

    def gen(self):
        for _ in range(500):
            b.balls.append(Ball(3))

        for j in b.balls:
            j.draw()
        pygame.display.update()

    def main(self):
        run = True
        while run:
            redrawWindow()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    check_btn()

            s.move()
            s.draw()
            b.draw()

            clock.tick(150)
        pygame.quit()


if __name__ == '__main__':
    g = Game()
    g.main()
