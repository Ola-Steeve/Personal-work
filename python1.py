from cgi import print_form
from multiprocessing.sharedctypes import Value
from xml.etree.ElementTree import Comment


interger_one=1
interger_two=2

string_one='1'
string_two='2'
print(interger_one+interger_two)
print(str(interger_one)+string_two)
var_that_is_none=None
print(var_that_is_none, type(var_that_is_none))
ola=['one','two','three']
print(ola)
ola.append('four')
print(ola[1])
print(len(ola))
our_first_dictionary ={'key':'value', 'key2': {'key2.1':'newkeyvalue'},'key3':'value3',2:3,5:'another value'}
print(our_first_dictionary, type(our_first_dictionary))
print(our_first_dictionary['key2'])


our_first_dictionary['Nigeria']='wasted'
print(our_first_dictionary)
our_first_dictionary['key']='one'
print(our_first_dictionary)

del our_first_dictionary['key3']
print(our_first_dictionary)

our_first_dictionary['key3']={'new key':'key3.1','new key2':'key3.2'}
print(our_first_dictionary)


####################
name='Ben'
age='133'
print(name, 'is',age)
print(f'name: {name} age: {age}')

if name == 'Ben' and age =='133':
    print('this is truly ben')



print('Ola is awesome')

for i in range(10):  #start=0,stop=10,step=1
    print(i)

my_list=['a','b','c','d','e']

for index in range(len(my_list)):
    value =my_list[index]
    print(index,value)



##############################

count =0
while count is True:
    print('i Like to move it')
    count+1