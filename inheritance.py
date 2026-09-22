#1. Single Inheritance
class Parent:
    def show(self):
        print("This is Parent class")
class Child(Parent):
    def display(self):
        print("This is Child class")
obj = Child()
obj.show()
obj.display()

#2. Inheritance with Constructor
class Person:
    def __init__(self, name):
        self.name = name
class Student(Person):
    def display(self):
        print("Name:", self.name)
s = Student("Rahul")
s.display()

#3. Multilevel Inheritance
class Grandfather:
    def show1(self):
        print("Grandfather")
class Father(Grandfather):
    def show2(self):
        print("Father")
class Son(Father):
    def show3(self):
        print("Son")
obj = Son()
obj.show1()
obj.show2()
obj.show3()

#4. Multiple Inheritance
class Father:
    def father(self):
        print("Father class")
class Mother:
    def mother(self):
        print("Mother class")
class Child(Father, Mother):
    def child(self):
        print("Child class")
obj = Child()
obj.father()
obj.mother()
obj.child()

#5. Hierarchical Inheritance
class Parent:
    def show(self):
        print("Parent class")
class Child1(Parent):
    def display1(self):
        print("Child 1")
class Child2(Parent):
    def display2(self):
        print("Child 2")
a = Child1()
b = Child2()
a.show()
a.display1()
b.show()
b.display2()

#6. Method Overriding
class Parent:
    def show(self):
        print("Parent method")
class Child(Parent):
    def show(self):
        print("Child method")
obj = Child()
obj.show()

#7. Using super()
class Parent:
    def show(self):
        print("Parent method")
class Child(Parent):
    def show(self):
        super().show()
        print("Child method")
obj = Child()
obj.show()

#8. Employee Inheritance
class Employee:
    def work(self):
        print("Employee is working")
class Manager(Employee):
    def manage(self):
        print("Manager is managing")
m = Manager()
m.work()
m.manage()

#9. Vehicle Inheritance
class Vehicle:
    def start(self):
        print("Vehicle starts")
class Car(Vehicle):
    def drive(self):
        print("Car is driving")
c = Car()
c.start()
c.drive()

#10. Animal Inheritance
class Animal:
    def eat(self):
        print("Animal eats food")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
d = Dog()
d.eat()
d.bark()