import string

class ReadFile:
    movementsList=list()
    originalmovement=list()
    def __init__(self,file_path):
        self.f = open(file_path, "r")
        file_content=self.f.read()
        file_content=file_content.translate(str.maketrans('', '', string.whitespace))
        for i in range(0,len(file_content),2):
            self.movementsList.append(file_content[i]+file_content[i+1])
        self.movementsList.reverse()
        self.originalmovement=self.movementsList.copy()
    def get_next_move(self):
        print(len(self.movementsList))
        if len(self.movementsList)>0:
            return self.movementsList.pop()
        else:
            self.movementsList=self.originalmovement.copy()
            return self.movementsList.pop()




