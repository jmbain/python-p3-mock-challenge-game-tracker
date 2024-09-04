class Game:
    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and len(new_title) > 0 and not hasattr(self, "_title"):
            self._title = new_title


    def results(self):
        result_objs = []
        for r in Result.all:
            if r.game is self: 
                result_objs.append(r)
        return result_objs
        

    def players(self):
        players_set = set()
        for r in self.results():
            players_set.add(r.player)
        return list(players_set)
        

    def average_score(self, player):
        total = 0
        count = 0
        for r in self.results():
            if r.player is player:
                total += r.score
                count += 1
        if count == 0:
            return None
        return total / count

    def __repr__(self) -> str:
        return f"<Game {self.game}>"

class Player:
    def __init__(self, username):
        self.username = username
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        if isinstance(new_username, str) and 2<= len(new_username) <=16:
            self._username = new_username

    def results(self):
        result_objs = []
        for r in Result.all:
            if r.player is self:
                result_objs.append(r)
        return result_objs
        
        # return [r for r in Result.all if r.player is self]

    def games_played(self):
        games = set()
        for r in self.results():
            games.add(r.game)
        return list(games)

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        count = 0
        for r in self.results():
            if r.game == game:
                count += 1
        return count
        
    @classmethod
    def highest_scored(cls, game):
        players = list(game.players())
        max_player = players[0]
        max_player_avg = game.average_score(players[0])
        for player in game.players():
            avg = game.average_score(player)
            if avg > max_player_avg:
                max_player_avg = avg
                max_player = player
        return max_player, max_player_avg


    def __repr__(self) -> str:
        return f"<Player {self.username}>"

class Result:
    all = []
    
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, new_score):
        if isinstance(new_score, int) and 1 <= new_score <= 5000 and not hasattr(self, "_score"):
            self._score = new_score
    
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, new_player):
        if isinstance(new_player, Player):
            self._player = new_player

    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, new_game):
        if isinstance(new_game, Game):
            self._game = new_game
    
    def __repr__(self) -> str:
        return f"<Result {self.player.username} {self.game.title} {self.score}>"