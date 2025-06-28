size = int(input("Enter the size of the pattern: "))

x = 0
while size > x:
    for i in range(size):
        print('*', end = '')
    print()
    x+=1

