import random
import data.pokemons_data as pokemons_data
from models.pokemon import WildPokemon


def get_pokemons_by_level(level):
    available_species = []

    for species, data in pokemons_data.POKEMONS.items():
        min_level, max_level = data["wild_level_range"]

        if min_level <= level <= max_level:
            available_species.append(species)

    return available_species


def pokemon_create(trainer):
    level = random.randint(
        max(1, trainer.level - 3),
        min(100, trainer.level + 2)
    )

    available_species = get_pokemons_by_level(level)

    if not available_species:
        return None

    species = random.choice(available_species)

    iv = round(random.uniform(0.1, 0.4), 2)

    return WildPokemon(
        species,
        level=level,
        iv=iv
    )