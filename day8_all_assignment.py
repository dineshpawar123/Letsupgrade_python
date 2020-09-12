

#----------------------------------------------question 1-----------------
def hello_decorator(func):

    def inner1():
        print("Hello, this is before function execution")
        t = input("Enter value of range ")


        x, y = 0, 1

        while y < int(t):
            print(y)
            x, y = y, x + y

        func()

        print("This is after function execution")

    return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
     print("This is inside the function !!")

function_to_be_used = hello_decorator(function_to_be_used)

function_to_be_used()


#-----------------------------q2--------------



f = open("a.txt","r")
try:
    for i in range(10):
        f.write("This is line %d\r\n" % (i+1))
except Exception as e:
        print("Oops!", e.__class__, "occurred.")
