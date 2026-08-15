POKEMONS = {
    # =========================
    # GRASS
    # =========================
    "Bulbasaur": {
        "species": "Bulbasaur",
        "types": ["Grass"],
        "hp": 45,
        "attack": 49,
        "defense": 49,
        "speed": 45,
        "experience": 0,
        "xp_to_next_level": 100,
        "evolves_to": "Ivysaur",
        "evolution_level": 16,
        "wild_level_range": [1, 15],
        "moves": ["Tackle", "Vine Whip"]
    },
    "Ivysaur": {
        "species": "Ivysaur",
        "types": ["Grass"],
        "hp": 60,
        "attack": 62,
        "defense": 63,
        "speed": 60,
        "experience": 0,
        "xp_to_next_level": 200,
        "evolves_to": "Venusaur",
        "evolution_level": 32,
        "wild_level_range": [16, 31],
        "moves": ["Vine Whip", "Razor Leaf", "Leech Seed"]
    },
    "Venusaur": {
        "species": "Venusaur",
        "types": ["Grass"],
        "hp": 82,
        "attack": 82,
        "defense": 83,
        "speed": 80,
        "experience": 0,
        "xp_to_next_level": None,
        "evolves_to": None,
        "evolution_level": None,
        "wild_level_range": [32, 100],
        "moves": ["Razor Leaf", "Solar Beam", "Leech Seed"]
    },

    # =========================
    # FIRE
    # =========================
    "Charmander": {
        "species": "Charmander",
        "types": ["Fire"],
        "hp": 39,
        "attack": 52,
        "defense": 43,
        "speed": 65,
        "experience": 0,
        "xp_to_next_level": 100,
        "evolves_to": "Charmeleon",
        "evolution_level": 16,
        "wild_level_range": [1, 15],
        "moves": ["Scratch", "Ember"]
    },
    "Charmeleon": {
        "species": "Charmeleon",
        "types": ["Fire"],
        "hp": 58,
        "attack": 64,
        "defense": 58,
        "speed": 80,
        "experience": 0,
        "xp_to_next_level": 200,
        "evolves_to": "Charizard",
        "evolution_level": 36,
        "wild_level_range": [16, 35],
        "moves": ["Ember", "Metal Claw", "Flamethrower"]
    },
    "Charizard": {
        "species": "Charizard",
        "types": ["Fire", "Flying"],
        "hp": 78,
        "attack": 84,
        "defense": 78,
        "speed": 100,
        "experience": 0,
        "xp_to_next_level": None,
        "evolves_to": None,
        "evolution_level": None,
        "wild_level_range": [36, 100],
        "moves": ["Flamethrower", "Fire Blast", "Wing Attack"]
    },

    # =========================
    # WATER
    # =========================
    "Squirtle": {
        "species": "Squirtle",
        "types": ["Water"],
        "hp": 44,
        "attack": 48,
        "defense": 65,
        "speed": 43,
        "experience": 0,
        "xp_to_next_level": 100,
        "evolves_to": "Wartortle",
        "evolution_level": 16,
        "wild_level_range": [1, 15],
        "moves": ["Tackle", "Water Gun"]
    },
    "Wartortle": {
        "species": "Wartortle",
        "types": ["Water"],
        "hp": 59,
        "attack": 63,
        "defense": 80,
        "speed": 58,
        "experience": 0,
        "xp_to_next_level": 200,
        "evolves_to": "Blastoise",
        "evolution_level": 36,
        "wild_level_range": [16, 35],
        "moves": ["Water Gun", "Bubble", "Bite"]
    },
    "Blastoise": {
        "species": "Blastoise",
        "types": ["Water"],
        "hp": 79,
        "attack": 83,
        "defense": 100,
        "speed": 78,
        "experience": 0,
        "xp_to_next_level": None,
        "evolves_to": None,
        "evolution_level": None,
        "wild_level_range": [36, 100],
        "moves": ["Hydro Pump", "Surf", "Bite"]
    },

    # =========================
    # ELECTRIC
    # =========================
    "Pikachu": {
        "species": "Pikachu",
        "types": ["Electric"],
        "hp": 35,
        "attack": 55,
        "defense": 40,
        "speed": 90,
        "experience": 0,
        "xp_to_next_level": 100,
        "evolves_to": "Raichu",
        "evolution_level": 30,
        "wild_level_range": [1, 29],
        "moves": ["Thunder Shock", "Quick Attack"]
    },
    "Magnemite": {
        "species": "Magnemite",
        "types": ["Electric"],
        "hp": 40,
        "attack": 35,
        "defense": 70,
        "speed": 45,
        "experience": 0,
        "xp_to_next_level": 100,
        "evolves_to": "Magneton",
        "evolution_level": 30,
        "wild_level_range": [1, 29],
        "moves": ["Thunder Shock", "Spark"]
    },
    "Voltorb": {
        "species": "Voltorb",
        "types": ["Electric"],
        "hp": 40,
        "attack": 30,
        "defense": 50,
        "speed": 100,
        "experience": 0,
        "xp_to_next_level": 100,
        "evolves_to": "Electrode",
        "evolution_level": 30,
        "wild_level_range": [1, 29],
        "moves": ["Spark", "Swift"]
    },

    # =========================
    # FLYING
    # =========================
    "Pidgey": {
        "species": "Pidgey",
        "types": ["Flying"],
        "hp": 40,
        "attack": 45,
        "defense": 40,
        "speed": 56,
        "experience": 0,
        "xp_to_next_level": 100,
        "evolves_to": "Pidgeotto",
        "evolution_level": 18,
        "wild_level_range": [1, 17],
        "moves": ["Tackle", "Gust"]
    },
    "Spearow": {
        "species": "Spearow",
        "types": ["Flying"],
        "hp": 40,
        "attack": 60,
        "defense": 30,
        "speed": 70,
        "experience": 0,
        "xp_to_next_level": 100,
        "evolves_to": "Fearow",
        "evolution_level": 20,
        "wild_level_range": [1, 19],
        "moves": ["Peck", "Fury Attack"]
    },
    "Zubat": {
        "species": "Zubat",
        "types": ["Flying"],
        "hp": 40,
        "attack": 45,
        "defense": 35,
        "speed": 55,
        "experience": 0,
        "xp_to_next_level": 100,
        "evolves_to": "Golbat",
        "evolution_level": 22,
        "wild_level_range": [1, 21],
        "moves": ["Bite", "Wing Attack"]
    },

    # =========================
    # ROCK
    # =========================
    "Geodude": {
        "species": "Geodude",
        "types": ["Rock", "Ground"],
        "hp": 40,
        "attack": 80,
        "defense": 100,
        "speed": 20,
        "experience": 0,
        "xp_to_next_level": 100,
        "evolves_to": "Graveler",
        "evolution_level": 25,
        "wild_level_range": [1, 24],
        "moves": ["Rock Throw", "Tackle"]
    },
    "Onix": {
        "species": "Onix",
        "types": ["Rock", "Ground"],
        "hp": 35,
        "attack": 45,
        "defense": 160,
        "speed": 70,
        "experience": 0,
        "xp_to_next_level": None,
        "evolves_to": None,
        "evolution_level": None,
        "wild_level_range": [1, 100],
        "moves": ["Rock Throw", "Bind"]
    },
    "Rhyhorn": {
        "species": "Rhyhorn",
        "types": ["Rock", "Ground"],
        "hp": 80,
        "attack": 85,
        "defense": 95,
        "speed": 25,
        "experience": 0,
        "xp_to_next_level": 100,
        "evolves_to": "Rhydon",
        "evolution_level": 42,
        "wild_level_range": [1, 41],
        "moves": ["Horn Attack", "Rock Blast"]
    },

    # =========================
    # GROUND
    # =========================
    "Sandshrew": {
        "species": "Sandshrew",
        "types": ["Ground"],
        "hp": 50,
        "attack": 75,
        "defense": 85,
        "speed": 40,
        "experience": 0,
        "xp_to_next_level": 100,
        "evolves_to": "Sandslash",
        "evolution_level": 22,
        "wild_level_range": [1, 21],
        "moves": ["Scratch", "Sand Attack"]
    },
    "Diglett": {
        "species": "Diglett",
        "types": ["Ground"],
        "hp": 10,
        "attack": 55,
        "defense": 25,
        "speed": 95,
        "experience": 0,
        "xp_to_next_level": 100,
        "evolves_to": "Dugtrio",
        "evolution_level": 26,
        "wild_level_range": [1, 25],
        "moves": ["Scratch", "Dig"]
    },
    "Cubone": {
        "species": "Cubone",
        "types": ["Ground"],
        "hp": 50,
        "attack": 50,
        "defense": 95,
        "speed": 35,
        "experience": 0,
        "xp_to_next_level": 100,
        "evolves_to": "Marowak",
        "evolution_level": 28,
        "wild_level_range": [1, 27],
        "moves": ["Bone Club", "Headbutt"]
    },

    # =========================
    # FIGHTING
    # =========================
    "Machop": {
        "species": "Machop",
        "types": ["Fighting"],
        "hp": 70,
        "attack": 80,
        "defense": 50,
        "speed": 35,
        "experience": 0,
        "xp_to_next_level": 100,
        "evolves_to": "Machoke",
        "evolution_level": 28,
        "wild_level_range": [1, 27],
        "moves": ["Karate Chop", "Low Kick"]
    },
    "Mankey": {
        "species": "Mankey",
        "types": ["Fighting"],
        "hp": 40,
        "attack": 80,
        "defense": 35,
        "speed": 70,
        "experience": 0,
        "xp_to_next_level": 100,
        "evolves_to": "Primeape",
        "evolution_level": 28,
        "wild_level_range": [1, 27],
        "moves": ["Scratch", "Low Kick"]
    },
    "Hitmonlee": {
        "species": "Hitmonlee",
        "types": ["Fighting"],
        "hp": 50,
        "attack": 120,
        "defense": 55,
        "speed": 87,
        "experience": 0,
        "xp_to_next_level": None,
        "evolves_to": None,
        "evolution_level": None,
        "wild_level_range": [1, 100],
        "moves": ["Rolling Kick", "High Jump Kick", "Mega Kick"]
    },

    # =========================
    # GHOST
    # =========================
    "Gastly": {
        "species": "Gastly",
        "types": ["Ghost"],
        "hp": 30,
        "attack": 35,
        "defense": 30,
        "speed": 80,
        "experience": 0,
        "xp_to_next_level": 100,
        "evolves_to": "Haunter",
        "evolution_level": 25,
        "wild_level_range": [1, 24],
        "moves": ["Lick", "Night Shade"]
    },
    "Haunter": {
        "species": "Haunter",
        "types": ["Ghost"],
        "hp": 45,
        "attack": 50,
        "defense": 45,
        "speed": 95,
        "experience": 0,
        "xp_to_next_level": 200,
        "evolves_to": "Gengar",
        "evolution_level": 40,
        "wild_level_range": [25, 39],
        "moves": ["Shadow Punch", "Night Shade", "Shadow Ball"]
    },
    "Gengar": {
        "species": "Gengar",
        "types": ["Ghost"],
        "hp": 60,
        "attack": 65,
        "defense": 60,
        "speed": 110,
        "experience": 0,
        "xp_to_next_level": None,
        "evolves_to": None,
        "evolution_level": None,
        "wild_level_range": [40, 100],
        "moves": ["Shadow Ball", "Dream Eater", "Dark Pulse"]
    },

    # =========================
    # NORMAL
    # =========================
    "Eevee": {
        "species": "Eevee",
        "types": ["Normal"],
        "hp": 55,
        "attack": 55,
        "defense": 50,
        "speed": 55,
        "experience": 0,
        "xp_to_next_level": 100,
        "evolves_to": None,
        "evolution_level": None,
        "wild_level_range": [1, 100],
        "moves": ["Tackle", "Quick Attack"]
    },
    "Meowth": {
        "species": "Meowth",
        "types": ["Normal"],
        "hp": 40,
        "attack": 45,
        "defense": 35,
        "speed": 90,
        "experience": 0,
        "xp_to_next_level": 100,
        "evolves_to": "Persian",
        "evolution_level": 28,
        "wild_level_range": [1, 27],
        "moves": ["Scratch", "Bite"]
    },
    "Snorlax": {
        "species": "Snorlax",
        "types": ["Normal"],
        "hp": 160,
        "attack": 110,
        "defense": 65,
        "speed": 30,
        "experience": 0,
        "xp_to_next_level": None,
        "evolves_to": None,
        "evolution_level": None,
        "wild_level_range": [1, 100],
        "moves": ["Body Slam", "Headbutt", "Rest"]
    }
}