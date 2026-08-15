class Trainer:
    def __init__(self, name):
        self._name = name
        self._level = 1
        self._xp = 0

        self._pokemons = []
        self._pokedex = []
        self._pokeballs = {}
        self._items = {}
        self._badges = []

        self._gold = 0

    # ---------- Properties ----------
    @property
    def name(self):
        return self._name

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = max(1, min(100, value))

    @property
    def gold(self):
        return self._gold

    @property
    def pokemons(self):
        return self._pokemons

    @property
    def pokedex(self):
        return self._pokedex

    @property
    def pokeballs(self):
        return self._pokeballs

    @property
    def items(self):
        return self._items

    @property
    def badges(self):
        return self._badges

    # ---------- Trainer ----------
    def level_up(self, level):
        self.level += level

    def gain_experience(self, experience):
        print(f"You gained {experience} experience.")

        partial_level = 0
        self._xp += experience

        while self._xp >= 100:
            self._xp -= 100
            partial_level += 1

        if partial_level:
            print("Level Up!")
            self.level_up(partial_level)
            print(f"You have just reached Level {self.level}")

    # ---------- Pokémon ----------
    def add_pokedex(self, pokemon):
        if pokemon not in self._pokedex:
            self._pokedex.append(pokemon)
            print(f"{pokemon} was added to your Pokédex.")

    def add_pokemon(self, pokemon):
        self._pokemons.append(pokemon)
        print(f"{pokemon} joined your team.")

    def remove_pokemon(self, pokemon):
        if pokemon in self._pokemons:
            self._pokemons.remove(pokemon)
            print(f"{pokemon} was removed from your team.")

    def show_pokemons(self):
        for pokemon in self._pokemons:
            print(pokemon)

    def show_pokedex(self):
        for pokemon in self._pokedex:
            print(pokemon)

    # ---------- Items ----------
    def add_item(self, item, amount):
        if item in self._items:
            self._items[item] += amount
        else:
            self._items[item] = amount

        print(f"You received {amount} {item}.")

    def remove_item(self, item):
        if item in self._items:
            self._items[item] -= 1

            if self._items[item] <= 0:
                del self._items[item]

            print(f"You used 1 {item}.")

    def show_items(self):
        for item, amount in self._items.items():
            print(item, amount)

    # ---------- Pokéballs ----------
    def add_pokeball(self, pokeball, amount):
        if pokeball in self._pokeballs:
            self._pokeballs[pokeball] += amount
        else:
            self._pokeballs[pokeball] = amount

        print(f"You received {amount} {pokeball}.")

    def remove_pokeball(self, pokeball):
        if pokeball in self._pokeballs:
            self._pokeballs[pokeball] -= 1

            if self._pokeballs[pokeball] <= 0:
                del self._pokeballs[pokeball]

            print(f"You used 1 {pokeball}.")

    def show_pokeballs(self):
        for pokeball, amount in self._pokeballs.items():
            print(f"{pokeball}: {amount}")

    def get_pokeball_count(self, pokeball):
        return self._pokeballs.get(pokeball, 0)

    # ---------- Badges ----------
    def add_badge(self, badge):
        self._badges.append(badge)
        print(f"You earned the Badge: {badge}")

    def count_badges(self):
        return len(self._badges)

    def show_badges(self):
        print(f"Badges: {self.count_badges()}")

        for badge in self._badges:
            print(badge)

    # ---------- Gold ----------
    def add_gold(self, gold):
        self._gold += gold
        print(f"You received {gold} gold.")

    def remove_gold(self, gold):
        self._gold -= gold
        print(f"You lost {gold} gold.")

    def show_gold(self):
        print(f"Gold: {self.gold}")