import random 

small_max_num = 10
max_num = 10000000
small_random_int = random.randint(0, small_max_num)
random_int = random.randint(0, max_num)
random_float = random.uniform(0, max_num)

def updown_game_easy(guess):
    if guess > small_random_int:
        return 'down'
    elif guess < small_random_int:
        return 'up'
    return guess == small_random_int

def updown_game_medium(guess):
    if guess > random_int:
        return 'down'
    elif guess < random_int:
        return 'up'
    return guess == random_int

def updown_game_hard(guess):
    if guess - random_float > 0.001:
        return 'down'
    elif guess - random_float < -0.001:
        return 'up' 
    return abs(random_float - guess) < 0.001


if __name__ == '__main__':
    from finder import manual_finder, naive_finder, smart_finder
    from time import time 

    begin = time()
    print(smart_finder(updown_game_medium))
    end = time()

    print(end - begin)
    