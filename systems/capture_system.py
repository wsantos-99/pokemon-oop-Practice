import random


class CaptureSystem:
    @staticmethod
    def calculate_catch_rate(pokemon, pokeball):
        level_penalty = max(0, (pokemon.level - 50) * 0.01)
        capture_bonus = pokeball.get("capture_rate", 1.0)
        catch_rate = capture_bonus * (1 - level_penalty)
        return min(0.95, max(0.01, catch_rate))

    @staticmethod
    def attempt_capture(pokemon, pokeball):
        if pokeball.get("name") == "Master Ball":
            return True, "The Master Ball captures the Pokémon without fail!"

        catch_rate = CaptureSystem.calculate_catch_rate(pokemon, pokeball)
        random_roll = random.random()
        variation = random.uniform(0.85, 1.15)
        final_chance = catch_rate * variation

        if final_chance >= 1.0:
            return True, "The Pokémon was caught! It's a perfect throw!"
        elif random_roll <= final_chance:
            return True, "The Pokémon was caught successfully!"
        else:
            if random_roll < final_chance * 0.5:
                return False, "The Pokémon almost escaped! But it broke free..."
            else:
                return False, "The Pokémon broke free!"