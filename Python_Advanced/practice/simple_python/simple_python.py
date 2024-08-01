# simple_python이 들어오면 엔터 기준으로 split 진행

simple_python = """
a=1
b=2
a+b+3
"""

def eval_simple_python(text):
    list_text = text.strip().split("\n")
    
    namespace = {}
    res = None
    
    for x in list_text:
        if x != '':
            res, namespace = eval_line(x, namespace)
        # try :
        #     if '=' in x:

        #     else: 
        #         return print(x)
        # except :
        #     raise NameError("Error")
    return res
        
def eval_line(line, namespace):
    if is_assingment(line):
        name, value = parse_assignment(line, namespace)
        namespace[name] = value
        return None, namespace
    elif is_expression(line):
        value = eval_expression(line, namespace)
        return value, namespace
    
    return value, namespace

def is_assingment(line):
    if '=' in line:
        left, right = line.split("=")
        name = left.strip() # check if name is valid
        expr = right.strip()
        return True
    else: 
        return False

def is_expression(line):
    return not is_assingment(line)

def parse_assignment(line, namespace):
    left, right = line.split("=")
    name = left.strip() # check if name is valid
    expr = right.strip()
    
    value = eval_expression(expr, namespace)
    
    return name, value
    
def eval_expression(line, namespace):
    values = line.split('+')
    values = [v.strip() for v in values]
    result = 0
    
    for v in values:
        if v.isnumeric():
            result += int(v)
        else:
            if v in namespace:
                result += namespace[v]
            else:
                raise NameError("")
            
    return result

print(eval_simple_python(simple_python))