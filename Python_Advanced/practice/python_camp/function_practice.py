import random 

# --------------------------------------------
# 1. max / min 구현하기 
#
# cmp라는 함수를 이용한 min/max 구현하기. 
# cmp는 두 원소 중 더 큰 것을 반환하는 함수. 
# --------------------------------------------

def my_max(lst, cmp = lambda x, y: x if x > y else y):
    
    if not lst:
        return None
    
    max_element = lst[0]
    
    for x in lst[1:]:
        max_element = cmp(max_element, x)
    
    return max_element

def my_min(lst, cmp = lambda x, y: x if x > y else y):
    
    if not lst:
        return None
    
    min_element = lst[0]
    
    for x in lst[1:]:
        if cmp(min_element, x) == min_element:
            min_element = x
        # else:
        #     min_element = min_element
        
    return min_element

# --------------------------------------------
# 2. sort 구현하기 
# 
# 1) 그냥 순서대로 오름차순으로 정렬하기 
# 2) 오름차순, 내림차순으로 정렬하기 
# 3) 주어진 기준 cmp에 맞춰서 오름차순, 내림차순으로 정렬하기 
# 4) 주어진 기준 cmp가 큰 element를 출력하거나, 같다는 결과를 출력하게 만들기 
# 5) cmp상 같은 경우 tie-breaking하는 함수 넣기 
# --------------------------------------------

# 인덱스 요소 찾기
def find_insert_index(lst, x):
    for i in range(len(lst)):
        if x < lst[i]:
            return i
    return len(lst)

# main
def sort1(lst):
    
    if not lst:
        return []
    
    lst_sort = [lst[0]]
    
    for x in lst[1:]:
        idx = find_insert_index(lst_sort, x)
        lst_sort.insert(idx, x)
    
    return lst_sort 

# =================================== #
# 강사님 code
def sort1_min(lst):
    res = []
    lst_copy = [e for e in lst]
    n = len(lst)
    
    while len(res) < n:
        m = my_min(lst_copy, lambda x, y: x if x > y else y)
        res.append(m)
        lst_copy.remove(m)      
            
    return res

def get_insert_idx(res, elem):
    idx = 0
    
    for i, e in enumerate(res):
        if elem < e:
            return i
        
    return len(res)

def sort1_insert(lst):
    res = []
    
    for idx, elem in enumerate(lst):
        new_idx = get_insert_idx(res, elem)
        res.insert(new_idx, elem)
        
    return res

# print(sort1_min([5, 3, 8, 6, 7, 2]))
# #####################################

def find_insert_index(lst, x, upper_to_lower):
    for i in range(len(lst)):
        if (upper_to_lower and x < lst[i]) or (not upper_to_lower and x > lst[i]):
            return i
    return len(lst)

def sort2(lst, upper_to_lower = True):

    if not lst:
        return []
    
    lst_sort = [lst[0]]
    
    for x in lst[1:]:
        idx = find_insert_index(lst_sort, x, upper_to_lower)
        lst_sort.insert(idx, x)
    
    return lst_sort 


# lst = [5, 3, 8, 6, 7, 2]
# print(sort2(lst, upper_to_lower=True)) 
# print(sort2(lst, upper_to_lower=False))

# =================================== #
# 강사님 code

def sort2_min(lst, upper_to_lower=True):
    res = []
    
    lst_copy = [e for e in lst]
    n = len(lst)
    
    while len(res) < n:
        m = my_min(lst_copy, lambda x, y: x if x > y else y)
        if not upper_to_lower:
            res.append(m)
        else:
            res = [m] + res
        lst_copy.remove(m)
        
    return res

def get_insert_idx(res, elem, upper_to_lower = False):
    
    for i, e in enumerate(res):
        if not upper_to_lower:
            if elem < e:
                return i
        else:
            if elem > e:
                return i
        
    return len(res)

def sort2_insert(lst, upper_to_lower=True):
    res = []
    
    for idx, elem in enumerate(lst):
        new_idx = get_insert_idx(res, elem, upper_to_lower = upper_to_lower)
        res.insert(new_idx, elem)
    
    return res    

# #####################################

def find_insert_index(lst, x, upper_to_lower, cmp):
    for i in range(len(lst)):
        if (upper_to_lower and cmp(x, lst[i]) == x) or (not upper_to_lower and cmp(x, lst[i]) != x):
            return i
    return len(lst)

def sort3(lst, upper_to_lower = True, cmp = lambda x, y: x if x > y else y):
    
    if not lst:
        return []
    
    lst_sort = [lst[0]]
    
    for x in lst[1:]:
        idx = find_insert_index(lst_sort, x, upper_to_lower, cmp)
        lst_sort.insert(idx, x)
    
    return lst_sort

# lst = [5, 3, 8, 2, 7, 2]
# print(sort3(lst, True, cmp = lambda x, y: x if x % 3 > y % 3 else y))
# print(sort3(lst, False))

# =================================== #
# 강사님 code

def sort3_min(lst, upper_to_lower=True, cmp = lambda x, y: x):
    res = []
    
    lst_copy = [e for e in lst]
    n = len(lst)
    
    while len(res) < n:
        m = my_min(lst_copy, cmp)
        if not upper_to_lower:
            res.append(m)
        else:
            res = [m] + res
        lst_copy.remove(m)
        
    return res 

def get_insert_idx(res, elem, upper_to_lower = True, cmp = lambda x, y: x if x > y else y):
    
    for i, e in enumerate(res):
        if not upper_to_lower:
            if e == cmp(elem, e):
                return i
        else:
            if e == cmp(elem, e):
                return i
        
    return len(res)

def sort3_insert(lst, upper_to_lower=True, cmp = lambda x, y: x if x > y else y):
    res = []
    
    for idx, elem in enumerate(lst):
        new_idx = get_insert_idx(res, elem, upper_to_lower = upper_to_lower, cmp=cmp)
        res.insert(new_idx, elem)
    
    return res    

# #####################################

def cmp(x, y):
    if x > y : 
        return x
    elif x < y : 
        return y
    else: 
        return 0

def find_insert_index(lst, x, upper_to_lower, cmp):
    for i in range(len(lst)):
        if (upper_to_lower and cmp(x, lst[i]) == x) or (not upper_to_lower and cmp(x, lst[i]) != x):
            return i
        
    return len(lst)

def sort4(lst, upper_to_lower = True, cmp = lambda x, y: x if x > y else y):
    
    if not lst:
        return []
    
    lst_sort = [lst[0]]
    
    for x in lst[1:]:
        idx = find_insert_index(lst_sort, x, upper_to_lower, cmp)
        lst_sort.insert(idx, x)
        
# lst = [5, 3, 8, 2, 7, 2]
# print(sort3(lst, True, cmp = cmp))
# print(sort3(lst, False))
# #####################################

def cmp(x, y):
    if len(x) > len(y): return x 
    elif len(x) < len(y): return y 
    else: return 'equal'

def my_cmp(x, y):
    if len(x) < len(y): return x 
    elif len(x) > len(y): return y 
    else: return 'equal'

def find_insert_index(lst, x, upper_to_lower, cmp, tie_breaker):
    for i in range(len(lst)):
        if cmp(x, lst[i]) == 'equal':
            if upper_to_lower:
                return i if tie_breaker(x, lst[i]) == x else i+1
            else:
                return i+1 if tie_breaker(x, lst[i]) == x else i
        elif (upper_to_lower and cmp(x, lst[i]) == x) or (not upper_to_lower and cmp(x, lst[i]) == lst[i]):
            return i 
    return len(lst)

def sort5(lst, upper_to_lower = True, cmp = lambda x, y: x if x > y else y, tie_breaker = lambda x, y: random.choice([x,y])):

    if not lst:
        return []
    
    lst_sort = [lst[0]]
    
    for x in lst[1:]:
        idx = find_insert_index(lst_sort, x, upper_to_lower, cmp, tie_breaker)
        lst_sort.insert(idx, x)
    
    return lst_sort
     
# lst = [(1, 2), (3, 4, 5), (3, 6), ]
# print(sort5(lst, True, cmp = my_cmp, tie_breaker = lambda x, y: x if sum(x) > sum(y) else y))
# print(sort5(lst, False, cmp = cmp, tie_breaker = lambda x, y: x if sum(x) > sum(y) else y))

# =================================== #
# 강사님 code

def my_min(lst, cmp = lambda x, y: x, tie_breaker = lambda x, y : x):
    
    if not lst:
        return None
    
    min_element = lst[0]
    
    for x in lst[1:]:
        case = cmp(x, min_element)
        if case == min_element:
            min_element = x
        elif case == x:
            pass
        else:
            tie_case = tie_breaker(x, min_element)
            if tie_case == min_element:
                min_element = x
        
    return min_element

def sort5_min(lst, upper_to_lower = True, cmp=lambda x, y: x, tie_breaker = lambda x, y: random.choice([x, y])):
    res = []
    lst_copy = [e for e in lst]
    n = len(lst)
    
    while len(res) < n:
        m = my_min(lst_copy, cmp = cmp, tie_breaker = tie_breaker)
        if not upper_to_lower:
            res.append(m)
        else:
            res = [m] + res
        lst_copy.remove(m)
    
    return res

def my_compare(x, y):
    if x[0] > y[0]: return x
    elif y[0] > x[0]: return y
    else: return "equal"
    
def get_insert_idx(res, elem, upper_to_lower = True, cmp = lambda x, y: x if x > y else y, tie_breaker = lambda x, y: random.choice([x,y])):
    
    for i, e in enumerate(res):
        case = cmp(elem, e)
        if not upper_to_lower:
            if e == cmp(elem, e):
                return i
            elif case != elem:
                tie_breaker()
        else:
            if e == cmp(elem, e):
                return i
        
    return len(res)

def sort5_insert(lst, upper_to_lower=True, cmp = lambda x, y: x if x > y else y, tie_breaker = lambda x, y: random.choice([x,y])):
    res = []
    
    for idx, elem in enumerate(lst):
        new_idx = get_insert_idx(res, elem, upper_to_lower = upper_to_lower, cmp=cmp, tie_breaker = tie_breaker)
        res.insert(new_idx, elem)
    
    return res      

# ####################################### #
# --------------------------------------------
# os_file_concept.py 해보고 올 것 
# --------------------------------------------

import pickle

# --------------------------------------------
# 3. safe pickle load/dump 만들기 
# 
# 일반적으로 pickle.load를 하면 무조건 파일을 읽어와야 하고, dump는 써야하는데 반대로 하면 굉장히 피곤해진다. 
# 이런 부분에서 pickle.load와 pickle.dump를 대체하는 함수 safe_load, safe_dump를 짜 볼 것.  
# hint. 말만 어렵고 문제 자체는 정말 쉬운 함수임.
# --------------------------------------------

def safe_load(pickle_path):
    return pickle.load(open(pickle_path, 'rb'))

def safe_dump(obj, pickle_path):
    return pickle.dump(obj, open(pickle_path, 'wb+'))

# --------------------------------------------
# 4. 합성함수 (추후 decorator)
# 
# 1) 만약 result.txt 파일이 없다면, 함수의 리턴값을 result.txt 파일에 출력하고, 만약 있다면 파일 내용을 읽어서 
#    '함수를 실행하지 않고' 리턴하게 하는 함수 cache_to_txt를 만들 것. txt 파일은 pickle_cache 폴더 밑에 만들 것.  
# 2) 함수의 실행값을 input에 따라 pickle에 저장하고, 있다면 pickle.load를 통해 읽어오고 없다면 
#    실행 후 pickle.dump를 통해 저장하게 하는 함수 cache_to_pickle을 만들 것. pickle 파일은 pickle_cache 폴더 밑에 만들 것. 
# 3) 함수의 실행값을 함수의 이름과 input에 따라 pickle에 저장하고, 2)와 비슷하게 진행할 것. pickle 파일은 pickle_cache 폴더 밑에, 각 함수의 이름을 따서 만들 것 
# --------------------------------------------
import os 
import pickle 

def create_dir(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
    else:
        print(f'{directory_name} does exists')

# directory_name = 'pickle_cache'
# create_dir(f'C:\\develops\\SeSAC_Python_Study\\Python_Advanced\\practice\\python_camp\\{directory_name}')
        
def function():
    from time import sleep 
    sleep(1)
    return str(1) 

def cache_to_txt(function):
    
    directory_name = 'pickle_cache'
    create_dir(directory_name)
    
    file_path = f'{directory_name}/result.txt'
    
    if not os.path.exists(file_path):
        res = function()
        f = open(file_path, 'w+', encoding='utf-8')
        f.write(res)
        f.close()
        return res
    else:
        f = open(file_path, 'r', encoding='utf-8')
        res = f.read() 
        f.close()
        return res

# cache_to_txt(function)

def double(x):
    print(f"double이 {x}으로 실행되었습니다.")
    return 2*x 

def triple(args):
    print(f"args = {args}")
    for x in args:
        a = 3*x
        print(x)
    return a

def create_dir(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
    else:
        print(f'{directory_name} does exists')
    return 
        
def cache_to_pickle(function):
    
    directory_name = 'pickle_cache'
    create_dir(directory_name)
    
    def my_function(*args, **kargs):
        
        file_path = f'{directory_name}/{args}result.pickle'
        
        if not os.path.exists(file_path):
            res = function(args)
            pickle.dump(res, open(file_path, 'wb+'))
            return res
        else:
            res = pickle.load(open(file_path, 'rb'))
            return res
        
    return my_function
        
# print(cache_to_pickle(triple)(1,2,3,4,5,6,10))

# stdout
# >> 2
# file ouput
# pickle_cache/1.pickle             # in case of (2)
# pickle_cache/double/1.pickle      # in case of (3)

# def f(g):
#     def h(x):
#         return g(x) + x
#     return h

# f(double)(3)

