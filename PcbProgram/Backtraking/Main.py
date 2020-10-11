

from Backtraking.ReadFile import ReadFile

a=ReadFile("F:\\Projects\\PCB\\working\\PcbProgram\\Backtraking\\random.txt")




def function(x):
    if x is 0:
        return 1
    return x*function(x-1)