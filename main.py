import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.pokemons import PlayerPokemon
from systems.battle_system import BattleSystem
from systems.pokemon_generator import pokemon_create
from models.trainer import Trainer


def main():
    print("=== Pokémon Game ===\n")
    name = input("Enter your name: ")
    trainer = Trainer(name)

    # Give initial items
    trainer.add_pokeball("Poké Ball", 10)
    trainer.add_pokeball("Great Ball", 5)
    trainer.add_pokeball("Ultra Ball", 3)
    trainer.add_pokeball("Master Ball", 1)
    trainer.add_gold(1000)

    # Choose starter Pokémon
    print("\nChoose your starter Pokémon:")
    print("1. Charmander (Fire)")
    print("2. Bulbasaur (Grass)")
    print("3. Squirtle (Water)")

    choice = input("Choose: ").strip()

    starters = {
        "1": "Charmander",
        "2": "Bulbasaur",
        "3": "Squirtle"
    }

    if choice in starters:
        starter_name = starters[choice]
        starter = PlayerPokemon(starter_name, level=5, iv=0.2)
        trainer.add_pokemon(starter)
        trainer.add_pokedex(starter.species)
        print(f"\n{starter.name} is your starter Pokémon!")
    else:
        print("Invalid choice!")
        return

    # Main game loop
    while True:
        print("\n" + "=" * 50)
        print(f"Trainer: {trainer.name} (Level {trainer.level})")
        print(f"Gold: {trainer.gold}")
        print(f"Pokémon: {len(trainer.pokemons)}")
        print("=" * 50)

        print("\nWhat would you like to do?")
        print("1. Battle a wild Pokémon")
        print("2. Show team")
        print("3. Show items")
        print("4. Quit")

        action = input("Choose: ").strip()

        if action == "1":
            wild_pokemon = pokemon_create(trainer)

            if wild_pokemon is None:
                print("No wild Pokémon available for your level!")
                continue

            print(f"\nA wild {wild_pokemon.species} (Level {wild_pokemon.level}) appeared!")

            print("\nChoose your Pokémon:")
            for i, pokemon in enumerate(trainer.pokemons, 1):
                if pokemon.current_hp > 0:
                    print(f"{i}. {pokemon.name} (Level {pokemon.level}) - HP: {pokemon.current_hp}/{pokemon.hp}")
                else:
                    print(f"{i}. {pokemon.name} (Level {pokemon.level}) - FAINTED")

            choice = input("Choose: ").strip()

            try:
                idx = int(choice) - 1
                if 0 <= idx < len(trainer.pokemons):
                    player_pokemon = trainer.pokemons[idx]
                    if player_pokemon.current_hp <= 0:
                        print("This Pokémon has fainted! Choose another one.")
                        continue

                    battle = BattleSystem(player_pokemon, wild_pokemon, trainer)
                    battle.start_battle()

                    if battle.caught:
                        print(f"{wild_pokemon.species} was added to your team!")
                    elif wild_pokemon.current_hp <= 0:
                        trainer.gain_experience(wild_pokemon.level * 20)
                        trainer.add_gold(wild_pokemon.level * 10)
                    elif wild_pokemon.current_hp > 0 and wild_pokemon not in trainer.pokemons:
                        print("The wild Pokémon escaped!")
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Please enter a number!")

        elif action == "2":
            print("\n=== Your Team ===")
            if not trainer.pokemons:
                print("You don't have any Pokémon!")
            else:
                for pokemon in trainer.pokemons:
                    status = "Fainted" if pokemon.current_hp <= 0 else f"HP: {pokemon.current_hp}/{pokemon.hp}"
                    print(f"{pokemon.name} (Lv.{pokemon.level}) - {status}")

        elif action == "3":
            print("\n=== Your Items ===")
            print("\n--- Poké Balls ---")
            if trainer.pokeballs:
                for ball, amount in trainer.pokeballs.items():
                    print(f"{ball}: {amount}")
            else:
                print("No Poké Balls")

            print("\n--- Other Items ---")
            if trainer.items:
                for item, amount in trainer.items.items():
                    print(f"{item}: {amount}")
            else:
                print("No items")

            print(f"\nGold: {trainer.gold}")

        elif action == "4":
            print("\nThanks for playing!")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()