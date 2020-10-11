class Point:
    def __init__(self,x,y):
        self.sus=None
        self.jos=None
        self.dreapta=None
        self.stanga=None
        self.x=x
        self.y=y
        self.index=0

    def add_point(self,newPoint,direction):
        if direction=="sus":
            self.sus=newPoint
        elif direction=="jos":
            self.jos=newPoint
        elif direction=="dreapta":
            self.dreapta=newPoint
        else:
            self.stanga=newPoint

    def remove_point(self):
        if self.sus!=None:
            self.sus=0
        elif self.stanga!=None:
            self.stanga=0
        elif self.dreapta!=None:
            self.dreapta=0
        elif self.jos!=None:
            self.jos=0
        else:
            return False

    def get_numer_of_free_options(self):
        counter=0
        if self.sus==None:
            counter+=1
        if self.dreapta==None:
            counter+=1
        if self.stanga==None:
            counter+=1
        if self.jos==None:
            counter+=1
        return counter

    def get_free_option(self):
        if self.sus==None:
            return "sus"
        elif self.dreapta==None:
            return "dreapta"
        elif self.stanga==None:
            return "stanga"
        else:
            return "jos"


class Matrice:
    def __init__(self,w,h):
        self.w, self.h = w,h
        self.index=0
        self.matrix = [[None for x in range(self.w)] for y in range(self.h)]
        self.points=list()

    def print_matrix(self):
        for i in self.matrix:
            for j in i:
                if j==None: print(str(0) + " ", end="")
                else:
                    print(str(j.index) + " ", end="")
            print("")


    def get_number_of_free_options(self):
        return self.points[-1].get_numer_of_free_options()

    def get_free_option(self):
        return self.points[-1].get_free_option()

    def add_point(self,directie):

        new=self.check_rulse_and_generate(directie)
        if new!=None:
            #pun indexul
            new.index=self.index

            # blochez calea catre punctul din care vine

            if directie == "sus":
                new.jos=self.points[-1]
            elif directie=="jos":
                new.sus=self.points[-1]
            elif directie=="dreapta":
                new.stanga=self.points[-1]
            else:
                new.dreapta=self.points[-1]

            #il adaug in matrice
            #verific daca gasesc punctul de final acolo
            if new.x==self.pctfinX and new.y==self.pctfinY:
                new.sus = 0
                new.jos = 0
                new.dreapta = 0
                new.stanga = 0
                new.index = -1
                self.matrix[new.x][new.y] = new
                print("am gasit pct final")
            else:
                self.matrix[new.x][new.y]=new

            #blochez calea punctului anterior
            self.points[-1].add_point(new, directie)

            #adaug punctul in lista
            self.points.append(new)
            self.index+=1
        else:
            if directie == "sus":
                self.points[-1].sus=0
            elif directie == "jos":
                self.points[-1].jos=0
            elif directie == "dreapta":
                self.points[-1].dreapta=0
            else:
                self.points[-1].stanga=0
            return False


    def remove_last_point(self):
        if len(self.points)>0:
            self.matrix[self.points[-1].x][self.points[-1].y] = None
            self.points.pop()
            self.points[-1].remove_point()
            self.index-=1
        else:

            return False


    def add_first(self,x,y):
        new=Point(x,y)
        self.matrix[new.x][new.y] = new
        new.index=self.index
        self.index+=1
        self.points.append(new)

    def add_last(self,x,y):
        self.pctfinX=x
        self.pctfinY=y
        #new.index = self.index
        #self.index += 1
        #self.points.append(new)

    def check_rulse_and_generate(self,directie):
        #legate de locatie-sa nu iasa din permiteru
        if directie == "sus":
            if (self.points[-1].x > 0):
                pass
            else:
                return None
        elif directie == "jos":
            if (self.points[-1].x < self.h-1):
                pass
            else:
                return None
        elif directie == "dreapta":
            if (self.points[-1].y < self.w-1):
                pass
            else:
                return None
        elif directie == "stanga":
            if (self.points[-1].y > 0):
                pass
            else:
                return None

        #legate de disponibilitatea punctului in care vreau sa ajung

        if directie == "sus":
            if (self.matrix[self.points[-1].x-1][self.points[-1].y]==None):
                pass
            else:
                return None
        elif directie == "jos":
            if (self.matrix[self.points[-1].x+1][self.points[-1].y]==None):
                pass
            else:
                return None
        elif directie == "dreapta":
            if (self.matrix[self.points[-1].x][self.points[-1].y+1]==None):
                pass
            else:
                return None
        elif directie == "stanga":
            if (self.matrix[self.points[-1].x][self.points[-1].y-1]==None):
                pass
            else:
                return None

        #legate de disponibilitatea directiei din punctul din care plec


        if directie=="sus":
            if(self.points[-1].sus==None):
                return Point(self.points[-1].x-1,self.points[-1].y)
            else:
                return None
        elif directie=="jos":
            if(self.points[-1].jos==None):
                return Point(self.points[-1].x+1,self.points[-1].y)
            else:
                return None
        elif directie=="dreapta":
            if(self.points[-1].dreapta==None):
                return Point(self.points[-1].x,self.points[-1].y+1)
            else:
                return None
        elif directie=="stanga":
            if(self.points[-1].stanga==None):
                return Point(self.points[-1].x,self.points[-1].y-1)
            else:
                return None
        else:
            return None

    def check_if_full(self):
        for i in self.matrix:
            for j in i:
                if j == None:
                    return False
        return True

if __name__ == "__main__":
    m=Matrice()
    m.add_first(0,0)
    m.add_point("dreapta")
    m.add_point("jos")
    m.remove_last_point()
    m.add_point("jos")
    m.add_point("jos")
    m.add_point("stanga")
    m.add_point("sus")
    m.add_point("dreapta")
    m.add_point("dreapta")

    m.print_matrix()