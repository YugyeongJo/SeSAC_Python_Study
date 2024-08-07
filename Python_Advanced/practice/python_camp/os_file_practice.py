# --------------------------------------------
# 1. os 활용 예제 
# 
# 1) os 디렉토리 구조 출력해보기 
# 2) root directory 아래에 있는 특정 확정자 파일들 다 출력하기 
# 3) os 디렉토리 복사하기
# --------------------------------------------
import os 

def print_directory_tree(root):
    """os 디렉토리 구조 출력하는 함수
    """
    for elem in os.listdir(root):
        if os.path.isdir(elem):
            print(f'<DIR>\t\t{elem}')
        elif '.' in elem:
            extension = elem.split('.')[-1]
            print(f'{extension} file\t\t{elem}')

def list_extension_files(root, file):
    """root directory 아래에 있는 특정 확장자 파일들 다 출력하기
    """
    for elem in os.listdir(root):
        if '.' in elem:
            extension = elem.split('.')[-1]
            if extension == file:
                print(f'{extension} file\t\t{elem}')
            else: 
                pass
        else:
            pass

def copy_directory(src, dest):
    """os 디렉토리 복사하는 함수
    """

print_directory_tree('./')
# list_extension_files('./', 'png')