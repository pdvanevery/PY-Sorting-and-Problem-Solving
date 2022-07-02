# Write your solution for algorithm 5 below
lst = [5, 10, 4, 7, 6, 2]

def sort_and_sum(lst, target):
    result = lst.sort()
    left = 0
    right = len(lst)-1
    while left < right:
        if result[left] + result[right] == target:
            print (f"{result[left]} + {result[right]} = {target}, at left = {left} and right = {right}")
        


""" def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    # Split the list
    length = len(arr)
    mid = length // 2
    
    left = arr[:mid]
    right = arr[mid:]
    
    print(f'left --> {left}')
    print(f'right --> {right}')
      
    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    result = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    
    return result

    """
