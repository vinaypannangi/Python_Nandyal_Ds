# def greet():
#     print("hello sir")
# greet()

def vinay1(func):
    def wrapper():
        print("Function is starting")
        func()
        print("Function is completed")
    return wrapper
@vinay1
def vinay():
    print("hello")
vinay()


# def T1(func):
#     def t4():
#         print("nandyal is in ap")
#         func()
#         print("guntur is in ap")
#     return t4()

# def t1(func):

#     def t4():
#         print("nandyal is in ap")
#         func()
#         print("guntur is in ap")
#     return t4()

# @t1
# def manoj():
#     print("Manoj Ella unnaru")
# manoj()

































