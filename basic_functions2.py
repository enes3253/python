for i in range(5, 0, -1):
    print(i)

def print_and_return(arr):
    return arr[1]

print(print_and_return([2,5]))

def first_plus_length(arr):
    return arr[0] + len(arr)
print(first_plus_length([1,2,3,4,5]))

def values_greater_than_second(list):
    if len(list)<2:
        return False
    newList = []
    for val in list:
        if val>list[1]:
            newList.append(val)
    print(len(newList))    
    return newList
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

def length_and_value(size,value):
    newArr = []
    for i in range(size):
        newArr.append(value)
    return newArr

print(length_and_value(2,4))