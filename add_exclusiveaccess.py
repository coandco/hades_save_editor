from models.save_file import HadesSaveFile
from pathlib import Path
import os

# To use this script, start a new run, save, and run this.  It should edit the save to
# give you the Exclusive Access boon (all boons are epic and above).

epic_trait = {
    "Additional": {},
    "CustomRarityColor": {1.0: 210.0, 2.0: 255.0, 3.0: 97.0, 4.0: 255.0},
    "CustomRarityName": "Boon_Synergy",
    "Frame": "Duo",
    "Icon": "Dionysus_Poseidon_01",
    "Id": "19239.86358547210690.94035342428833",
    "InheritFrom": {1.0: "SynergyTrait"},
    "IsDuoBoon": True,
    "Name": "RaritySuperBoost",
    "NewTotal": {},
    "NewTotals": {},
    "OldTotal": {},
    "PercentIncrease": {},
    "Rarity": "Legendary",
    "RarityBonus": {"EpicBonus": 1.0, "LegendaryBonus": 0.0, "RareBonus": 0.0},
    "RarityLevels": {"Legendary": {"MaxMultiplier": 1.0, "MinMultiplier": 1.0}},
    "RarityMultiplier": 1.0,
    "ReplaceUpgradedRarityTable": {"Common": "Epic", "Epic": "Heroic", "Rare": "Epic"},
    "RequiredFalseRewardType": "Devotion",
    "RequiredFalseTrait": "RaritySuperBoost",
    "Title": "RaritySuperBoost",
}

if os.name == "nt":
    save_path = Path.home() / "Documents/Saved Games/Hades"
else:
    save_path = (
        Path.home()
        / ".steam/steam/steamapps/compatdata/1145360/pfx/drive_c/users/steamuser/My Documents/Saved Games/Hades"
    )

loaded_save = HadesSaveFile.from_file(save_path / "Profile1_Temp.sav")
hero_trait_dict = loaded_save.lua_state._active_state["CurrentRun"]["Hero"]["TraitDictionary"]
hero_traits = loaded_save.lua_state._active_state["CurrentRun"]["Hero"]["Traits"]
if any(x.get("Title", None) == "RaritySuperBoost" for x in hero_traits.values()):
    print("Exclusive Access already exists!")
    exit(1)
else:
    highest_index = int(max(hero_traits.keys()))
    new_index = float(highest_index + 1)
    hero_traits[new_index] = epic_trait
    hero_trait_dict["RaritySuperBoost"] = {1.0: epic_trait}

loaded_save.to_file(save_path)
