import os 

# from ADT.tree import Tree 
from data_structure.tree import Tree

# ////////////// 선생님 이게 왜 전체 구조가 아니라 일부만 나오는지 모르겠어요.....
def get_directory_tree(directory, ignore_directories = [], ignore_extensions = []):
    return str(tree_maker(directory))

def tree_maker(directory):
    root = directory
    directory_list = os.listdir(root)
    
    children = []
    for x in directory_list:
        path = f'{root}/{x}'
        if os.path.isdir(x):
            child = tree_maker(path)
            children.append(child)
        else:
            children.append(Tree(x))
    
    return Tree(root, children)

# def hint(directory):
#     print(directory)
#     for elem in os.listdir(directory):
#         sub_path = f'{directory}/{elem}'
        
#         if os.path.isdir(sub_path):
#             # do sth 
#             print(sub_path, elem)
#         else:
#             print(sub_path)

if __name__ == '__main__':
    print(get_directory_tree('.'))
    # print(hint('.'))
"""
./
├── ADT/
│   ├── queue.py
│   ├── stack.py
│   ├── tree.py
│   └── __pycache__/
│       ├── queue.cpython-39.pyc
│       └── stack.cpython-39.pyc
├── bank_simulation.py
├── data_structure/
│   ├── linked_list.py
│   ├── node.py
│   ├── tree.py
│   └── __pycache__/
│       ├── linked_list.cpython-39.pyc
│       ├── node.cpython-39.pyc
│       └── tree.cpython-39.pyc
├── formula.py
├── global_variables.py
├── os_tree_structure.py
├── sorting/
│   ├── experiment result/
│   │   ├── merge_sort.png
│   │   ├── quick_sort.png
│   │   ├── sort3_insert.png
│   │   ├── sort3_insert_1000.png
│   │   └── sorted.png
│   ├── measure_performance.py
│   ├── sorting.py
│   └── __pycache__/
│       └── sorting.cpython-39.pyc
├── util.py
└── __pycache__/
    ├── global_variables.cpython-39.pyc
    └── util.cpython-39.pyc
"""