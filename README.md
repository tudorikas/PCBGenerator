# Pcb

Utilizare:
Un exemplu de utilizare se gaseste in fisierul **Main.py**

La inceputul rularii programului clasa **PcbGraphical** trebuie initializata cu urmatorii parametri:

Momentan, programul permite initializarea doar de matrice patratica.

**numberOfColumns** - int - Numarul de linii si de coloane din matrice 
**widthOfCell** - int - grosimea liniilor ce urmeaza sa fie desenate
**drawMatrix** - int - pentru valoarea 1 va desena liniile matricei
**sleepTime** - float - timpul de asteptare inainte de a adauga urmatoarea mutare

Apoi se vor apela urmatoarele 2 functii care au ca rol setarea punctului de inceput si de sfarsit

**set_start_point(i=0,j=0)**  - Va fi marcat cu ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) rosu pe desen

**set_stop_point(i=4,j=0)**  - Va fi marcat cu ![#FFF000](https://via.placeholder.com/15/FFF000/000000?text=+) galben pe desen

Functii ce pot fi apelate:

Pentru adaugarea unei noi mutari se apeleaza functia:

**add_new_cell(direction=1/2/3/4)**

Pentru stergerea ultimei celule:

**remove_last_element()**

Pentru aflarea pozitiei actuale in care urmeaza sa se ia o decizie:

**i,j=get_coordonate_of_actual_cell()**

Gridul construit poate fi accesat:

**Pcb.Grid[i][j]**

Iar acesta contine urmatoarele campuri:

class Point:
    **i=None
    j=None
    decisionPoint=None
    direction=None
    startPoint=0
    endPoint=0**

![alt text](https://github.com/tudorikas/Pcb/blob/master/diagram.png?raw=true)


    
    
