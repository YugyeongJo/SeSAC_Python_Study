def get_insert_idx(res, elem, 
        cmp = lambda x, y: x if x > y else y, ):

    for i, e in enumerate(res):
        case = cmp(elem, e)
        if elem == cmp(elem, e): # elem > e:
            return i 
    
    return len(res)


def sort3_insert(lst, cmp = lambda x, y: x if x > y else y):
    res = []

    for elem in lst:
        new_idx = get_insert_idx(res, elem, cmp = cmp)
        res.insert(new_idx, elem)
    
    return res 

def merge_sort_divide(lst, cmp = lambda x, y: x if x > y else y):
    # 나누기
    if len(lst) >= 2:
        mid = len(lst)//2
        
        left = merge_sort(lst[:mid], cmp)
        right = merge_sort(lst[mid:], cmp)
    
        return merge_sort(left, right)
    else: 
        return lst
    
def merge_sort(left, right, cmp = lambda x, y: x if x > y else y):
    # 합치기
    i = j = 0
    res = []
    
    while i < len(left) and j < len(right):
        if left[i] == cmp(left[i], right[j]):
            res.append(right[j])
            j += 1
        else:
            res.append(left[i])
            i += 1
            
    if i == len(left):
        while j < len(right):
            res.append(right[j])
            j += 1
    else:
        while i < len(left):
            res.append(left[i])
            i += 1
            
    return res

def quick_sort(lst, cmp = lambda x, y: x if x > y else y):
    return lst 

def tim_sort(lst, cmp = lambda x, y: x if x > y else y):
    return lst 