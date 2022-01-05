matn = 'abcde'
matn = matn.lower()

matn2 = ''
for i in matn:
    
    if i == 'b':
        continue
    elif i == 'd':
        continue
    else:
        matn2 = matn2 + '.'
        matn2 = matn2 + i
        
print(matn2)        
