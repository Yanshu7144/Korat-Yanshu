#Required

def addnum(a,b) :
    return a+b
ret=addnum(5,10)
print(ret)

#keyword

def student(name,age):
    print("student Details:",name,age)
student('Jay',21)
student(name='Yanshu',age=21)
student('Meet',age=22)
student(age=21,name='Jenish')

#Default

def printinfo(name,age=35):
    print("Name =",name)
    print("Age =",age)
    return
printinfo(age=50,name="Yanshu")

#Variable_Length

def my_function(*args):
    for a in args :
        print(a)
my_function(1,2,3)

def my_fun(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
my_fun(name="Yanshu",age=20)

#Global

global_var=10
def modify_global_var():
    global global_var
    global_var+=5
print(global_var)
modify_global_var()
print(global_var)

#Local

def sum(x,y):
    sum=x+y
    return sum
print(sum(2,10))

#Nonlocal

def outer():
    x1="Local"
    def inner():
        nonlocal x1
        x1="nonlocal"
        print("inner =",x1)
        inner()
        return x1
x = outer()
print(x)
