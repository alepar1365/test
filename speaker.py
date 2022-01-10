seda = 'golabi'
shomare_harf = 0
for horoof in seda:
    x = seda.find(horoof)
    eco = ''
    for i in range(seda[:x]):
        eco += i
    # edame seda:
    # print(???? + seda[horoof:])
print(eco)