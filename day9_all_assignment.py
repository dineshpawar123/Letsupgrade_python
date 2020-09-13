lst = list(range(1000))

print(lst)

def getCloseByEvenNumberGen(lst):
    for item in lst:


            length = int(len(str(item)))
            # print(length)
            sum = 0

            temp = item

            while temp > 0:
                dig = int(temp % 10)
                # print("dig ==", dig)
                sum = sum + (dig ** length)
                # print("sum ==",sum)
                temp = temp / 10

            if item == sum:
                yield item

print(list(getCloseByEvenNumberGen(lst)))



