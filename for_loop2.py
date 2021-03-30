def biggie_size(lst):
    for i in range(len(lst)):
        if lst[i] > 0:
            lst[i] = "big"
    return lst

print(biggie_size([-8,2,6,-5]))

def count_positives(lst):
    count = 0
    for val in lst:
        if val > 0:
            count += 1
    lst[len(lst) - 1] = count
    return lst

print(count_positives([-6,14,2,-15]))

def sum_total(lst):
    total = 0
    for val in lst:
        total += val
    return total

print(sum_total([15,-5,8,-6]))

def average(lst):
    total = 0
    for val in lst:
        total += val
    return float(total) / float(len(lst))

print(average([5,2]))    

def length(lst):
    count = 0
    for val in lst:
        count += 1
    return count

print(length([25,10,3,-8]))

def minimum(lst):
    if len(lst) == 0:
        return False
    result = lst[0]
    for val in lst:
        if val < result:
            result = val
    return result

print(minimum([10,6,5,-7]))
print(minimum([]))

def maximum(lst):
    if len(lst) == 0:
        return False

    result = lst[0]
    for val in lst:
        if val > result:
            result = val
    return result

print(maximum([10,6,5,-7]))
print(maximum([]))

def ultimate_analysis(lst):
    result = {
        'sum_total': None,
        'maximum': None,
        'minimum': None,
        'average': None,
        'length': 0
    }
    if len(lst) == 0:
        return result
    else:
        result['sum_total'] = 0
        result['maximum'] = lst[0]
        result['minimum'] = lst[0]
    
    for val in lst:
        if val > result['maximum']:
            result['maximum'] = val
        elif val < result['minimum']:
            result['minimum'] = val

        result['sum_total'] += val
        result['length'] += 1
    result['average'] = result['sum_total'] / len(lst)

    return result

print(ultimate_analysis([10,6,5,-7]))
print(ultimate_analysis([]))

def reverse_list(lst):
    half_len = int(len(lst) / 2)
    for i in range(half_len):
        lst[i] , lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]
    return lst

print(ultimate_analysis([10,6,5,-7]))