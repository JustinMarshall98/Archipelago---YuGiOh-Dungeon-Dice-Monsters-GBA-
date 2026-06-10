from .tournament import all_tournaments
from .duelists import all_duelists
from .dice import all_dice
from .utils import Constants
from .locations import get_location_name_for_tournament, get_2nd_location_name_for_tournament, get_3rd_location_name_for_tournament, get_location_name_for_duelist, get_2nd_location_name_for_duelist, get_location_name_for_dice

division_1_locations: list[str] = []
for tournament in all_tournaments:
    if tournament.offset == Constants.DIVISION_1_COMPLETION_OFFSET:
        division_1_locations.append(get_location_name_for_tournament(tournament))
        division_1_locations.append(get_2nd_location_name_for_tournament(tournament))
        division_1_locations.append(get_3rd_location_name_for_tournament(tournament))

reverse_division_locations: list[str] = []
for tournament in all_tournaments:
    if tournament.offset == Constants.DIVISION_2_COMPLETION_OFFSET:
        reverse_division_locations.append(get_location_name_for_tournament(tournament))
        reverse_division_locations.append(get_2nd_location_name_for_tournament(tournament))
        reverse_division_locations.append(get_3rd_location_name_for_tournament(tournament))

dark_division_locations: list[str] = []
for tournament in all_tournaments:
    if tournament.offset == Constants.DIVISION_3_COMPLETION_OFFSET and tournament.name != "The Last Judgment":
        dark_division_locations.append(get_location_name_for_tournament(tournament))
        dark_division_locations.append(get_2nd_location_name_for_tournament(tournament))
        dark_division_locations.append(get_3rd_location_name_for_tournament(tournament))

duelist_locations: list[str] = []
for duelist in all_duelists:
    if duelist._name != "Yami Yugi":
        duelist_locations.append(get_location_name_for_duelist(duelist))
        duelist_locations.append(get_2nd_location_name_for_duelist(duelist))

grandpas_shop_locations: list[str] = []
for dice in all_dice:
    if dice.name != "D. Magician Girl":
        grandpas_shop_locations.append(get_location_name_for_dice(dice))

shop_tier_0_locations: list[str] = []
for dice in all_dice:
    if dice.shop_level == 0:
        shop_tier_0_locations.append(get_location_name_for_dice(dice))

shop_tier_1_locations: list[str] = []
for dice in all_dice:
    if dice.shop_level >= 1 and dice.shop_level <= 3:
        shop_tier_1_locations.append(get_location_name_for_dice(dice))

shop_tier_2_locations: list[str] = []
for dice in all_dice:
    if dice.shop_level >= 4 and dice.shop_level <= 6:
        shop_tier_2_locations.append(get_location_name_for_dice(dice))

shop_tier_3_locations: list[str] = []
for dice in all_dice:
    if dice.shop_level >= 7 and dice.shop_level <= 9:
        shop_tier_3_locations.append(get_location_name_for_dice(dice))

shop_tier_4_locations: list[str] = []
for dice in all_dice:
    if dice.shop_level >= 10 and dice.shop_level <= 12:
        shop_tier_4_locations.append(get_location_name_for_dice(dice))

shop_tier_5_locations: list[str] = []
for dice in all_dice:
    if dice.shop_level >= 13 and dice.shop_level <= 15:
        shop_tier_5_locations.append(get_location_name_for_dice(dice))

shop_tier_6_locations: list[str] = []
for dice in all_dice:
    if dice.shop_level >= 16 and dice.shop_level <= 18:
        shop_tier_6_locations.append(get_location_name_for_dice(dice))

location_groups = {
    "Division 1": division_1_locations,
    "Reverse Division": reverse_division_locations,
    "Dark Division": dark_division_locations,
    "Duelists": duelist_locations,
    "Grandpas Shop": grandpas_shop_locations,
    "Shop Tier 0": shop_tier_0_locations,
    "Shop Tier 1": shop_tier_1_locations,
    "Shop Tier 2": shop_tier_2_locations,
    "Shop Tier 3": shop_tier_3_locations,
    "Shop Tier 4": shop_tier_4_locations,
    "Shop Tier 5": shop_tier_5_locations,
    "Shop Tier 6": shop_tier_6_locations,
}