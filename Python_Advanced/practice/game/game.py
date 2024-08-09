import random

class Game:
    def __init__(self, players):
        self.players = players 

    def play_match(self, player1, player2):
        # player1, player2의 win_lose_history를 update하고 
        # elo rating 알고리즘에 따라 각자의 current_rating을 update할 것 
        # https://namu.wiki/w/Elo%20%EB%A0%88%EC%9D%B4%ED%8C%85 참고 

        pass 

    def match_players(self):
        # player들을 current_rating을 기반으로 
        
    def simulate(self):
        pass 

class Player:
    
    def __init__(self, player_id, initial_rating = 1000, actual_rating = 1000):
        self.win_lose_history = []
        self.current_rating = initial_rating
        assert actual_rating < 4000
        self.actual_rating = actual_rating
        

    def __str__(self):
        return f'{str(self.player_id)}: current rating - {self.current_rating}, actual_rating - {self.actual_rating}'

    @staticmethod
    def generate_random_player_id():
        return pass
    
    @staticmethod
    def generate_random_players(n):    
        return [Player(Player.generate_random_player_id(), actual_rating = random.gauss(1000, 100)) for _ in range(n)]

    
if __name__ == '__main__':
    player_list = Player.generate_random_players(100)
    
    # g = Game(player_list)
    # g.match_players(player_list[0], player_list[1])