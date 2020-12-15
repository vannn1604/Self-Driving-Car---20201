import pygame
import xlrd

from graphic.loader import load_image
from fuzzy_base.dijkstra import get_path

# Map filenames.
MAP_NAVS = [] # mảng tọa độ (x, y) của các điểm trung tâm
LINE_NAVS = []

FINISH_INDEX = 0

TRAFFIC_LAMP_POS = [] # mảng các vị trí của đèn giao thông (số thứ tự điểm trong chuỗi điểm đường đi - là số thứ tự điểm, k phải tọa độ)
TRAFFIC_LAMP_COORDINATES = [] # mảng thông tin chi tiết của đèn tín hiệu: tọa độ x, y, hướng của đèn, index

class Map(pygame.sprite.Sprite):
    def __init__(self, init_x, init_y, map_number):
        pygame.sprite.Sprite.__init__(self)

        self.map_number = map_number
        image_temp = "map" + str(map_number) + ".png"
        self.get_map_navs()
        self.image = load_image(image_temp)
        self.rect = self.image.get_rect()
        self.rect_w = self.rect.size[0]
        self.rect_h = self.rect.size[1]
        self.image = pygame.transform.scale(self.image, (int(self.rect_w * 6), int(self.rect_h * 6)))
        self.x = init_x
        self.y = init_y
        blue = 230, 30, 30
        point1 = 635*6, 525*6
        point2 = 165*6, 167*6
        pygame.draw.lines(self.image, blue, False, LINE_NAVS, 5)

    # Realign the map
    def update(self, cam_x, cam_y):
        self.rect.topleft = self.x - cam_x + 800, self.y - cam_y + 500

    def get_map_navs(self):
        with xlrd.open_workbook('../media/toa-do.xlsx') as book:
            listPoint, dis = get_path(82, 37)
            sheet = book.sheet_by_index(3)
            for pointid in listPoint:
                for row_num in range(sheet.nrows):
                    row_value = sheet.row_values(row_num)
                    if row_value[0] == pointid:
                        MAP_NAVS.append((row_value[1]*6, row_value[2]*6, int(row_value[0])))
                        LINE_NAVS.append((row_value[1]*6, row_value[2]*6))

            print("MAP POS: ", MAP_NAVS)  # Vị trí (index) của các đèn giao thông
            print("WAY POS: ", listPoint)  # Vị trí (index) của các đèn giao thông

            sheet = book.sheet_by_index(4) # Vị trí (tọa độ) của các đèn giao thông
            i = 0.0
            j = 0
            for pointid in listPoint:
                for row_num in range(sheet.nrows):
                    row_value = sheet.row_values(row_num)
                    if row_value[5] == pointid:
                        # TRAFFIC_LAMP_POS.append(int(row_value[5]))
                        TRAFFIC_LAMP_POS.append(listPoint.index(int(row_value[5])))
                        TRAFFIC_LAMP_COORDINATES.append((row_value[1] * 6, row_value[2] * 6, row_value[3], i))
                        i = i + 1.0
                    j = j + 1
            print("TRAFFIC LAMP POS: ", TRAFFIC_LAMP_COORDINATES) # Vị trí (index) của các đèn giao thông

    # def get_traffic_lamp_pos(self):
    #     with xlrd.open_workbook('media/toa-do.xlsx') as book:
    #         sheet = book.sheet_by_index(self.map_number + 2)
    #
    #         pos_tmp = [x for x in sheet.col_values(1)]
    #         for i in range(1, len(pos_tmp)):
    #             TRAFFIC_LAMP_POS.append(int(pos_tmp[i]))
    #         print("TRAFFIC LAMP POS: ", TRAFFIC_LAMP_POS)
    #
    #         sheet2 = book.sheet_by_index(self.map_number + 5)
    #         x_coordinate = [x for x in sheet2.col_values(1)]
    #         y_coordinate = [y for y in sheet2.col_values(2)]
    #         direction = [direction for direction in sheet2.col_values(3)]
    #         index = [index for index in sheet2.col_values(4)]
    #
    #         for i in range(1, len(x_coordinate)):
    #             TRAFFIC_LAMP_COORDINATES.append((x_coordinate[i], y_coordinate[i], direction[i], index[i]))
