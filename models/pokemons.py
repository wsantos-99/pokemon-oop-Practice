import data.pokemons_data as pokemons_data
import data.moves_data as moves_data
import data.type_matchups_data as type_matchup
from typing import cast
import random
import math


class Pokemon:
    def __init__(self, pokemon, name="", level=1, iv=0.1):
        pokemon_data = pokemons_data.POKEMONS[pokemon]
        self._data = pokemon_data

        if name:
            self._name = name
        else:
            self._name = pokemon_data["species"]

        self._species = pokemon_data["species"]
        self._types = pokemon_data["types"]
        self._level = level
        self._iv = 1 + iv

        self._hp = pokemon_data["hp"]
        self._attack = pokemon_data["attack"]
        self._defense = pokemon_data["defense"]
        self._speed = pokemon_data["speed"]

        self._update_stats()
        self._current_hp = self._hp

        self._moves = []
        for move in pokemon_data["moves"]:
            self._moves.append({
                "name": move,
                **moves_data.MOVES[move]
            })

    def __str__(self):
        return f"{self._name} {self._species} {self.level}"

    def _update_stats(self):
        self._hp = math.floor(self._data["hp"] * self._level * self._iv)
        self._attack = math.floor(self._data["attack"] * self._level * self._iv)
        self._defense = math.floor(self._data["defense"] * self._level * self._iv)
        self._speed = math.floor(self._data["speed"] * self._level * self._iv)

    @property
    def name(self):
        return self._name

    @property
    def species(self):
        return self._species

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = max(1, min(100, value))
        self._update_stats()

    @property
    def hp(self):
        return self._hp

    @property
    def current_hp(self):
        return self._current_hp

    @current_hp.setter
    def current_hp(self, value):
        self._current_hp = max(0, min(self._hp, value))

    @property
    def defense(self):
        return self._defense

    @property
    def attack(self):
        return self._attack

    @property
    def speed(self):
        return self._speed

    @property
    def types(self):
        return self._types

    @property
    def moves(self):
        move_list = []

        for move in self._moves:
            move_list.append(
                f"{move['name']} | "
                f"Type: {move['type']} | "
                f"Power: {move['power']} | "
                f"Accuracy: {move['accuracy']}"
            )

        return "\n".join(move_list)

    @property
    def moves_list(self):
        return self._moves

    def get_move(self, move_name):
        for move in self._moves:
            if move["name"] == move_name:
                return move
        return None

    def attack_damage(self, move_name, target, level=100):
        move = self.get_move(move_name)
        if not move:
            print(f"{self._name} doesn't know {move_name}")
            return 0

        if target.dodge(move["accuracy"], level):
            print(f"{self._name}'s {move_name} missed!")
            return 0

        move = cast(dict, move)
        base_damage = (move["power"] * self._attack) / target.defense
        stab = 1.5 if move["type"] in self._types else 1.0
        effectiveness = self._calculate_type_effectiveness(move["type"], target.types)
        random_factor = random.randint(85, 100) / 100
        damage = int(base_damage * stab * effectiveness * random_factor)
        damage = math.floor(damage)

        self._show_effectiveness_message(move["type"], target.types, effectiveness)
        print(f"{target.name} took {damage} damage!")
        target.take_damage(damage)

        return damage

    @staticmethod
    def _calculate_type_effectiveness(attack_type, target_types):
        effectiveness = 1.0

        for target_type in target_types:
            effectiveness *= type_matchup.TYPE_EFFECTIVENESS[attack_type][target_type]

        return effectiveness

    @staticmethod
    def _show_effectiveness_message(attack_type, target_types, effectiveness):
        if effectiveness > 1.5:
            print(f"{attack_type} is super effective! (x{effectiveness})")
        elif effectiveness > 1.0:
            print(f"{attack_type} is effective! (x{effectiveness})")
        elif effectiveness < 0.5:
            print(f"{attack_type} is not very effective... (x{effectiveness})")
        elif effectiveness < 1.0:
            print(f"{attack_type} is not very effective... (x{effectiveness})")
        elif effectiveness == 0:
            print(f"{attack_type} doesn't affect {target_types}...")

    def take_damage(self, damage):
        self._current_hp -= damage
        if self._current_hp <= 0:
            self._current_hp = 0
            print(f"{self._name} fainted!")
            return True

        self._current_hp = math.floor(self._current_hp)
        print(f"{self._name} has {self._current_hp} HP remaining")
        return False

    def dodge(self, accuracy, level=100):
        dodge = (100 - accuracy) + (self._speed / 50) + (self._level - level) * 0.5
        if random.randint(1, 100) <= dodge:
            print(f"{self._name} dodged the attack!")
            return True
        return False

    def _recovery_hp(self, life):
        self._current_hp += life
        if self._current_hp > self._hp:
            self._current_hp = self._hp


class WildPokemon(Pokemon):
    def __init__(self, pokemon, name="", level=1, iv=0.1):
        super().__init__(pokemon, name, level, iv)


class PlayerPokemon(Pokemon):
    def __init__(self, pokemon, name="", level=1, iv=0.1):
        super().__init__(pokemon, name, level, iv)

        self._experience = 0
        self._xp_to_next_level = 100
        self._evolves_to = self._data["evolves_to"]
        self._evolution_level = self._data["evolution_level"]

    def evolve(self):
        print(f"{self._name} evolves to {self._evolves_to}")

        self._data = pokemons_data.POKEMONS[self._evolves_to]

        self._species = self._data["species"]
        self._types = self._data["types"]

        self._update_stats()

        self._evolves_to = self._data["evolves_to"]
        self._evolution_level = self._data["evolution_level"]

    @property
    def experience(self):
        return self._experience

    @property
    def evolves_to(self):
        return self._evolves_to

    def level_up(self, level):
        self.level += level

    def get_total_experience(self):
        total_xp = self._experience

        for level in range(1, self._level):
            total_xp += level * 100

        return total_xp

    def show_experience_gain(self, experience):
        max_xp = 495000
        total_experience = self.get_total_experience()

        if total_experience + experience >= max_xp:
            print(f"{self._name} gained {max_xp - total_experience} experience")
        else:
            print(f"{self._name} gained {experience} experience")

    def gain_experience(self, experience):
        if self._level < 100:
            partial_level = 0

            self.show_experience_gain(experience)
            self._experience += experience

            if self._experience >= 100:
                print("Level up!")

                while self._experience >= self._xp_to_next_level:
                    self._experience -= self._xp_to_next_level
                    partial_level += 1
                    self._xp_to_next_level += 100

                    if partial_level + self._level >= 100:
                        break

                self.level_up(partial_level)

                print(
                    f"{self._name} has just reached Level {self._level}"
                )

                if self._level >= self._evolution_level:
                    while (
                            self._evolution_level
                            and self._level >= self._evolution_level
                    ):
                        self.evolve()