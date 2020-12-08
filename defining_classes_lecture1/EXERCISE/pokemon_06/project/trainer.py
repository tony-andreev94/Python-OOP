#from defining_classes_lecture1.EXERCISE.pokemon_06.project.pokemon import Pokemon


class Trainer:

    def __init__(self, name: str):
        self.name = name
        self.pokemon = []
        self.pokemon_with_details = {}

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemon:
            return "This pokemon is already caught"

        pokemon_details = pokemon.pokemon_details()
        self.pokemon.append(pokemon.name)
        self.pokemon_with_details[pokemon.name] = pokemon.health
        return f"Caught {pokemon_details}"

    def release_pokemon(self, pokemon_name: str):
        if pokemon_name in self.pokemon:
            self.pokemon.remove(pokemon_name)
            self.pokemon_with_details.pop(pokemon_name)
            return f"You have released {pokemon_name}"

        return "Pokemon is not caught"

    def trainer_data(self):
        data = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n"
        for each in self.pokemon_with_details:
            data += f'- {each} with health {self.pokemon_with_details[each]}\n'

        return data


# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())
