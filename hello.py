x = input('Say HELLO: ')
hello = ''
for i in x:
    if i == 'h':
        hello += i
    if i == 'e':
        hello += i
    if i == 'l':
        hello += i
    if i == 'o':
        hello += i  
#print(hello)
count_l = 0
for i in hello:
    if i == 'l':
        count_l += 1

#print(count_l)
#hello_2 = ''

if count_l >= 2:
    hello_correct = 'hello'
    ghalat = 0
    for i in hello_correct:
        y = hello.find(i)
        if y == -1:
            print('NO')
            break
        else:
            ghalat += 1
    if ghalat == 5:
        print('YES')        
else:
    print('NO')
