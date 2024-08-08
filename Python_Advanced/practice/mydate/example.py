
def lst_sub(l, r, table = {0:12, 1:31, 2:24, 3:60, 4:60}):
    res = []
    for a, b in zip(l, r):
        res.append(a-b)
    
    first_nonzero_idx = 0
    
    for idx, elem in enumerate(res):
        if elem > 0:
            first_nonzero_idx = idx 
            break 
    else:
        assert False, 'l is smaller than r or euql to r'
        
    for idx, elem in enumerate(res[first_nonzero_idx:-1], start = first_nonzero_idx):
        if res[idx+1] < 0:
            res[idx] = res[idx] - 1
            res[idx+1] = res[idx+1] + table[idx]
    
    return res 

def day_check(lst):
    year, month = lst[0], lst[1] + 1
    if month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def lst_add(l, r, table = {0:lambda lst:12, 
                           1:day_check, 
                           2:lambda lst: 24, 
                           3:lambda lst: 60, 
                           4:lambda lst: 60}):
    res = []
    for a, b in zip(l, r):
        res.append(a+b)
        
    for idx, elem in enumerate(res[1::-1]):
        idx = len(res)-idx-1
        cur_max = table[idx-1](res)
        print(res, cur_max)
        
        while res[idx] > cur_max:
            res[idx] = res[idx] - cur_max
            res[idx - 1] += 1
            cur_max = table[idx-1](res)
            print(res)

    return res 
    
if __name__ == '__main__':
    print(lst_sub([2023, 2, 14], [2022, 12, 15]))
    print(lst_add([2023, 1, 31], [0, 0, 31]))