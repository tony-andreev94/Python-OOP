#from defining_classes_lecture1.EXERCISE.guild_system_07.project.player import Player


class Guild:

    def __init__(self, name: str):
        self.name = name
        self.list_of_players = []

    def player_has_no_guild(self, player):
        if player.guild == "Unaffiliated":
            return True
        else:
            return False

    def assign_player(self, player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."

        if player.guild == "Unaffiliated":
            self.list_of_players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

        return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str):
        if player_name not in self.list_of_players:
            return f"Player {player_name} is not in the guild."

        self.list_of_players.remove(player_name)
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        players = ""
        for player in self.list_of_players:
            players += f"{player.player_info()}\n"

        result += players
        return result


# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())
