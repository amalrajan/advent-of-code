import copy
import math
import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def calculate_winner(player, boss):
    turn = True

    while player["Hit Points"] > 0 and boss["Hit Points"] > 0:
        if turn:
            boss["Hit Points"] -= max(1, player["Damage"] - boss["Armor"])
        else:
            player["Hit Points"] -= max(1, boss["Damage"] - player["Armor"])

        # print(player["Hit Points"], boss["Hit Points"])

        # Swap turns
        turn = not turn

    # Return True if player wins
    if player["Hit Points"] > 0:
        return True
    else:
        return False


def solve():
    equipments = [
        {
            "Name": "Dagger",
            "Cost": 8,
            "Damage": 4,
            "Armor": 0,
            "Category": "Weapons",
        },
        {
            "Name": "Shortsword",
            "Cost": 10,
            "Damage": 5,
            "Armor": 0,
            "Category": "Weapons",
        },
        {
            "Name": "Warhammer",
            "Cost": 25,
            "Damage": 6,
            "Armor": 0,
            "Category": "Weapons",
        },
        {
            "Name": "Longsword",
            "Cost": 40,
            "Damage": 7,
            "Armor": 0,
            "Category": "Weapons",
        },
        {
            "Name": "Greataxe",
            "Cost": 74,
            "Damage": 8,
            "Armor": 0,
            "Category": "Weapons",
        },
        {
            "Name": "Leather",
            "Cost": 13,
            "Damage": 0,
            "Armor": 1,
            "Category": "Armor",
        },
        {
            "Name": "Chainmail",
            "Cost": 31,
            "Damage": 0,
            "Armor": 2,
            "Category": "Armor",
        },
        {
            "Name": "Splintmail",
            "Cost": 53,
            "Damage": 0,
            "Armor": 3,
            "Category": "Armor",
        },
        {
            "Name": "Bandedmail",
            "Cost": 75,
            "Damage": 0,
            "Armor": 4,
            "Category": "Armor",
        },
        {
            "Name": "Platemail",
            "Cost": 102,
            "Damage": 0,
            "Armor": 5,
            "Category": "Armor",
        },
        {
            "Name": "Damage +1",
            "Cost": 25,
            "Damage": 1,
            "Armor": 0,
            "Category": "Rings",
        },
        {
            "Name": "Damage +2",
            "Cost": 50,
            "Damage": 2,
            "Armor": 0,
            "Category": "Rings",
        },
        {
            "Name": "Damage +3",
            "Cost": 100,
            "Damage": 3,
            "Armor": 0,
            "Category": "Rings",
        },
        {
            "Name": "Defense +1",
            "Cost": 20,
            "Damage": 0,
            "Armor": 1,
            "Category": "Rings",
        },
        {
            "Name": "Defense +2",
            "Cost": 40,
            "Damage": 0,
            "Armor": 2,
            "Category": "Rings",
        },
        {
            "Name": "Defense +3",
            "Cost": 80,
            "Damage": 0,
            "Armor": 3,
            "Category": "Rings",
        },
    ]

    player = {
        "Hit Points": 100,
        "Damage": 0,
        "Armor": 0,
    }

    boss = {
        "Hit Points": 104,
        "Damage": 8,
        "Armor": 1,
    }

    ans = math.inf

    def backtrack(
        player,
        boss,
        equipments,
        gold,
        weapon_count,
        armor_count,
        ring_count,
    ):
        nonlocal ans
        if not equipments:
            return

        # Only calculate battle outcome if at least 1 weapon
        battle_outcome = False
        if weapon_count == 1:
            battle_outcome = calculate_winner(
                copy.deepcopy(player),
                copy.deepcopy(boss),
            )

        if battle_outcome == True:
            if gold < ans:
                ans = gold
            return

        # Include current equipment
        if (
            (equipments[0]["Category"] == "Weapons" and weapon_count >= 1)
            or (equipments[0]["Category"] == "Armor" and armor_count >= 1)
            or (equipments[0]["Category"] == "Rings" and ring_count > 2)
        ):
            pass
        else:
            player_updated = copy.deepcopy(player)
            player_updated["Damage"] += equipments[0]["Damage"]
            player_updated["Armor"] += equipments[0]["Armor"]

            backtrack(
                player_updated,
                boss,
                equipments[1:],
                gold + equipments[0]["Cost"],
                (
                    weapon_count + 1
                    if equipments[0]["Category"] == "Weapons"
                    else weapon_count
                ),
                (
                    armor_count + 1
                    if equipments[0]["Category"] == "Armor"
                    else armor_count
                ),
                ring_count + 1 if equipments[0]["Category"] == "Ring" else ring_count,
            )

        # Exclude current equipment
        backtrack(
            player,
            boss,
            equipments[1:],
            gold,
            weapon_count,
            armor_count,
            ring_count,
        )

    backtrack(
        player,
        boss,
        equipments,
        0,
        0,
        0,
        0,
    )

    return ans


if __name__ == "__main__":
    print(solve())
