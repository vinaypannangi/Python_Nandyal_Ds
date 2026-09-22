def student():
    name = "rahul"
    age = 20
    print(locals()["name"])
    print(locals()["age"])
student()