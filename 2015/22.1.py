import copy
import math
import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def solve(inputs):
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
        "Hit Points": 13,
        "Damage": 8,
    }
    player = {
        "Hit Points": 10,
        "Mana": 250,
        "Damage": 0,
        "Armor": 0,
    }

    min_mana_spent = math.inf

    def backtrack(player, boss, turn, mana_spent):
        nonlocal min_mana_spent

        if player["Hit Points"] <= 0:
            return

        if boss["Hit Points"] <= 0:
            min_mana_spent = min(min_mana_spent, mana_spent)
            return

        for spell in spells:
            if spell in player and player[spell] > 0:
                continue

            # Activate spell
            updated_player = copy.deepcopy(player)
            for feature in spells[spell]:
                if feature in ["Damage", "Healing", "Armor", "Mana"]:
                    updated_player[feature] += spells[spell][feature]
                    updated_player[spell] = spells[spell]["Effect Turns"]
            backtrack(
                # player
            )


if __name__ == "__main__":
    print(solve())
