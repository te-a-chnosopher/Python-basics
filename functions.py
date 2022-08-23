


#count = 1
#print(count)
#count = count+1
#count += 1
#print (count)
#count *= 2
#print (count)
#count /= 2
#print (count)

def addOne (number):
    number = number + 1
    return number
var= 1
print(var)
var2 = addOne(var)
print(var2)
var3 = addOne(var2)
print(var3)
var4 = addOne(2.3+7.2)
print(var4)

def addTwo (number1, number2):
    output = number1 + 2
    output += number2 + 3
    return output

sum = addTwo(var2,var4)
print(sum)

