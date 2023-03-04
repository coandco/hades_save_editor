from models.save_file import HadesSaveFile
from pathlib import Path
import os

# To use this script, start a new run, save, and run this.  It should edit the save to
# give you the Exclusive Access boon (all boons are epic and above).


def add_trait(save: HadesSaveFile, trait: dict):
    hero_trait_dict = save.lua_state._active_state["CurrentRun"]["Hero"]["TraitDictionary"]
    hero_traits = save.lua_state._active_state["CurrentRun"]["Hero"]["Traits"]
    if any(x.get("Title", None) == trait["Title"] for x in hero_traits.values()):
        print(f"{trait['Title']} already exists!")
        return
    else:
        highest_index = int(max(hero_traits.keys()))
        new_index = float(highest_index + 1)
        hero_traits[new_index] = trait
        hero_trait_dict[trait["Title"]] = {1.0: trait}


# Thus far it can only add traits that don't affect weapons, since those are added in a different place
epic_only_trait = {"Additional": {}, "CustomRarityColor": {1.0: 210.0, 2.0: 255.0, 3.0: 97.0, 4.0: 255.0}, "CustomRarityName": "Boon_Synergy", "Frame": "Duo", "Icon": "Dionysus_Poseidon_01", "Id": "19239.86358547210690.94035342428833", "InheritFrom": {1.0: "SynergyTrait"}, "IsDuoBoon": True, "Name": "RaritySuperBoost", "NewTotal": {}, "NewTotals": {}, "OldTotal": {}, "PercentIncrease": {}, "Rarity": "Legendary", "RarityBonus": {"EpicBonus": 1.0, "LegendaryBonus": 0.0, "RareBonus": 0.0}, "RarityLevels": {"Legendary": {"MaxMultiplier": 1.0, "MinMultiplier": 1.0}}, "RarityMultiplier": 1.0, "ReplaceUpgradedRarityTable": {"Common": "Epic", "Epic": "Heroic", "Rare": "Epic"}, "RequiredFalseRewardType": "Devotion", "RequiredFalseTrait": "RaritySuperBoost", "Title": "RaritySuperBoost"}
extra_dashes_trait = {"Additional": {1.0: 3.0}, "Cost": 30.0, "DisplayDelta1": "Increase1", "Icon": "Boon_Hermes_01", "Id": "1414655.355041503910.90760965365916", "Increase1": "Increase1", "InheritFrom": {"1.0": "ShopTier1Trait"}, "Name": "BonusDashTrait", "NewTotal": {1.0: 3.0}, "NewTotal1": "NewTotal1", "NewTotals": {}, "OldTotal": {1.0: 0.0}, "OldTotal1": "OldTotal1", "PercentIncrease": {1.0: "NEW"}, "PropertyChanges": {1.0: {"BaseValue": 3.0, "ChangeType": "Add", "ChangeValue": 3.0, "ExtractValue": {"ExtractAs": "TooltipBonusDashes", "Key": "ChangeValue"}, "WeaponNames": {1.0: "RushWeapon", 2.0: "RamWeapon"}, "WeaponProperty": "ClipSize"}}, "Rarity": "Epic", "RarityLevels": {"Common": {"Multiplier": 1.0}, "Epic": {"Multiplier": 3.0}, "Heroic": {"Multiplier": 4.0}, "Rare": {"Multiplier": 2.0}}, "RarityMultiplier": 3.0, "RequiredFalseTrait": "BonusDashTrait", "Title": "BonusDashTrait", "TooltipBonusDashes": 3.0, "TooltipBonusDashesNewTotal": 3.0, "TooltipBonusDashesTotal": 0.0, "TooltipBonusDashesTotalPercentIncrease": "NEW", "TotalPercentIncrease1": "NewTraitPrefix"}
money_per_room_trait = {"Additional": {}, "AnchorId": 2000501.0, "Cost": 30.0, "Icon": "Boon_Hermes_14", "Id": "26332024.53869628910.40881159156561", "InheritFrom": {"1.0": "ShopTier1Trait"}, "MoneyPerRoom": 100.0, "Name": "ChamberGoldTrait", "NewTotal": {}, "NewTotals": {}, "OldTotal": {}, "PercentIncrease": {}, "Rarity": "Epic", "RarityLevels": {"Common": {"MaxMultiplier": 1.0, "MinMultiplier": 1.0}, "Epic": {"MaxMultiplier": 1.6, "MinMultiplier": 1.6}, "Heroic": {"MaxMultiplier": 1.9, "MinMultiplier": 1.9}, "Rare": {"MaxMultiplier": 1.3, "MinMultiplier": 1.3}}, "RarityMultiplier": 1.6, "RequiredFalseTraits": {1.0: "ChamberGoldTrait"}, "Title": "ChamberGoldTrait", "TraitIconOverlay": 2000502.0}

if os.name == "nt":
    save_path = Path.home() / "Documents/Saved Games/Hades"
else:
    save_path = (
        Path.home()
        / ".steam/steam/steamapps/compatdata/1145360/pfx/drive_c/users/steamuser/My Documents/Saved Games/Hades"
    )

loaded_save = HadesSaveFile.from_file(save_path / "Profile1_Temp.sav")
add_trait(loaded_save, epic_only_trait)
add_trait(loaded_save, extra_dashes_trait)
add_trait(loaded_save, money_per_room_trait)

loaded_save.to_file(save_path / "Profile1_Temp.sav")
