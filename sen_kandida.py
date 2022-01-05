big = 0
sen = 0

while True:
    sen = input('Sen ra vared konid: ')
    sen = int(sen)
    if sen != -1:
        if sen in range(10, 91):

            if sen > big:
                big = sen
        else:
            print('koochooloooooo')
    else:
        break        
print(big)        