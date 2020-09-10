#------------assignment1-----------------
print("---------------Assignment1-------------------");
lst =[2,7,8]
lst1=[7,3,2,9,8,7,1,5,9,8]

print(lst)
length = int(len(lst))
print("length :",length)

print(lst1)
length1 = int(len(lst1))
print("length :",length1)

i=0
cnt=0

for j in range(0,(len(lst1))):
    if lst[i]==lst1[j] :
        cnt=cnt+1
        i = i+1
        if i==3:
            break

if cnt==length:
    print("its a match")
else:
    print("its gone")




#---------------Assignment2-------------------------
print("---------------Assignment2-------------------")

ages = range(2, 2500)

def myFunc(x):
    for i in range(1, x):
        if ((x % 2) == 0):
            return False
    return x;

adults = filter(myFunc, ages)

for x in adults:
    print(x)



#---------------Assignment3-------------------------
print("---------------Assignment3-------------------")



new_list = [];
message = ["hey this is sai","i am in mumbai"]
for i in range(len(message)):
    new_list.append([
        word.capitalize()

            for word in message[i].split(" ")
                    ])

print(new_list);
