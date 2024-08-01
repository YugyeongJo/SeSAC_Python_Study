import sys 
try:
    from solution.exceptions import InvalidTokenException, NotClosedParenthesesException
except ImportError:
    from exceptions import InvalidTokenException, NotClosedParenthesesException

tokens = ['(', ')']



# 매칭되는 문자열 idx 찾기
def find_matching_pair(text, idx):
    """For a given text of parentheses and idx, find the index of matching parentheses in the text. 

    Args:
        str text 
        int idx 
    Returns:
        int
    Raises:
        InvalidTokenException: When the input contains invalid character.
        NotClosedParenthesesException: When it is impossible to find the matching parentheses. 
        ValueError: When the input idx is larger or equal to len(text) or is smaller than 0. 
    
    Examples:
        find_matching_pair('()', 0)
        >> 1 
        find_matching_pair('(())', 1)
        >> 2
        find_matching_pair(')', 0)
        >> NotClosedParenthesesException 
    """
    # 예외 상황 1 : 입력한 idx가 out of range일 경우
    if idx < 0 or idx >= len(text):
        raise ValueError("idx is larger or equal to len(text) or is smaller than 0.")
    
    num = 0
    for i, x in enumerate(text[idx:], start=idx):
        # 예외 상황 2 : ()가 아닐 경우
        if not all(c in '()' for c in text):
            raise InvalidTokenException("The input contains invalid character.")
    
        if x == tokens[0]:
            num += 1
        elif x == tokens[1]:
            num -= 1
            if num == 0:
                pair_idx = i
                break

    # 예외 상황 3
    if num != 0:
        raise NotClosedParenthesesException("it is impossible to find the matching parentheses.")    
    
    if pair_idx == -1:
        raise NotClosedParenthesesException("Matching parentheses not found.")

    return pair_idx
    

# 적용되는 rule function 
def determine_if_rule0(text):
    return text == ''

def determine_if_rule1(text):
    return not determine_if_rule0(text) and find_matching_pair(text, 0) == len(text)-1

def determine_if_rule2(text):
    return not determine_if_rule0(text) and not determine_if_rule1(text)



# 딕셔너리 반환
# rule 0 
def parse_empty_string():
    return {'node': '', 'rule': 0}


# 기본 값
# offset = 전체 문자열의 인덱스번호와 맞춰주려고 
def default_node_information(text, offset):
    res = {}
    
    res['node'] = text
    res['start'] = offset
    res['end'] = len(text)-1+offset
    
    return res


# 기본 값 + rule1
def update_rule1_data(text, res):
    assert determine_if_rule1(text)
    
    matching_pair_idx = find_matching_pair(text, 0)
    
    res['rule'] = 1
    res['left'] = {
        'node': '('
        , 'start': 0
        , 'end' : 0
    }
    res['right'] = {
        'node': ')'
        , 'start': matching_pair_idx
        , 'end' : matching_pair_idx
    }
    
    
    return res 

# 기본 값 + rule1 mid
def update_rule1_mid(text, res):
    assert determine_if_rule1(text)
    
    matching_pair_idx = find_matching_pair(text, 0)
    
    res['mid'] = parse_parentheses_with_offset(text[1:matching_pair_idx], offset=1)
    
    return res 


# 기본 값 + rule2
def update_rule2_data(text, res):  
    assert determine_if_rule2(text)
    
    res['rule'] = 2
    
    return res 

# 기본 값 + rule2 nodes
def update_rule2_nodes(text, res):
    assert determine_if_rule2(text)
    
    result = []
    idx = 0
    while idx < len(text)-1:
        jdx = find_matching_pair(text, idx)
        result.append((text[idx:jdx+1], idx))
        idx = jdx + 1
    
    # res_nodes = []
    # for t, i in result:
    #     res_nodes.append(parse_parentheses_with_offset(t, i))
    # res['nodes'] = res_nodes
    
    res['nodes'] = [parse_parentheses_with_offset(text, idx) for text, idx in result]
    
    return res 


# explain
def parse_parentheses(text):
    """For the given string, parse it in the form of dict. 

    For detailed explanation about the parsing process and the result format, consult parentheses/documents/assignment.txt file. 

    Args:
        str text
    Returns:
        dict 
    Raises:
        InvalidTokenException: When the input contains invalid character.
        NotClosedParenthesesException: When the input have a syntax error.
    Examples:

    parse_parentheses('')
    >> {
            'node': '',
            'rule': 0,  
    }
    parse_parentheses('()')
    >> {
            'node': '()', 
            'start': 0, 
            'end': 1,
            'rule': 1, 
            'left': {
                'node': '(', 
                'start': 0, 
                'end': 0, 
            },
            'mid': {
                'node': '', 
                'rule': 0, 
            }, 
            'right': {
                'node': ')',
                'start': 1, 
                'end': 1,   
            },
    }
    parse_parentheses('(())')
    >> {
            'node': '(())', 
            'start': 0, 
            'end': 3, 
            'rule': 1, 
            'left': {
                'node': '(', 
                'start': 0, 
                'end': 0, 
            }, 
            'mid': {}, // Same as parse_parentheses('()'), except for start/end attributes. 
            'right': {
                'node': ')', 
                'start': 3, 
                'end': 3, 
            }
    }
    parse_parentheses('()()')
    >> {
            'node': '()()', 
            'start': 0, 
            'end': 3, 
            'rule': 2, 
            'nodes': [
                {...},  // Same as parse_parentheses('()').
                {...},  // Same as parse_parentheses('()'), except for start/end attributes. 
            ]
    }
    parse_parentheses('(()())')
    >> {
            'node': '(()())', 
            'start': 0, 
            'end': 5, 
            'rule': 1, 
            'left': {...}, // Same as parse_parentheses('()')['left'] 
            'mid': {...}, // Same as parse_parentheses('()()'), except for start/end attributes. 
            'right': {...}, // Same as parse_parentheses('()')['left'], except for start/end attributes. 
    }
    """ 

    return parse_parentheses_with_offset(text)

# main
def parse_parentheses_with_offset(text, offset = 0):
    rule0 = determine_if_rule0(text)
    rule1 = determine_if_rule1(text) 
    rule2 = determine_if_rule2(text) 

    if rule0: # rule 0 
        return parse_empty_string()
    
    res = default_node_information(text, offset)

    if rule1: # rule 1
        res = update_rule1_data(text, res)
        res = update_rule1_mid(text, res)
    elif rule2: # rule 2 
        res = update_rule2_data(text, res) 
        res = update_rule2_nodes(text, res)     
    else:
        assert False, 'Something goes wrong' 
    
    return res 

def main():
    args = sys.argv
    with open(f'{sys.argv[1]}', 'r') as f:
        text = f.read().strip()
        print(parse_parentheses(text))

if __name__ == '__main__':
    main()