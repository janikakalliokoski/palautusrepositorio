class Player:
    def __init__(self, name, team, goals, assists, nationality):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.nationality = nationality
        self.total = self.goals + self.assists

    def __str__(self):
        total = self.goals + self.assists
        return(f"{self.name:20} {self.team} {self.goals}+{self.assists}={total}")
