# --------------------------------------------
# 1. 패턴 찍는 함수들 만들어보기 
# 
# 
# 1) 피라미드 찍어보기 - 1 
#
# 다음과 같은 패턴의 높이를 받아, 다음 패턴을 프린트하는 함수 pyramid1를 짜 보세요. 
#
#     *
#    ***
#   *****
#  *******
# *********
# --------------------------------------------

# write your code here 

def pyramid1(n):
    empty = ' '
    star = '*'

    for i in range(n):
        line = empty*(n-(i+1)) + star*((2*i)+1)
        print(line)
        
    pass

# n = int(input())
# pyramid1(n)

# --------------------------------------------
# 2) 피라미드 찍어보기 - 2 
# 
# 다음과 같은 패턴의 높이를 받아, 다음 패턴을 프린트하는 함수 pyramid2를 짜 보세요. 
# 
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
# --------------------------------------------

# write your code here 
def pyramid2(n):
    empty = ' '
    pattern = ' *'
    
    for i in range(n):
        line = empty*(n-(i+1)) + '*' + (pattern*i)
        print(line)
    pass

# n = int(input())
# pyramid2(n)

# --------------------------------------------
# 3) 피라미드 찍어보기 - 3 
# 
# 다음과 같은 패턴의 높이를 받아, 다음 패턴을 프린트하는 함수 pyramid3를 짜 보세요. 
#
#     A 
#    A B 
#   A B C 
#  A B C D 
# A B C D E 
# --------------------------------------------

# write your code here 
def pyramid3(n):
    import string 
    
    empty = ' '
    alphabet_upper = [i for i in string.ascii_uppercase]
    alphabet = ''
    
    for i in range(n): 
        empty_line = empty*(n-(i+1))
        alphabet += (alphabet_upper[i] + ' ')
        line = empty_line + alphabet
        print(line)     
    pass

# n = int(input())
# pyramid3(n)
    
# -------------------------------------------- 
# 4) 피라미드 찍어보기 - 4 
# 
# 다음과 같은 패턴의 높이를 받아, 다음 패턴을 프린트하는 함수 pyramid4를 짜 보세요. 
# 
#       1 
#      1 1 
#     1 2 1 
#    1 3 3 1 
#   1 4 6 4 1 
# --------------------------------------------

# write your code here 
def pyramid4(n):
    empty = ' '
    
    for i in range(n): 
        empty_line = empty*(n-(i+1))
        
    pass

# --------------------------------------------
# 5) 다음 패턴을 찍는 함수 sierpinski_triangle을 짜 보세요. 
#
# n = 1
#    *
#   * * 
#  *   *
# * * * *
#
# n = 2
#         *
#        * *
#       *   *
#      * * * *
#     *       * 
#    * *     * *
#   *   *   *   * 
#  * * * * * * * * 
# 
# n = 3 
#                 *
#                * *
#               *   *
#              * * * *
#             *       * 
#            * *     * *
#           *   *   *   * 
#          * * * * * * * *
#         *               *   
#        * *             * *  
#       *   *           *   * 
#      * * * *         * * * *
#     *       *       *       *  
#    * *     * *     * *     * *
#   *   *   *   *   *   *   *   * 
#  * * * * * * * * * * * * * * * *
# --------------------------------------------

# write your code here 
def sierpinski_triangle(n):
    
    
    pass

star = '*'
empty = ' '
n = 3

for j in range(1, n):
    for i in range(4):
        if i == 0:
            line = ((4*j)*empty) + empty*(4-(i+1)) + star
        elif i == 3:
            line = ((4*j)*empty) + (star + empty) * (i+1)
        else: 
            line = ((4*j)*empty) + empty*(4-(i+1)) + star + empty*((2*i)-1) + star
        print(line)

# --------------------------------------------
# 2. 여러 리스트 관련 함수들 구현해보기 
#
# 아래 함수들은 대부분 itertools에 있는 함수들임. 
# itertools를 쓰지 말고 구현해 볼 것.  
#
# 1) accumulate(lst, function = lambda x, y : x+y)
# 
# lst의 각 원소들에 대해서, function을 누적하여 적용한 리스트를 반환. 
# lst -> [lst[0], f(lst[0], lst[1]), f(lst[2], f(lst[1], lst[0])), ...] 
# --------------------------------------------

# write your code here 
def accumulate(lst, function = lambda x, y: x+y):
    result = []
    answer = lst[0]
    x = 0
    for i in range(len(lst)-1):
        result.append(answer)
        x = answer 
        y = lst[i+1]
        answer = function(x, y)
    
    answer = function(x, lst[-1])
    result.append(answer)
    
    print(result)
    pass

# lst = [1, 3, 5]
# accumulate(lst, function = lambda x, y: x+y)

# --------------------------------------------
# 2) batched(lst, n)
# 
# lst의 원소들을 n개의 인접한 원소들끼리 묶은 리스트를 반환. 
# ex) batched([1,2,3,4,5], 2) 
#     >> [(1,2), (3,4), (5,)]
# ex) batched(['a', 'b', 1, 3, 6, 1, 3, 7], 3) 
#     >> [('a', 'b', 1), (3, 6, 1), (3, 7)]
# --------------------------------------------

# write your code here 
lst = [1,2,3,4,5]
n = 2

def batched(lst, n):
    for i in range(n):
        lst[i:i+n]
    
    pass

# --------------------------------------------
# 3) product(args)
# 
# list들의 list args를 받아서, 각각의 리스트에서 하나씩의 원소를 뽑은 튜플들의 리스트를 반환. 
# ex) product([[1,2,3], [4,5,6]])
#     >> [(1,4), (1,5), (1,6), 
#         (2,4), (2,5), (2,6), 
#         (3,4), (3,5), (3,6),] 
# --------------------------------------------

# write your code here 
args = [[1,2,3], [4,5,6,7], [8, 9, 10]]
count = len(args)

result = [0 for i in range(count)]

for i in range():
    
print(result)
def product(args):
        
    pass



# --------------------------------------------
# 4) permutations(lst, r) 
#
# lst 안의 원소들 r개로 이루어진 permutation의 리스트를 반환. 
# permutation이란, 순서를 가지면서 중복을 허용하지 않는 부분집합을 의미함. 
# 즉 여기서는 1,2와 2,1은 다르고, 1,1은 허용되지 않음. 
# ex) permutations([1,2,3,4,5], 2)
#     >> [(1,2), (1,3), (1,4), (1,5), 
#         (2,1), (2,3), (2,4), (2,5), 
#         (3,1), (3,2), (3,4), (3,5), 
#         (4,1), (4,2), (4,3), (4,5), 
#         (5,1), (5,2), (5,3), (5,4),]
# --------------------------------------------

# write your code here 
def permutations(lst, r):
    pass

# --------------------------------------------
# 5) combination(lst, r) 
#
# lst 안의 원소들 r개로 이루어진 combination의 리스트를 반환. 
# combination이란, 순서를 가지지 않으면서 중복을 허용하지 않는 부분집합을 의미함. 
# 즉 여기서는 1,2와 2,1은 같고, 1,1은 허용되지 않음. 
# ex) combination([1,2,3,4,5], 2)
#     >> [(1,2), (1,3), (1,4), (1,5), 
#         (2,3), (2,4), (2,5), 
#         (3,4), (3,5), 
#         (4,5), ]
# --------------------------------------------

# write your code here 
def combination(lst, r):
    pass

# --------------------------------------------
# 6) combination_with_duplicate(lst, r)
#
# lst 안의 원소들 r개로 이루어진 중복을 허용하는 combination의 리스트를 반환. 
# ex) combination_with_duplicate([1,2,3,4,5], 2)
#     >> [(1,1), (1,2), (1,3), (1,4), (1,5), 
#         (2,2), (2,3), (2,4), (2,5), 
#         (3,3), (3,4), (3,5), 
#         (4,4), (4,5),
#         (5,5), ]
# --------------------------------------------

# write your code here 
def combination_with_duplicate(lst, r):
    pass

    


