outside=5

def test_func(x):
    global outside
    outside=4
    global outside_2
    outside_2=90
    y=x+outside
    return y

print(test_func(1))
print(outside_2)