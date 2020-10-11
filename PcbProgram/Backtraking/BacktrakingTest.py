import time
from threading import Thread

import pygame

from Backtraking.ReadFile import ReadFile
from Backtraking.Matrice import Matrice
from MatrixBuild import PcbGraphical

list_of_moves=list()



def add_move(directie):
    global list_of_moves
    if directie == "sus":
        list_of_moves.append(1)
    elif directie == "jos":
        list_of_moves.append(2)
    elif directie == "dreapta":
        list_of_moves.append(3)
    elif directie == "stanga":
        list_of_moves.append(4)
    else:
        list_of_moves.append(9)


#print(m.get_number_of_free_options())

#m.add_point("dreapta")
#print(m.get_number_of_free_options())

def get_next_move():
    value = file.get_next_move()
    if value == "00":
        directie = "sus"
    elif value == "01":
        directie = "dreapta"
    elif value == "10":
        directie = "jos"
    else:
        directie = "stanga"
    return directie

def work():
    while(True):#de motificat- cand ajung in pct de final sau am aprcurs lista de prea m,ulte ori
        global list_of_moves
        number_of_free_pass=m.get_number_of_free_options()
        #print("numarul de miscari libere "+str(number_of_free_pass))
        if number_of_free_pass==0:
            #print("nu am miscari libere, merg inapoi")
            m.remove_last_point()
            add_move("sterge")
        elif number_of_free_pass==1:
            #print("am o singura miscare libera--------!!!")
            aaa=m.get_free_option()
            print(aaa)
            m.add_point(aaa)
            add_move(aaa)
        else:
            #print("aleg random")
            directie=get_next_move()
            print(directie)
            val=m.add_point(directie)
            if val==False:
                print("directie gresita")
            else:
                add_move(directie)
        m.print_matrix()
        if(m.check_if_full()):
            if m.points[-1].index==-1:
                m.print_matrix()
                time.sleep(100)
        time.sleep(2)


file=ReadFile("F:\\Projects\\PCB\\working\\PcbProgram\\Backtraking\\random.txt")

m = Matrice(5,5)
m.add_first(0, 0)
m.add_last(1,0)
m.print_matrix()
Pcb = PcbGraphical(numberOfColumns=int(5), widthOfCell=15, drawMatrix=0, sleepTime=0.1)
Pcb.set_start_point(i=int(0), j=int(0))
Pcb.set_stop_point(i=int(0), j=int(1))
thread = Thread(target=work, args=())
thread.start()
#thread.join()
clock = pygame.time.Clock()
FPS = 60  # silky smooth 60 frames per second
done = False
Pcb.add_new_cell(direction=3)
while not done:
    if len(list_of_moves)>0:
        move=list_of_moves.pop(0)
        if move==9:
            Pcb.remove_last_element()
        else:
            print("---miscare facuta pe harta "+str(move))
            Pcb.add_new_cell(direction=move)
    else:
        time.sleep(0.3)
        #print("not")
