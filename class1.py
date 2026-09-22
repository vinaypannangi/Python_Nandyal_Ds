class Narendra:
    def __init__(self):
        print("Hello Narendra")

    def c2(self):
        print("Ella unnaru")   

class Rahul(Narendra):
    def c3(self):
        print("Tinnara")
    
    def c4(self):
        print("Em chestunnaru")

a=Narendra()
a.c2()
print()
b=Rahul()
b.c2()
print()
b.c3()
print()
b.c4()

