from MatrixBuild import PcbGraphical

def main():
    Pcb = PcbGraphical(numberOfColumns=35, widthOfCell=15, drawMatrix=0, sleepTime=0.5)
    Pcb.set_start_point(i=0, j=0)
    Pcb.set_stop_point(i=4, j=0)
    Pcb.add_new_cell(direction=3)
    print(Pcb.get_coordonate_of_actual_cell())
    Pcb.add_new_cell(direction=2)
    Pcb.add_new_cell(direction=3)
    Pcb.add_new_cell(direction=3)
    Pcb.remove_last_element()
    Pcb.add_new_cell(direction=1)
    Pcb.add_new_cell(direction=3)
    Pcb.add_new_cell(direction=3)

if __name__ == "__main__":
    main()

