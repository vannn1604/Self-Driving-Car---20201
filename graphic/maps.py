import pygame
import xlrd

from graphic.loader import load_image

# Map filenames.
MAP_NAVS = [] # mảng tọa độ (x, y) của các điểm trung tâm

FINISH_INDEX = 0

TRAFFIC_LAMP_POS = [] # mảng các vị trí của đèn giao thông (là số thứ tự điểm, k phải tọa độ)
TRAFFIC_LAMP_COORDINATES = [] # mảng thông tin chi tiết của đèn tín hiệu: tọa độ x, y, hướng của đèn, index


class Map(pygame.sprite.Sprite):
    def __init__(self, init_x, init_y, map_number):
        pygame.sprite.Sprite.__init__(self)

        self.map_number = map_number
        image_temp = "map" + str(map_number) + ".png"
        self.get_map_navs()
        self.image = load_image(image_temp)
        self.rect = self.image.get_rect()
        self.x = init_x
        self.y = init_y

    # Realign the map
    def update(self, cam_x, cam_y):
        self.rect.topleft = self.x - cam_x + 600, self.y - cam_y + 300

    def get_map_navs(self):
        with xlrd.open_workbook('../media/toa-do.xlsx') as book:
            sheet = book.sheet_by_index(self.map_number - 1)

            x_coordinate = [x for x in sheet.col_values(1)] # mảng hoành độ các điểm trung tâm
            y_coordinate = [y for y in sheet.col_values(2)] # mảng tung độ các điểm trung tâm

            for i in range(1, len(x_coordinate)):
                MAP_NAVS.append((x_coordinate[i], y_coordinate[i]))

            sheet = book.sheet_by_index(self.map_number + 2)

            pos_tmp = [x for x in sheet.col_values(1)]
            for i in range(1, len(pos_tmp)):
                TRAFFIC_LAMP_POS.append(int(pos_tmp[i]))
            print("TRAFFIC LAMP POS: ", TRAFFIC_LAMP_POS) # Vị trí (index) của các đèn giao thông

            sheet = book.sheet_by_index(self.map_number + 5)
            x_coordinate = [x for x in sheet.col_values(1)]
            y_coordinate = [y for y in sheet.col_values(2)]
            direction = [direction for direction in sheet.col_values(3)]
            index = [index for index in sheet.col_values(4)]

            for i in range(1, len(x_coordinate)):
                TRAFFIC_LAMP_COORDINATES.append((x_coordinate[i], y_coordinate[i], direction[i], index[i]))

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
