item_oldprice=dict()
item_newprice=dict()
num_items=raw_input('Enter the number of items: ')
for n in range(0,int(num_items)):
    input=raw_input('Enter item and old price: ')
    item_oldprice[input.split()[0]]=int(input.split()[1])
for n in range(0,int(num_items)):
    input=raw_input('Enter item and new price: ')
    item_newprice[input.split()[0]]=int(input.split()[1])
print ''
for item in item_oldprice.keys():
    if item_oldprice[item]!=item_newprice[item]:
        if item_oldprice[item]<item_newprice[item]:
            print item,'+'+str(item_newprice[item]-item_oldprice[item])
        else:
            print item,str(item_newprice[item]-item_oldprice[item])



