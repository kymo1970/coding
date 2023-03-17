import pygame
from pygame import Color
import datetime
from math import pi, cos, sin


WIDTH, HEIGHT = 600, 600
FPS = 60
PURPLE = (123, 50, 250)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
center = (WIDTH//2, HEIGHT//2)
clockRadius = 300


def numbers(number, size, position):
    font = pygame.font.SysFont("Z003", size, True, False)
    text = font.render(number, True, GREEN)
    textRect = text.get_rect(center=(position))
    mw.blit(text, textRect)


def polarToCartesian(r, theta):
    x = r * sin(pi * theta / 180)
    y = r * cos(pi * theta / 180)
    return x + WIDTH / 2, -(y - HEIGHT / 2)


pygame.init()

mw = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kymo's Designs - Analog Clock")
clock = pygame.time.Clock()


def main():
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        currentTime = datetime.datetime.now()
        microSecond = currentTime.microsecond
        second = currentTime.second
        minute = currentTime.minute
        hour = currentTime.hour
        day = currentTime.day
        month = currentTime.month
        year = currentTime.year
        weekday = currentTime.today().isoweekday()
        #calendar = currentTime.today().isocalendar()

        mw.fill(Color(0, 0, 0))
        pygame.draw.circle(mw, PURPLE, center, clockRadius - 10, 10)
        pygame.draw.circle(mw, PURPLE, center, 12)

        numbers(str(weekday), 40, (WIDTH / 2 - 220, HEIGHT / 2))

        #numbers(str(calendar[1]), 40, (WIDTH / 2 - 140, HEIGHT / 2))

        numbers(str(month), 40, (WIDTH / 2 + 140, HEIGHT / 2))

        numbers(str(day), 40, (WIDTH / 2 + 220, HEIGHT / 2))

        numbers(str(year), 40, (WIDTH / 2, HEIGHT / 2 + 160))


        for number in range(1, 13):
            numbers(str(number), 80, polarToCartesian(clockRadius - 80, number * 30))


        for number in range(0, 360, 6):
            if number % 5:
                pygame.draw.line(mw, PURPLE, polarToCartesian(clockRadius - 15, number), polarToCartesian(clockRadius - 30, number), 2)
            else:
                pygame.draw.line(mw, PURPLE, polarToCartesian(clockRadius - 15, number), polarToCartesian(clockRadius - 35, number), 6)


        # Hour Hand
        r = 250
        theta = (hour + (minute / 60) + (second / 3600) + microSecond / 3600000000) * (360 / 12)
        pygame.draw.line(mw, BLUE, center, polarToCartesian(r, theta), 15)


        # Minute Hand
        r = 300
        theta = (minute + second / 60 + microSecond / 60000000) * (360 / 60)
        pygame.draw.line(mw, BLUE, center, polarToCartesian(r, theta), 10)

        # Second Hand
        r = 340
        theta = ((second + microSecond / 1000000) * (360 / 60))
        pygame.draw.line(mw, RED, center, polarToCartesian(r, theta), 4)

        theta = (microSecond * (360 / 1000000))


        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()

main()