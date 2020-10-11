import sys
from threading import Thread
from pygame.locals import *
from MatrixBuild import PcbGraphical
import time
import pygame
import random

list_of_moves=list()
def input_values():
    global list_of_moves
    while True:
        num1 = random.randint(0, 3)
        list_of_moves.append(num1)
        time.sleep(4)

def main():
    global list_of_moves
    #Pcb = PcbGraphical(numberOfColumns=int(sys.argv[1:][0]), widthOfCell=15, drawMatrix=0, sleepTime=0.1)
    #Pcb.set_start_point(i=int(sys.argv[1:][1]), j=int(sys.argv[1:][2]))
    #Pcb.set_stop_point(i=int(sys.argv[1:][3]), j=int(sys.argv[1:][4]))

    Pcb = PcbGraphical(numberOfColumns=int(8), widthOfCell=15, drawMatrix=0, sleepTime=0.1)
    Pcb.set_start_point(i=int(0), j=int(0))
    Pcb.set_stop_point(i=int(0), j=int(1))
    thread = Thread(target=input_values, args=())
    thread.start()
    #thread.join()

    clock = pygame.time.Clock()
    FPS = 60  # silky smooth 60 frames per second
    done = False


    while not done:
        if len(list_of_moves)>0:
            move=list_of_moves.pop()
            Pcb.add_new_cell(direction=move)
        else:
            print("not")
        # your important mainloop stuff in here
        #for event in pygame.event.get():
        #    print("a")
        #    if event.type == pygame.KEYDOWN:
        #        if event.key == K_UP:
        #            print("w is pressed")
        #            Pcb.add_new_cell(direction=1)
        #        elif event.key == K_LEFT:
        #            print("s is pressed")
        #            Pcb.add_new_cell(direction=4)
        #        elif event.key == K_DOWN:
        #            print("a is pressed")
        #            Pcb.add_new_cell(direction=2)
        #        elif event.key == K_RIGHT:
        #            print("d is pressed")
        #            Pcb.add_new_cell(direction=3)
        #        elif event.key == K_BACKSPACE:
        #            print("back is pressed")
        #            Pcb.remove_last_element()
        #if pressed[pygame.K_w]:
#
        #if pressed[pygame.K_s]:
#
        #if pressed[pygame.K_a]:
        #    print("a is pressed")
        #    Pcb.add_new_cell(direction=4)
        #if pressed[pygame.K_d]:
        #    print("d is pressed")
        #    Pcb.add_new_cell(direction=3)
        #if pressed[pygame.K_x]:
        #    print("x is pressed")
        #    Pcb.remove_last_element()
        clock.tick(FPS)  # keep the speed in check
        #print(len(list_of_moves))
        #if len(list_of_moves)>0:
        #    Pcb.add_new_cell(direction=int(list_of_moves.pop()))
        #time.sleep(0.5)
        #print("ok")

    #Pcb.add_new_cell(direction=2)
    #print(Pcb.get_coordonate_of_actual_cell())
    #Pcb.add_new_cell(direction=2)
    #Pcb.add_new_cell(direction=2)
    #Pcb.add_new_cell(direction=2)
    #Pcb.remove_last_element()


if __name__ == "__main__":
    main()

