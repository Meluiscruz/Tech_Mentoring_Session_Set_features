# -*- coding: utf-8 -*-

#This is the final exercise of the Platzi Master Session (11/06/2020)
#Use of sets. That session was conducted by Facundo García Martoni @facmartoni

#This function removes the duplicated components from some_list by the use of for and if clauses.
def remove_duplicates_1(some_list):             
    without_duplicates = []
    for element in some_list:                       #Check each element from the list
        if element not in without_duplicates:       #If the element is not in without_duplicates list
            without_duplicates.append(element)      #The append() method appends an element to the end of the list.
    return without_duplicates                       #Return the list without duplicates

#This function removes the duplicated components from some_list by the use of a one-line for-if version.
def remove_duplicates_2(some_list):
    without_duplicates = []
    [without_duplicates.append(element) for element in some_list if element not in without_duplicates]
    return without_duplicates

#This function removes the duplicated components from some_list by the use of the set().
def remove_duplicates_3(some_list):
    return list(set(some_list))                     #Return the listed set.

def run():
    random_list = [1,2,3,3,3,"Platzi","Platzi", True, 4.6,"Pepe", False]    #This is a random list with duplicated elements. 

    print(remove_duplicates_1(random_list))
    print(remove_duplicates_2(random_list))
    print(remove_duplicates_3(random_list))

if __name__ == '__main__':
    run()