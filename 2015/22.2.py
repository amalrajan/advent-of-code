import copy
import json
import math
import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def solve():
    spells = {
        "Magic Missile": {
            "Mana Cost": 53,
            "Damage": 4,
            "Healing": 0,
            "Armor": 0,
            "Effect Turns": 1,
            "Mana": 0,
        },
        "Drain": {
            "Mana Cost": 73,
            "Damage": 2,
            "Healing": 2,
            "Armor": 0,
            "Effect Turns": 1,
            "Mana": 0,
        },
        "Shield": {
            "Mana Cost": 113,
            "Damage": 0,
            "Healing": 0,
            "Armor": 7,
            "Effect Turns": 6,
            "Mana": 0,
        },
        "Poison": {
            "Mana Cost": 173,
            "Damage": 3,
            "Healing": 0,
            "Armor": 0,
            "Effect Turns": 6,
            "Mana": 0,
        },
        "Recharge": {
            "Mana Cost": 229,
            "Damage": 0,
            "Healing": 0,
            "Armor": 0,
            "Effect Turns": 5,
            "Mana": 101,
        },
    }

    boss = {
        "Hit Points": 58,
        "Damage": 9,
    }

    player = {
        "Hit Points": 50,
        "Mana": 500,
        "Damage": 0,
        "Armor": 0,
        "Mana Spent": 0,
    }

    min_mana_spent = math.inf
    visited = set()

    def apply_effects(player, boss):
        # Part 2
        player["Hit Points"] -= 1

        # Apply active spell effects
        player["Armor"] = 0  # Reset armor to base value each turn
        for spell_name, spell in spells.items():
            spell_turns = f"{spell_name}_Turn"
            if spell_turns in player and player[spell_turns] > 0:
                boss["Hit Points"] -= spell["Damage"]
                player["Armor"] += spell["Armor"]
                player["Hit Points"] += spell["Healing"]
                player["Mana"] += spell["Mana"]
                player[spell_turns] -= 1

    def backtrack(player, boss, turn):
        nonlocal min_mana_spent, visited

        if player["Mana Spent"] > min_mana_spent:
            return

        # Cache visited branches
        temp_key = copy.deepcopy(player)
        temp_key.pop("Mana Spent")
        serialized = json.dumps(temp_key) + json.dumps(boss) + str(turn)
        if serialized in visited:
            return
        else:
            visited.add(serialized)

        apply_effects(player, boss)

        if player["Hit Points"] <= 0 or player["Mana"] < 0:
            return

        if boss["Hit Points"] <= 0:
            min_mana_spent = min(min_mana_spent, player["Mana Spent"])
            return

        if turn:
            # Attempt to activate a new spell
            for spell_name, spell in spells.items():
                spell_turns = f"{spell_name}_Turn"
                if spell_turns in player and player[spell_turns] > 0:
                    continue

                if player["Mana"] < spell["Mana Cost"]:
                    continue

                new_player = copy.deepcopy(player)
                new_boss = copy.deepcopy(boss)

                # Activate spell
                new_player[spell_turns] = spell["Effect Turns"]
                new_player["Mana"] -= spell["Mana Cost"]
                new_player["Mana Spent"] += spell["Mana Cost"]

                backtrack(
                    new_player,
                    new_boss,
                    not turn,
                )
        else:
            new_player = copy.deepcopy(player)
            new_boss = copy.deepcopy(boss)

            damage_taken = max(1, new_boss["Damage"] - new_player["Armor"])
            new_player["Hit Points"] -= damage_taken
            backtrack(
                new_player,
                new_boss,
                not turn,
            )

    backtrack(player, boss, True)
    return min_mana_spent


if __name__ == "__main__":
    print(solve())
