x = '1+1+3+1+3+2'

xx=''
for i in x:
    if i == '1':
        xx += i
        xx += '+'
for i in x:    
    if i == '2':
        xx += i
        xx += '+'
for i in x:    
    if i == '3':
        xx += i
        xx += '+'
                
print(xx[0:-1])    