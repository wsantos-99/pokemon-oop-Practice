MOVES = {
    # =========================
    # NORMAL MOVES
    # =========================
    "Tackle": {
        "type": "Normal",
        "category": "Physical",
        "power": 40,
        "accuracy": 100,
        "description": "A physical attack with no special effects."
    },
    "Scratch": {
        "type": "Normal",
        "category": "Physical",
        "power": 40,
        "accuracy": 100,
        "description": "Scratches the target with sharp claws."
    },
    "Quick Attack": {
        "type": "Normal",
        "category": "Physical",
        "power": 40,
        "accuracy": 100,
        "priority": 1,
        "description": "An extremely fast attack that always strikes first."
    },
    "Bite": {
        "type": "Normal",
        "category": "Physical",
        "power": 60,
        "accuracy": 100,
        "flinch_chance": 0.3,
        "description": "Bites the target. May cause flinching."
    },
    "Body Slam": {
        "type": "Normal",
        "category": "Physical",
        "power": 85,
        "accuracy": 100,
        "paralysis_chance": 0.3,
        "description": "Drops onto the target. May cause paralysis."
    },
    "Headbutt": {
        "type": "Normal",
        "category": "Physical",
        "power": 70,
        "accuracy": 100,
        "flinch_chance": 0.3,
        "description": "Hits the target with a hard head. May cause flinching."
    },
    "Horn Attack": {
        "type": "Normal",
        "category": "Physical",
        "power": 65,
        "accuracy": 100,
        "description": "Attacks with a sharp horn."
    },
    "Fury Attack": {
        "type": "Normal",
        "category": "Physical",
        "power": 15,
        "accuracy": 85,
        "hits": [2, 5],
        "description": "Strikes 2-5 times in a row."
    },
    "Mega Kick": {
        "type": "Normal",
        "category": "Physical",
        "power": 120,
        "accuracy": 75,
        "description": "A powerful kicking attack."
    },
    "Swift": {
        "type": "Normal",
        "category": "Special",
        "power": 60,
        "accuracy": 100,
        "always_hits": True,
        "description": "Never misses."
    },
    "Rest": {
        "type": "Normal",
        "category": "Status",
        "power": 0,
        "accuracy": 100,
        "heal": "MAX",
        "status": "Sleep",
        "status_duration": 2,
        "description": "Restores full HP and induces sleep for 2 turns."
    },
    "Bind": {
        "type": "Normal",
        "category": "Physical",
        "power": 15,
        "accuracy": 85,
        "trapping": True,
        "trapping_duration": [2, 5],
        "description": "Traps the target for 2-5 turns."
    },

    # =========================
    # GRASS MOVES
    # =========================
    "Vine Whip": {
        "type": "Grass",
        "category": "Physical",
        "power": 45,
        "accuracy": 100,
        "description": "Whips the target with vines."
    },
    "Razor Leaf": {
        "type": "Grass",
        "category": "Physical",
        "power": 55,
        "accuracy": 95,
        "critical_ratio": 0.125,
        "description": "Has a high critical-hit ratio."
    },
    "Leech Seed": {
        "type": "Grass",
        "category": "Status",
        "power": 0,
        "accuracy": 90,
        "leech": True,
        "leech_fraction": 0.125,
        "description": "Plants a seed that drains HP each turn."
    },
    "Solar Beam": {
        "type": "Grass",
        "category": "Special",
        "power": 120,
        "accuracy": 100,
        "requires_charge": True,
        "description": "Charges on first turn, attacks on second."
    },

    # =========================
    # FIRE MOVES
    # =========================
    "Ember": {
        "type": "Fire",
        "category": "Special",
        "power": 40,
        "accuracy": 100,
        "burn_chance": 0.1,
        "description": "A small flame attack. May cause burn."
    },
    "Flamethrower": {
        "type": "Fire",
        "category": "Special",
        "power": 90,
        "accuracy": 100,
        "burn_chance": 0.1,
        "description": "Powerful flame attack. May cause burn."
    },
    "Fire Blast": {
        "type": "Fire",
        "category": "Special",
        "power": 110,
        "accuracy": 85,
        "burn_chance": 0.1,
        "description": "Intense blast of fire. May cause burn."
    },
    "Metal Claw": {
        "type": "Steel",
        "category": "Physical",
        "power": 50,
        "accuracy": 95,
        "attack_boost_chance": 0.1,
        "description": "Claws with metallic power. May raise Attack."
    },

    # =========================
    # WATER MOVES
    # =========================
    "Water Gun": {
        "type": "Water",
        "category": "Special",
        "power": 40,
        "accuracy": 100,
        "description": "Shoots water at the target."
    },
    "Bubble": {
        "type": "Water",
        "category": "Special",
        "power": 40,
        "accuracy": 100,
        "speed_reduction_chance": 0.1,
        "description": "Bubbles that may reduce target's Speed."
    },
    "Hydro Pump": {
        "type": "Water",
        "category": "Special",
        "power": 110,
        "accuracy": 80,
        "description": "A powerful water jet attack."
    },
    "Surf": {
        "type": "Water",
        "category": "Special",
        "power": 90,
        "accuracy": 100,
        "description": "Hits both opponents in double battles."
    },

    # =========================
    # ELECTRIC MOVES
    # =========================
    "Thunder Shock": {
        "type": "Electric",
        "category": "Special",
        "power": 40,
        "accuracy": 100,
        "paralysis_chance": 0.1,
        "description": "Electric shock. May cause paralysis."
    },
    "Spark": {
        "type": "Electric",
        "category": "Physical",
        "power": 65,
        "accuracy": 100,
        "paralysis_chance": 0.3,
        "description": "Electric attack. May cause paralysis."
    },

    # =========================
    # FLYING MOVES
    # =========================
    "Gust": {
        "type": "Flying",
        "category": "Special",
        "power": 40,
        "accuracy": 100,
        "description": "Whips up a strong gust of wind."
    },
    "Wing Attack": {
        "type": "Flying",
        "category": "Physical",
        "power": 60,
        "accuracy": 100,
        "description": "Strikes with sharp wings."
    },
    "Peck": {
        "type": "Flying",
        "category": "Physical",
        "power": 35,
        "accuracy": 100,
        "description": "Pecks the target with beak."
    },

    # =========================
    # ROCK / GROUND MOVES
    # =========================
    "Rock Throw": {
        "type": "Rock",
        "category": "Physical",
        "power": 50,
        "accuracy": 90,
        "description": "Throws a rock at the target."
    },
    "Rock Blast": {
        "type": "Rock",
        "category": "Physical",
        "power": 25,
        "accuracy": 90,
        "hits": [2, 5],
        "description": "Hurls 2-5 rocks in succession."
    },
    "Dig": {
        "type": "Ground",
        "category": "Physical",
        "power": 80,
        "accuracy": 100,
        "requires_charge": True,
        "description": "Digs underground on first turn, attacks on second."
    },
    "Sand Attack": {
        "type": "Ground",
        "category": "Status",
        "power": 0,
        "accuracy": 100,
        "accuracy_reduction": 1,
        "description": "Lowers target's Accuracy."
    },

    # =========================
    # FIGHTING MOVES
    # =========================
    "Karate Chop": {
        "type": "Fighting",
        "category": "Physical",
        "power": 50,
        "accuracy": 100,
        "critical_ratio": 0.125,
        "description": "A chopping attack with high critical-hit ratio."
    },
    "Low Kick": {
        "type": "Fighting",
        "category": "Physical",
        "power": 50,
        "accuracy": 100,
        "weight_based": True,
        "description": "Damage depends on target's weight."
    },
    "Rolling Kick": {
        "type": "Fighting",
        "category": "Physical",
        "power": 60,
        "accuracy": 85,
        "flinch_chance": 0.3,
        "description": "A spinning kick. May cause flinching."
    },
    "High Jump Kick": {
        "type": "Fighting",
        "category": "Physical",
        "power": 130,
        "accuracy": 90,
        "recoil_on_miss": True,
        "description": "A powerful jump kick. Hurts user if it misses."
    },

    # =========================
    # GHOST MOVES
    # =========================
    "Lick": {
        "type": "Ghost",
        "category": "Physical",
        "power": 30,
        "accuracy": 100,
        "paralysis_chance": 0.3,
        "description": "Licks the target. May cause paralysis."
    },
    "Night Shade": {
        "type": "Ghost",
        "category": "Special",
        "power": 0,
        "accuracy": 100,
        "level_based_damage": True,
        "description": "Damages target equal to user's level."
    },
    "Shadow Punch": {
        "type": "Ghost",
        "category": "Physical",
        "power": 60,
        "accuracy": 100,
        "always_hits": True,
        "description": "Never misses."
    },
    "Shadow Ball": {
        "type": "Ghost",
        "category": "Special",
        "power": 80,
        "accuracy": 100,
        "sp_defense_reduction_chance": 0.2,
        "description": "May lower target's Special Defense."
    },
    "Dream Eater": {
        "type": "Ghost",
        "category": "Special",
        "power": 100,
        "accuracy": 100,
        "requires_sleep": True,
        "heal_fraction": 0.5,
        "description": "Only works on sleeping targets. Heals user by 50% of damage."
    },
    "Dark Pulse": {
        "type": "Dark",
        "category": "Special",
        "power": 80,
        "accuracy": 100,
        "flinch_chance": 0.2,
        "description": "May cause flinching."
    },

    # =========================
    # STEEL MOVES
    # =========================
    "Iron Tail": {
        "type": "Steel",
        "category": "Physical",
        "power": 100,
        "accuracy": 75,
        "description": "Attacks with a steel tail. May lower Defense."
    },
}