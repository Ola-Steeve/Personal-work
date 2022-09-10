def print_if_odd(number):
    if number % 2 == 0:
        return
    print(number)


count =0
while True:
    count +=1
    print_if_odd(count)

    if count>=20:
        break
print('ended loop')

#####################################
