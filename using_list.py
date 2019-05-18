shoplist=['apple','mango','banana','carrot']
print('I have',len(shoplist),'items to purchase')
print('These items are:')
for i in shoplist:
    print(i)

print('\nI also have to buy rice.')
shoplist.append('rice')
print('List now',shoplist)

shoplist.sort()
print('Sorted shopping list is',shoplist)

print('The first item is',shoplist[0])

olditem=shoplist[0]

del shoplist[0]
print('shoplist now',shoplist)

list1=['aa']
print(list1,len(list1))

zoo=('a',)
print(zoo)
