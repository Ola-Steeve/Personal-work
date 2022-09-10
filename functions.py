from msilib import add_stream


def add_subtractnumbers(number1, number2,*args,**kwargs):
    print(args)
    print(kwargs)
    return number1+number2, number1-number2, number1*number2

def print_if_odd(number):
    if number % 2 == 0:
        return
    print(number)



count = 0
while True:
    count +=1
    print_if_odd(count)

    if count >=20:
        break
print('end of loop')







start_number = 1
add_number=4

###########################
# Function parameter

mult=add_subtractnumbers(start_number,add_number,1,3,5,3,23,232,test1=123,qwert=12)
# print(mult)