file1=open('testfile.txt','a')
file1.write('This is going to be our first file\n')
file1.write('This is line number 2\n')
file1.write('Another line')
file1.close()

with open('next.txt', 'r') as new:
    for line in new.readlines():
        print(line)