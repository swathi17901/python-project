'''                                                                                                     
box={"pen","pencil","scale","eraser","pen"}

print(box)

print('pencil' in box)
print('note' not  in box)

a=set('princy')
b=set('priya')

print(a)
print("letter in a but not in b",b-a,a-b)
print("both a or b",a|b)
print("letters in both a and b",a&b)
print("letter in a or b but not both",a^b)

a={x for x in 'education' if x in 'abcde'}
print(a)   

#set checking

   

'''
#dictionaries

dic={'name':'swathi','age':19}
print(dic['name'])

dist={x:x**2 for x in (4,6,8)}
print(dist)
'''
print(list(dic))
print(sorted(dic))
print('guido' in dic)
print('guide' in dic)

a=dict([('bala',54),('arun',34),('aruvi',21)])
print(a)



a=dict(a=17,b=45,c=32)
print(a)
'''
