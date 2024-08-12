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

def merge_sort(lst, cmp = lambda x, y: x if x > y else y):
    # 나누기
    if len(lst) >= 2:
        mid = len(lst)//2
        
        left = merge_sort(lst[:mid], cmp)
        right = merge_sort(lst[mid:], cmp)
    
        return merge(left, right, cmp)
    else: 
        return lst
    
def merge(left, right, cmp = lambda x, y: x if x > y else y):
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
    left, center, right = [], [], []
    if lst == []:
        return lst
    
    pivot = lst[-1]
    
    if len(lst) >= 2:
        for i in range(len(lst)):
            # if cmp(lst[i], pivot) == pivot:
            #     left.append(lst[i])
            # elif cmp(lst[i], pivot) == lst[i]:
            #     right.append(lst[i])
            if lst[i] > pivot:
                left.append(lst[i])
            elif lst[i] < pivot:
                right.append(lst[i])
            else:
                center.append(lst[i])
    else:
        return lst
            
    return quick_sort(left) + center + quick_sort(right)

def tim_sort(lst, cmp = lambda x, y: x if x > y else y):
    # 나누기
    if len(lst) <= 4:
        return sort3_insert(lst)
    else: 
        mid = len(lst)//2
        
        left = tim_sort(lst[:mid], cmp)
        right = tim_sort(lst[mid:], cmp)
        return merge(left, right, cmp)