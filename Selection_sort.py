# Selection Sort

'''
Selection Sort is very neat & common sorting Algorithm
Algoritm Scan all element from given Array and find the smallest one
Similary It scan remaining array and find another smaller one and so on....

Big(0) : 0(n2) ==> Log(n) > for scanning who list
Number of time scanning list is n 
so log(n)*n > log(n2) == > Big(0) is 0(n2)
'''

'''
Pseudo Code

for item in array:
Step1    find_smallest in list 
Step2    pop the element form array
Step3    add the element in new array
Step4    repeated step 1 to step 3

'''

def find_smallest(arr):
    '''
    Find the smallest number in given array
    :param : input the array
    :return : index of smallest number
    '''
    smallest_number, idx = arr[0],0
    for i in range(0,len(arr)):
        if arr[i] < smallest_number:
            smallest_number = arr[i]
            idx = i
    
    return idx


def selection_sort(arr):
    '''
    Python implementation of selection Sort
    :input arr : input the array
    :return : Sorted array
    '''

    new_arr = []

    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    
    return new_arr


print(selection_sort([5, 3, 6, 2, 10,-1]))




