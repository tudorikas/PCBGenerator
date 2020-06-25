import time

import pygame

from GridData import Point

WHITE = (129, 130, 133)
GREEN = (128, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


# dict:  straightVert=1 RfromBottom=2 LfromBottom=3  RfromUp=4 LfromUp=5 straightHoriz=6
# self.road i,j,type,direction
# direction: 1 up, 2 down, 3 right, 4 left

class PcbGraphical:
    def __init__(self, numberOfColumns, widthOfCell, drawMatrix, sleepTime):
        self.numberOfColumns = numberOfColumns
        self.numberOfRows = numberOfColumns
        self.widthOfCell = widthOfCell
        self.drawMatrix = drawMatrix
        self.WIDTH = (numberOfColumns + 2) * widthOfCell
        self.HEIGHT = (numberOfColumns + 2) * widthOfCell
        self.x = 0
        self.y = 0
        self.grid = [[0 for x in range(numberOfColumns)] for y in range(numberOfColumns)]
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("PCB generator")
        self.clock = pygame.time.Clock()
        self.road = list()
        self.build_grid()
        self.sleep = sleepTime

    def build_grid(self):
        y = 0
        pygame.draw.rect(self.screen, BLUE, (10, 10, self.WIDTH - 20, self.HEIGHT - 20), 1)
        for i in range(0, self.numberOfRows):
            x = self.widthOfCell  # set x coordinate to start position
            y = y + self.widthOfCell  # start a new row
            for j in range(0, self.numberOfColumns):
                if self.drawMatrix == 1:
                    pygame.draw.line(self.screen, WHITE, [x, y], [x + self.widthOfCell, y], )  # top of cell
                    pygame.draw.line(self.screen, WHITE, [x + self.widthOfCell, y],
                                     [x + self.widthOfCell, y + self.widthOfCell])  # right of cell
                    pygame.draw.line(self.screen, WHITE, [x + self.widthOfCell, y + self.widthOfCell],
                                     [x, y + self.widthOfCell])  # bottom of cell
                    pygame.draw.line(self.screen, WHITE, [x, y + self.widthOfCell], [x, y])  # left of cell
                self.grid[i][j] = None  # add cell to grid list
                x = x + self.widthOfCell  # move cell to new position

    # def add_single_cell(self, x, y):
    #    [i, j] = self.change_coord(self.myround(y), self.myround(x))
    #    pygame.draw.rect(self.screen, GREEN, (x + (self.widthOfCell/3), y + 1, ((self.widthOfCell/3)), self.widthOfCell), 0)          # draw a single width cell
    #    #pygame.draw.rect(self.screen, GREEN, (x + 1, y + 1, self.widthOfCell - 1, self.widthOfCell - 1), 0)
    #    pygame.display.update()
    #    self.road.append((i,j))
    #    self.grid[i][j]=1

    def add_straight_vert_cell(self, x, y):
        [i, j] = self.change_coord(self.myround(y), self.myround(x))
        pygame.draw.rect(self.screen, GREEN,
                         (x + (self.widthOfCell / 3), y, ((self.widthOfCell / 3)), (self.widthOfCell / 3)),
                         0)  # draw a single width cell
        pygame.draw.rect(self.screen, GREEN,
                         (x + (self.widthOfCell / 3), y + (self.widthOfCell / 3), (self.widthOfCell / 3),
                          (self.widthOfCell / 3)),
                         0)  # draw a single width cell
        pygame.draw.rect(self.screen, GREEN,
                         (x + (self.widthOfCell / 3), y + ((self.widthOfCell / 3) * 2), (self.widthOfCell / 3),
                          (self.widthOfCell / 3)),
                         0)  # draw a single width cell

        # pygame.draw.rect(self.screen, GREEN, (x + 1, y + 1, self.widthOfCell - 1, self.widthOfCell - 1), 0)
        pygame.display.update()
        self.road.append((i, j, 1, 0))
        newPoint = Point(i, j, 1)
        self.grid[i][j] = newPoint

    def add_straight_horiz_cell(self, x, y):
        [i, j] = self.change_coord(self.myround(y), self.myround(x))
        pygame.draw.rect(self.screen, GREEN,
                         (x, y + (self.widthOfCell / 3), (self.widthOfCell / 3), (self.widthOfCell / 3)),
                         0)  # draw a single width cell
        pygame.draw.rect(self.screen, GREEN,
                         (x + (self.widthOfCell / 3), y + (self.widthOfCell / 3), (self.widthOfCell / 3),
                          (self.widthOfCell / 3)),
                         0)  # draw a single width cell
        pygame.draw.rect(self.screen, GREEN,
                         (x + (self.widthOfCell / 3) * 2, y + (self.widthOfCell / 3), (self.widthOfCell / 3),
                          (self.widthOfCell / 3)),
                         0)  # draw a single width cell

        # pygame.draw.rect(self.screen, GREEN, (x + 1, y + 1, self.widthOfCell - 1, self.widthOfCell - 1), 0)
        pygame.display.update()
        self.road.append((i, j, 6, 0))
        newPoint = Point(i, j, 6)
        self.grid[i][j] = newPoint

    def add_right_from_down_cell(self, x, y):
        [i, j] = self.change_coord(self.myround(y), self.myround(x))
        pygame.draw.rect(self.screen, GREEN,
                         (x + ((self.widthOfCell / 3) * 2), y + (self.widthOfCell / 3), (self.widthOfCell / 3),
                          (self.widthOfCell / 3)),
                         0)  # draw a single width cell
        pygame.draw.rect(self.screen, GREEN,
                         (x + (self.widthOfCell / 3), y + (self.widthOfCell / 3), (self.widthOfCell / 3),
                          (self.widthOfCell / 3)),
                         0)  # draw a single width cell
        pygame.draw.rect(self.screen, GREEN,
                         (x + (self.widthOfCell / 3), y + ((self.widthOfCell / 3) * 2), (self.widthOfCell / 3),
                          (self.widthOfCell / 3)),
                         0)  # draw a single width cell

        # pygame.draw.rect(self.screen, GREEN, (x + 1, y + 1, self.widthOfCell - 1, self.widthOfCell - 1), 0)
        pygame.display.update()
        self.road.append((i, j, 2, 0))
        newPoint = Point(i, j, 2)
        self.grid[i][j] = newPoint

    def add_left_from_down_cell(self, x, y):
        [i, j] = self.change_coord(self.myround(y), self.myround(x))
        pygame.draw.rect(self.screen, GREEN,
                         (x, y + (self.widthOfCell / 3), (self.widthOfCell / 3),
                          (self.widthOfCell / 3)),
                         0)  # draw a single width cell
        pygame.draw.rect(self.screen, GREEN,
                         (x + (self.widthOfCell / 3), y + (self.widthOfCell / 3), (self.widthOfCell / 3),
                          (self.widthOfCell / 3)),
                         0)  # draw a single width cell
        pygame.draw.rect(self.screen, GREEN,
                         (x + (self.widthOfCell / 3), y + ((self.widthOfCell / 3) * 2), (self.widthOfCell / 3),
                          (self.widthOfCell / 3)),
                         0)  # draw a single width cell

        # pygame.draw.rect(self.screen, GREEN, (x + 1, y + 1, self.widthOfCell - 1, self.widthOfCell - 1), 0)
        pygame.display.update()
        self.road.append((i, j, 3, 0))
        newPoint = Point(i, j, 3)
        self.grid[i][j] = newPoint

    def add_left_from_up_cell(self, x, y):
        [i, j] = self.change_coord(self.myround(y), self.myround(x))
        pygame.draw.rect(self.screen, GREEN,
                         (x, y + (self.widthOfCell / 3), (self.widthOfCell / 3),
                          (self.widthOfCell / 3)),
                         0)  # draw a single width cell
        pygame.draw.rect(self.screen, GREEN,
                         (x + (self.widthOfCell / 3), y + (self.widthOfCell / 3), (self.widthOfCell / 3),
                          (self.widthOfCell / 3)),
                         0)  # draw a single width cell
        pygame.draw.rect(self.screen, GREEN,
                         (x + (self.widthOfCell / 3), y, (self.widthOfCell / 3),
                          (self.widthOfCell / 3)),
                         0)  # draw a single width cell

        # pygame.draw.rect(self.screen, GREEN, (x + 1, y + 1, self.widthOfCell - 1, self.widthOfCell - 1), 0)
        pygame.display.update()
        self.road.append((i, j, 5, 0))
        newPoint = Point(i, j, 5)
        self.grid[i][j] = newPoint

    def add_right_from_up_cell(self, x, y):
        [i, j] = self.change_coord(self.myround(y), self.myround(x))
        pygame.draw.rect(self.screen, GREEN,
                         (x + ((self.widthOfCell / 3) * 2), y + (self.widthOfCell / 3), (self.widthOfCell / 3),
                          (self.widthOfCell / 3)),
                         0)  # draw a single width cell
        pygame.draw.rect(self.screen, GREEN,
                         (x + (self.widthOfCell / 3), y + (self.widthOfCell / 3), (self.widthOfCell / 3),
                          (self.widthOfCell / 3)),
                         0)  # draw a single width cell
        pygame.draw.rect(self.screen, GREEN,
                         (x + (self.widthOfCell / 3), y, (self.widthOfCell / 3),
                          (self.widthOfCell / 3)),
                         0)  # draw a single width cell

        # pygame.draw.rect(self.screen, GREEN, (x + 1, y + 1, self.widthOfCell - 1, self.widthOfCell - 1), 0)
        pygame.display.update()
        self.road.append((i, j, 4, 0))
        newPoint = Point(i, j, 4)
        self.grid[i][j] = newPoint

    # First element


    def draw_fist_element(self, i, j, direction):

        x, y = self.change_coord_intoxy(i, j)
        pygame.draw.line(self.screen, RED, [x, y], [x + self.widthOfCell, y], )  # top of cell
        pygame.draw.line(self.screen, RED, [x + self.widthOfCell, y],
                         [x + self.widthOfCell, y + self.widthOfCell])  # right of cell
        pygame.draw.line(self.screen, RED, [x + self.widthOfCell, y + self.widthOfCell],
                         [x, y + self.widthOfCell])  # bottom of cell
        pygame.draw.line(self.screen, RED, [x, y + self.widthOfCell], [x, y])  # left of cell
        # 2 cazuri
        # 1 daca e straight
        # 2 daca e stang sau dreapta
        # direction: 1 up, 2 down, 3 right, 4 left
        if j == 0:
            position_of_start_point = 1
        elif j == self.numberOfRows - 1:
            position_of_start_point = 2
        elif i == 0:
            position_of_start_point = 4
        else:
            position_of_start_point = 3

        if direction == 1:
            if position_of_start_point == 2:
                self.add_straight_vert_cell(x, y)
            if position_of_start_point == 3:
                self.add_right_from_up_cell(x, y)
            if position_of_start_point == 4:
                self.add_left_from_up_cell(x, y)
        elif direction == 2:
            if position_of_start_point == 1:
                self.add_straight_vert_cell(x, y)
            elif position_of_start_point == 3:
                self.add_right_from_down_cell(x, y)
            elif position_of_start_point == 4:
                self.add_left_from_down_cell(x, y)
        elif direction == 3:
            if position_of_start_point == 1:
                self.add_right_from_up_cell(x, y)
            elif position_of_start_point == 2:
                self.add_right_from_down_cell(x, y)
            elif position_of_start_point == 4:
                self.add_straight_horiz_cell(x, y)
        elif direction == 4:
            if position_of_start_point == 1:
                self.add_left_from_up_cell(x, y)
            elif position_of_start_point == 2:
                self.add_left_from_down_cell(x, y)
            elif position_of_start_point == 3:
                self.add_straight_horiz_cell(x, y)

        y = list(self.road[-1])
        y[3] = direction
        self.road[-1] = tuple(y)
        self.grid[i][j].startPoint = 1

    # def pick_start_stop(self):
    #    pick=0
    #    x, y = self.change_coord_intoxy(0, 0)
    #    self.add_straight_horiz_cell(x,y)
    #    while True:
    #        ev = pygame.event.get()
    #        for event in ev:
    #            if event.type == pygame.MOUSEBUTTONDOWN:
    #                pos = pygame.mouse.get_pos()
    #                [i, j] = self.change_coord_pick(self.myround(pos[0]), self.myround(pos[1]))
    #                direction = input("dir")
    #                self.add_element(i,j,int(direction))
    #                #self.add_single_cell(self.myround(pos[0]), self.myround(pos[1]))
    #                list_as_array = np.array(self.grid)
    #                print(list_as_array)
    #                if pick==0:
    #                    self.start=(i,j)
    #                elif pick==1:
    #                    self.stop=(i,j)
    #                elif pick==10:
    #                    return
    #                pick += 1

    def set_start_point(self, i, j):
        # direction: 1 up, 2 down, 3 right, 4 left
        self.road.append((i, j, 0, 0))

    # Last element

    def set_stop_point(self, i, j):
        # direction: 1 up, 2 down, 3 right, 4 left
        x, y = self.change_coord_intoxy(i, j)
        newPoint = Point(i, j, 0)
        newPoint.endPoint = 1
        self.grid[i][j] = newPoint
        x, y = self.change_coord_intoxy(i, j)
        pygame.draw.line(self.screen, YELLOW, [x, y], [x + self.widthOfCell, y], )  # top of cell
        pygame.draw.line(self.screen, YELLOW, [x + self.widthOfCell, y],
                         [x + self.widthOfCell, y + self.widthOfCell])  # right of cell
        pygame.draw.line(self.screen, YELLOW, [x + self.widthOfCell, y + self.widthOfCell],
                         [x, y + self.widthOfCell])  # bottom of cell
        pygame.draw.line(self.screen, YELLOW, [x, y + self.widthOfCell], [x, y])  # left of cell

    def get_position(self, i, j):
        # direction: 1 up, 2 down, 3 right, 4 left
        last_element = self.road[-1]
        if last_element[0] < i:
            return 4
        elif last_element[0] > i:
            return 3
        elif last_element[1] < j:
            return 1
        elif last_element[1] > j:
            return 2

    def check_final_point(self, i, j):
        if self.grid[i][j] != None:
            if self.grid[i][j].endPoint == 1:
                return True
        return False

    def draw_last_element(self, iLast, jLast):
        i = self.road[-1][0]
        j = self.road[-1][1]
        direction = self.road[-1][3]
        x, y = self.change_coord_intoxy(iLast, jLast)

        # direction: 1 up, 2 down, 3 right, 4 left
        if jLast == 0:
            position_of_end_point = 1
        elif jLast == self.numberOfRows - 1:
            position_of_end_point = 2
        elif iLast == 0:
            position_of_end_point = 4
        else:
            position_of_end_point = 3

        if direction == 1:
            if position_of_end_point == 1:
                self.add_straight_vert_cell(x, y)
            if position_of_end_point == 3:
                self.add_right_from_down_cell(x, y)
            if position_of_end_point == 4:
                self.add_left_from_down_cell(x, y)
        elif direction == 2:
            if position_of_end_point == 2:
                self.add_straight_vert_cell(x, y)
            elif position_of_end_point == 3:
                self.add_right_from_up_cell(x, y)
            elif position_of_end_point == 4:
                self.add_left_from_up_cell(x, y)
        elif direction == 3:
            if position_of_end_point == 1:
                self.add_left_from_up_cell(x, y)
            elif position_of_end_point == 2:
                self.add_left_from_down_cell(x, y)
            elif position_of_end_point == 3:
                self.add_straight_horiz_cell(x, y)
        elif direction == 4:
            if position_of_end_point == 1:
                self.add_right_from_up_cell(x, y)
            elif position_of_end_point == 2:
                self.add_right_from_down_cell(x, y)
            elif position_of_end_point == 4:
                self.add_straight_horiz_cell(x, y)

    # Add new cell

    def add_new_cell(self, direction):
        time.sleep(self.sleep)
        # check if we are at the first cell
        if self.road[-1][3] == 0 and self.road[-1][2] == 0:
            self.draw_fist_element(self.road[-1][0], self.road[-1][1], direction)
            return False

        i, j = self.get_coordonate_of_actual_cell()
        self.add_element(i, j, direction)

        # check if we are at the last cell
        i, j = self.get_coordonate_of_actual_cell()
        if self.check_final_point(i, j):
            # am ajuns la ultimul element
            self.draw_last_element(i, j)
            print("Ati ajuns la punctul final")
            return True
        return False

    def get_coordonate_of_actual_cell(self):
        i = self.road[-1][0]
        j = self.road[-1][1]
        direction = self.road[-1][3]
        if direction == 1:
            j -= 1
        if direction == 2:
            j += 1
        if direction == 3:
            i += 1
        if direction == 4:
            i -= 1
        return i, j

    def add_element(self, i, j, direction):
        # dict:  straightVert=1 RfromBottom=2 LfromBottom=3  RfromUp=4 LfromUp=5 straightHoriz=6
        x, y = self.change_coord_intoxy(i, j)
        # 2 cazuri
        # 1 daca e straight
        # 2 daca e stang sau dreapta
        # direction: 1 up, 2 down, 3 right, 4 left
        position_of_last_element = self.get_position(i, j)
        if direction == 1:
            if position_of_last_element == 2:
                self.add_straight_vert_cell(x, y)
            elif position_of_last_element == 3:
                self.add_right_from_up_cell(x, y)
            elif position_of_last_element == 4:
                self.add_left_from_up_cell(x, y)
        elif direction == 2:
            if position_of_last_element == 1:
                self.add_straight_vert_cell(x, y)
            elif position_of_last_element == 3:
                self.add_right_from_down_cell(x, y)
            elif position_of_last_element == 4:
                self.add_left_from_down_cell(x, y)
        elif direction == 3:
            if position_of_last_element == 1:
                self.add_right_from_up_cell(x, y)
            elif position_of_last_element == 2:
                self.add_right_from_down_cell(x, y)
            elif position_of_last_element == 4:
                self.add_straight_horiz_cell(x, y)
        elif direction == 4:
            if position_of_last_element == 1:
                self.add_left_from_up_cell(x, y)
            elif position_of_last_element == 2:
                self.add_left_from_down_cell(x, y)
            elif position_of_last_element == 3:
                self.add_straight_horiz_cell(x, y)
        y = list(self.road[-1])
        y[3] = direction
        self.road[-1] = tuple(y)

        # continua in jos

        # self.add_single_cell(x,y)
        return len(self.road)

    # Remove element

    def remove_last_element(self):
        time.sleep(self.sleep)
        self.remove_elements(len(self.road) - 1)

    def remove_elements(self, i):
        if len(self.road) >= i:
            n = len(self.road) - i
            remain_elements = self.road[:len(self.road) - n]
            remove_elements = self.road[len(self.road) - n:len(self.road)]
            for element in reversed(remove_elements):
                self.remove_single_cell(element)
            self.road = remain_elements

    def remove_single_cell(self, element):
        x, y = self.change_coord_intoxy(element[0], element[1])
        pygame.draw.rect(self.screen, BLACK, (x, y, self.widthOfCell, self.widthOfCell), 0)  # draw a single width cell
        pygame.display.update()
        time.sleep(self.sleep)
        self.grid[element[0]][element[1]] = None

    # Auxiliare

    def myround(self, x):
        return x - (x % self.widthOfCell)

    def change_coord_intoxy(self, i, j):
        return (int((i + 1) * self.widthOfCell), int((j + 1) * self.widthOfCell))

    def change_coord(self, x, y):
        return (int(y / self.widthOfCell) - 1, int(x / self.widthOfCell) - 1)

    def change_coord_pick(self, x, y):
        return (int(x / self.widthOfCell) - 1, int(y / self.widthOfCell) - 1)

    # def carve_out_maze(self):
    #    pygame.display.update()
    #    self.pick_start_stop()
    #    print(self.start)
    #    print(self.stop)
    #    list_as_array = np.array(self.grid)
    #
    #    print(list_as_array)


#
# print(list_as_array)
# self.add_element(3,3)
# self.remove_elements(2)
## ##### pygame loop #######
# running = True
# while running:
#    # keep running at the at the right speed
#    self.clock.tick(30)
#    # process input (events)
#    for event in pygame.event.get():
#        # check for closing the window
#        if event.type == pygame.QUIT:
#            running = False

