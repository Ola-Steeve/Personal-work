list_a =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,15,1,2,3,4,6,78,34,13,3,6,8,34]
for x in list_a:
    if x <10:
        print(x)

########################################

less_num=[]
for num in list_a:
    if num < 10 :
        less_num.append(num)
print(less_num)