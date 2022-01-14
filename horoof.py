x = 'MEHdi'
x_koochik = x.lower()
bozorg = 0
koochik = 0

for i in x:
    y = x_koochik.find(i)
    # print(y)
    if y == -1:
        bozorg +=1
    else:
        koochik += 1
if bozorg > koochik:
    print(x.upper())        
else:    
    print(x_koochik)