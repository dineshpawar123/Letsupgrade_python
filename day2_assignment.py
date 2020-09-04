# Day2Assignment




#---------------------------List Implementation

lst =[1,2,3,4,"pune","mumbai","nashik"]

print(lst)

lst.append("kolhapur") #Append
print(lst)

lst.pop(4)
print(lst)

lst.reverse()
print(lst)


lst.insert(1,"0")
print(lst)

lst.count(1)
print(lst)

#-----------------------------------Dictionary implementation

my_dict ={"a":"1","b":"2","c":"3","d":"4"}

my_dict2 ={}
print(my_dict)

my_dict.pop("d")
print(my_dict)

my_dict.get("a")
print(my_dict)


print(my_dict.values())

print(my_dict.items())

my_dict.clear()
print(my_dict)

#-----------------------------------set implementation

st={1,2,3,4,5,6,7,8}

a=st.add(9)
print(a)


st.update(["orange", "mango", "grapes"])
print(st)

b=len(st)
print(b)

st.remove(1)
print(st)

st.discard("orange")
print(st)

#-----------------------------------tuple implementation

thistuple = ("1", "3", "4")
print(thistuple)


thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)
print(x)

x = thistuple.index(8)
print(x)

#-----------------------------------string implementation

a = "Hello, dinesh!"
print(len(a))

a = "Hello, dinesh!"
print(a.lower())

a = "Hello, dinesh!"
print(a.upper())


a = "Hello, dinesh!"
print(a.replace("H", "J"))

a = "Hello, dinesh!"
print(a.split(","))





