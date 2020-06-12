# -*- coding: utf-8 -*-

#Those are some examples shown on the Platzi Master Session (11/06/2020)
#Use of sets. That session was conducted by Facundo García Martoni @facmartoni

my_set = {3,4,5}                    #What is a set? A disordered collection of unique and immutable elements.
print("my_set =", my_set)

my_set2 = {"Hola",23.3,False, True}
print("my_set2 =", my_set2)

my_set3 = {3,3,2}
print("my_set3 =", my_set3)

empty_set = {}
print(type(empty_set))

empty_set = set()
print(type(empty_set))

my_list = [1,1,2,3,4,4,5]
my_set = set (my_list)
print(my_set)

#How to add a new element to a set? 

my_set = {3,4,5,10,-4}
print("my_set before add a new element=", my_set)

my_set.add(6)
print("my_set after add a new element=", my_set)

my_set.update([1,2,3,4,5,6,7])
print("my_set after add a new element=", my_set)

#How to remove a new element to a set? 

my_set = {7,-8,4,'Hola_amigo','aleph'}
print("my_set before remove an element=", my_set)

my_set.remove('Hola_amigo')
print("my_set after remove a concrete element=", my_set)

my_set = {4,7,-8,5,'Hola_amigo','aleph'}
print("my_set before remove an element=", my_set)

my_set.discard(7)
print("my_set after remove a concrete element=", my_set)

#How to clear a set? 

my_set = {4,7,2,'curnocopia',-8,'Hola_amigo','aleph'}
print("my_set before be cleared=", my_set)

my_set.clear()
print("my_set after be cleared=", my_set)

#How to remove a random element to a set? 

my_set = {4.52,7.3,2,'curnocopia',-8,4,'Hola_amigo','aleph'}
print("my_set before=", my_set)

my_set.pop()
print("my_set after=", my_set)

#Set_1 union Set_2

my_set_1 = {4.52,7.3,2,'curnocopia',-8,4,'Hola_amigo','aleph'}
my_set_2 = {4.52,7.3,2,'curnocopia',-8,4,'Hola_amigo','aleph','new element',-5,7.31,'patato'}
my_set_3 = my_set_1 | my_set_2

print("Set_1 union Set_2 =", my_set_3)

#Set_1 intersection Set_2

my_set_1 = {4.52,7.3,2,'bjork',-8,4,'aleph'}
my_set_2 = {4.52,7.3,2,'curnocopia',-8,4,'Hola_amigo','aleph','new element',-5,7.31,'patato'}
my_set_3 = my_set_1 & my_set_2

print("Set_1 intersection Set_2 =", my_set_3)

#Set_1 relative Set_2

my_set_1 = {4.52,7.3,2,'bjork',-8,4,'aleph'}
my_set_2 = {4.52,7.3,2,'curnocopia',-8,4,'Hola_amigo','aleph','new element',-5,7.31,'patato'}
my_set_3_1 = my_set_1 - my_set_2
my_set_3_2 = my_set_2 - my_set_1

print("Set_1 - Set_2 =", my_set_3_1)
print("Set_2 - Set_1 =", my_set_3_2)

#Set_1 Symmetric difference Set_2

my_set_1 = {4.52,7.3,2,'bjork',-8,4,'aleph'}
my_set_2 = {4.52,7.3,2,'curnocopia',-8,4,'Hola_amigo','aleph','new element',-5,7.31,'patato'}
my_set_3 = my_set_1 ^ my_set_2

print("Set_1 Symmetric difference Set_2 =", my_set_3)
