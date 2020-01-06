# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

list1 = [1,2,3,4,'a']
list1.append(5) # přidání hodnoty do listu

list_of_lists = [list1,[5,6,7]]
print(list_of_lists)
print(list_of_lists[0][0]) # vyhodí 1. hodnotu v 1. listu

for item in list1: # není žádný end, co je odsazené je v cyklu; odsazení označených řádků: tab; zrušení odsazení: Shift+tab
    print(item)
    
for k in range(3,5): # range(5) je jenom u for cyklu, vyhodí hodnoty 0-4; range(3,5) - první číslo tam je, druhé už ne
    print(k)
    
a=5
if a==1:
    print('1')
elif a!=3 and a<5:
    print('2')
else:
    print('3')
    
    

def plus(a,b=2): # funkce
    c = a + b
    return c

print(plus(1,b=1)) # volání funkce
print(plus(1))
a,b = plus(1,1)

list1=[1,2,3]
list2=list1
list2[2]=99 # přepíše v listu 1 i v listu 2 -> je to jen ukazatel na pamět a ne uložení do listu
list2=list1.copy() # takto se nepřepíše list 1 pokud něco přepíšu v listu 2


a='fvgdfgd' 

# vytvoření funkce - bud napsat do stejného skriptu, nebo do jiného, ale musí se skript importovat (import skript.funkce)