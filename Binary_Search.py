# Binary Search

'''
Binary search is an algorithm; its input is a sorted list of elements
If an element you’re looking for is in that list, binary search returns the position
where it’s located. Otherwise, binary search returns null. this Algorithm faster than
Simple or Stupid Search, Total number of Iteration take is log2(number of element in the list)

example : 128 element => 7 steps
          512 element => 8 steps
'''

def binary_search(input_list,item):
    '''
    implementation of binary search
    :param input_list: sorted input list elements
    :param item: element for search
    : return: index if element found else None
    '''

    low = 0 
    high = len(input_list) - 1 # low and high useful to track and help to understand that which part we are tracking


    while low <= high:
        mid = (low + high)//2


        if input_list[mid] == item:
            return mid
        
        elif input_list[mid] > item:
            high = mid -1
        
        else:
            low = mid  +1
    
    return None

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3)) # => 1
print(binary_search(my_list, -1)) # => None