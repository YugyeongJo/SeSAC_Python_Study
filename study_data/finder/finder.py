"""Implement a better finder to find the right argument for the function. 

Your job is to implement a function that accepts another function(call this f) and additional information(related to possible candidates) as input, and returns the argument that f returns True. 

As a hint, f will return 'up' or 'down'. When f needs larger input value to return True, it will return 'up'. Else, it will return 'down'. 

You will be asked to implement 2 finder functions; naive_finder and smart_finder. 

1) naive_finder

Function naive_finder assumes that the test function only accepts integer inputs; therefore, naive_finder can (naively) iterate all the possible candidates. It will take long - but that's why it's called naive.  Function naive_finder accepts another function f and a candidate list as input. When naive_finder is called, it iterates over all possible candidates, applies all candidates to the function one at a time, and returns when the result is True. 

naive_finder should be able to find right argument for updown_game.updown_game_easy and updown_game.updown_game_medium. 

2) smart_finder

Function smart_finder accepts another function, and the max/min value of the input for the function f. To implement the smart_finder function, think of how you actually play '업다운 게임'. 

smart_finder should be able to find right argument for updown.game.updown_game_hard and animation.check_collision. 
"""
# 실행
def manual_finder(f):
    while True:
        i = input(f'Guess the argument!\nGuess is: ')
        res = f(float(i))
        if res is True:
            print(f'You found the right argument!; {float(i)}')
            return float(i)
            
        print(res) 
    

# def naive_finder(f, low=1, high=max_num):
#     low = 1
#     high = 10000000
    
#     while True:
#         i = high//2
#         res = f(i)
#         if res is True:
#             print(f'You found the right argument!; {i}')
#             return i
#         elif res == 'up':
#             low = i
#         elif res == 'down':
#             high = i
#         print(res)
        
def naive_finder(f, low=1, high=10000000):
    while low <= high:
        guess = (low + high) // 2  # 중앙값 계산
        print(f"컴퓨터의 추측: {guess}")
        
        res = f(guess)
        
        if res is True:
            print(f'You found the right argument!; {guess}')
            return guess
        elif res == 'up':
            low = guess + 1  # low를 중앙값 다음으로 조정
        elif res == 'down':
            high = guess - 1  # high를 중앙값 이전으로 조정
        else:
            print("Invalid response from function")
    


def smart_finder(f, min_input = 0.0, max_input = 100.0):
    while min_input <= max_input:
        guess = (min_input + max_input) / 2  # 중앙값 계산
        print(f"컴퓨터의 추측: {guess}")
        
        res = f(guess)
        
        if res is True:
            print(f'You found the right argument!; {guess}')
            return guess
        elif res == 'up':
            min_input = guess + 1  # min_input 중앙값 다음으로 조정
        elif res == 'down':
            max_input = guess - 1 # max_input 중앙값 이전으로 조정
        elif res == None:
            min_input += 1
            max_input -= 2
        else:
            print("Invalid response from function")


# if __name__ == '__main__':
#     manual_finder()