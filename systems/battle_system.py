import random
import time

from systems.capture_system import CaptureSystem


class BattleSystem:
    def __init__(self, player_pokemon, wild_pokemon, trainer=None):
        self.player = player_pokemon
        self.wild = wild_pokemon
        self.trainer = trainer
        self.battle_log = []
        self.caught = False

    def start_battle(self):
        print(f"A wild {self.wild.species} appeared!")
        print(f"Go! {self.player.name}!")
        self.battle_loop()

    def battle_loop(self):
        while self.wild.current_hp > 0 and self.player.current_hp > 0 and not self.caught:
            if self.player.speed > self.wild.speed:
                self.player_turn()
                if self.wild.current_hp <= 0 or self.caught:
                    break
                self.wild_turn()
            else:
                self.wild_turn()
                if self.player.current_hp <= 0:
                    break
                if self.caught:
                    break
                self.player_turn()
            time.sleep(0.5)

        self.end_battle()

    def player_turn(self):
        print("\n--- Your Turn ---")
        print(f"{self.player.name} (HP: {self.player.current_hp}/{self.player.hp})")
        print(f"{self.wild.species} (HP: {self.wild.current_hp}/{self.wild.hp})")
        print("\n1. Attack")
        print("2. Use Poké Ball")
        print("3. Run")

        choice = input("Choose an action: ").strip()

        if choice == "1":
            self.player_attack()
        elif choice == "2":
            self.try_capture()
        elif choice == "3":
            self.try_run()
        else:
            print("Invalid choice! Try again.")
            self.player_turn()

    def player_attack(self):
        print("\nAvailable moves:")
        for i, move in enumerate(self.player.moves_list, 1):
            print(f"{i}. {move['name']} (Power: {move['power']}, Accuracy: {move['accuracy']}%)")

        try:
            choice = int(input("Choose a move: ")) - 1
            if 0 <= choice < len(self.player.moves_list):
                move = self.player.moves_list[choice]
                self.player.attack_damage(move["name"], self.wild)
            else:
                print("Invalid move!")
                self.player_attack()
        except ValueError:
            print("Please enter a number!")
            self.player_attack()

    def wild_turn(self):
        print("\n--- Wild Pokémon's Turn ---")
        if self.wild.moves_list:
            move = random.choice(self.wild.moves_list)
            print(f"{self.wild.species} used {move['name']}!")
            self.wild.attack_damage(move["name"], self.player)

    def try_capture(self):
        if not self.trainer:
            print("No trainer available to use items!")
            return False

        # Show available Poké Balls
        pokeball_list = list(self.trainer.pokeballs.keys())
        if not pokeball_list:
            print("You don't have any Poké Balls!")
            return False

        print("\nAvailable Poké Balls:")
        ball_options = {}
        counter = 1
        for ball_name, amount in self.trainer.pokeballs.items():
            if amount > 0:
                print(f"{counter}. {ball_name} (x{amount})")
                ball_options[str(counter)] = ball_name
                counter += 1

        print(f"{counter}. Cancel")

        choice = input("Choose a ball: ").strip()

        if choice == str(counter):
            print("Canceled.")
            return False

        if choice in ball_options:
            pokeball_name = ball_options[choice]
            amount = self.trainer.get_pokeball_count(pokeball_name)

            if amount <= 0:
                print(f"You don't have any {pokeball_name}s!")
                return False

            # Get capture rate for the Poké Ball
            capture_rate = 1.0
            if pokeball_name == "Poké Ball":
                capture_rate = 1.0
            elif pokeball_name == "Great Ball":
                capture_rate = 1.5
            elif pokeball_name == "Ultra Ball":
                capture_rate = 2.0
            elif pokeball_name == "Master Ball":
                capture_rate = 255

            pokeball = {"name": pokeball_name, "capture_rate": capture_rate}

            # Use the Poké Ball
            self.trainer.remove_pokeball(pokeball_name)

            success, message = CaptureSystem.attempt_capture(self.wild, pokeball)
            print(message)

            if success:
                print(f"Congratulations! You caught {self.wild.species}!")
                if self.trainer:
                    self.trainer.add_pokemon(self.wild)
                    self.trainer.add_pokedex(self.wild.species)
                self.caught = True
                return True
            else:
                print(f"The {self.wild.species} is still fighting!")
                return False
        else:
            print("Invalid choice!")
            return False

    def try_run(self):
        escape_chance = (self.player.speed / (self.wild.speed + 10)) * 0.5
        if random.random() < escape_chance:
            print("You fled successfully!")
            return True
        else:
            print("You couldn't escape!")
            return False

    def end_battle(self):
        if self.caught:
            print(f"\nYou successfully caught {self.wild.species}!")
        elif self.wild.current_hp <= 0:
            print(f"\nWild {self.wild.species} fainted!")
            exp_gain = self.wild.level * 50
            self.player.gain_experience(exp_gain)
            print(f"You gained {exp_gain} experience points!")
        elif self.player.current_hp <= 0:
            print(f"\n{self.player.name} fainted!")
            print("You lost the battle...")