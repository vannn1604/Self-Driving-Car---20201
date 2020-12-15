import pygame
from pygame.locals import *
import xlrd
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
# import graphic.maps as maps

pygame.init()
SIZE = (1133, 725)
screen = pygame.display.set_mode(SIZE)
backg = pygame.image.load('../media/map2.png')
screen.blit(backg, (0,0))
position = 0
pygame.display.update()
Running = True
MAP_FULLNAVS = []

def get_nav():
    with xlrd.open_workbook('../media/toa-do.xlsx') as book:
        sheet = book.sheet_by_index(3)
        for row_num in range(sheet.nrows):
            row_value = sheet.row_values(row_num)
            MAP_FULLNAVS.append((row_value[1], row_value[2], int(row_value[0])))
get_nav()

def get_nearest(u):
    DIS = []
    d = 0
    for nav in MAP_FULLNAVS:
        d = abs(u[0] - nav[0]) + abs(u[1] - nav[1])
        DIS.append(d)
    min_index = DIS.index(min(DIS))
    return MAP_FULLNAVS[min_index][2]

while Running:
    for evnt in pygame.event.get():
         if evnt.type == pygame.QUIT:
             Running = False
         elif evnt.type == pygame.MOUSEBUTTONDOWN:
             x, y = evnt.pos
             icon = pygame.image.load('../media/point.png')
             icon = pygame.transform.scale(icon, (30, 30))
             screen.blit(icon, (x-15, y-30))
             pygame.display.update()
             u = (x, y)
             print("({}, {})".format(x, y))
             print("nearest point index: ", get_nearest(u))