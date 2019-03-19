def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
    for passnum in range(len(items)-1,0,-1):
        for i in range(passnum):
            if items[i]>items[i+1]:
                temp = items[i]
                items[i] = items[i+1]
                items[i+1] = temp
        return items

def merge(l, r):
    """Merge sort merging function."""

    left_index, right_index = 0, 0
    result = []
    while left_index < len(l) and right_index < len(r):
        if l[left_index] < r[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(r[right_index])
            right_index += 1

    result += l[left_index:]
    result += r[right_index:]
    return result

def merge_sort(items):
    '''Return array of items, sorted in ascending order'''

    if len(items) <= 1:
        return items

    half = len(items) // 2
    l = merge_sort(items[:half])
    r = merge_sort(items[half:])

    return merge(l, r)        
