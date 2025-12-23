# Credit to Rosalie and her work on the FFT II project that I'm basing this on https://github.com/Rosalie-A/Archipelago/blob/finalfantasytactics/worlds/fftii/Rom.py
import json
import os
import pkgutil

from pathlib import Path

import bsdiff4

from worlds.Files import APProcedurePatch, APTokenMixin, APPatchExtension

from typing import BinaryIO

class YuGiOhDDMPatchExtension(APPatchExtension):
    game = "YuGiOh! Dungeon Dice Monsters"

    @staticmethod
    def patch_rom(caller, iso, placement_file):
        patch_dict = json.loads(caller.get_file(placement_file))
        if patch_dict["DiceStats"] == 1:
            base_patch = pkgutil.get_data(__name__, "ddmshopanddicestats.bsdiff4")
        else:
            base_patch = pkgutil.get_data(__name__, "ddmshoponly.bsdiff4")
        rom_data = bsdiff4.patch(iso, base_patch)
        rom_data = bytearray(rom_data)
        return rom_data
    
class YuGiOhDDMProcedurePatch(APProcedurePatch, APTokenMixin):
    game = "YuGiOh! Dungeon Dice Monsters"
    hash = "1AC4901F9A831D6B86CA776BB61F8D8B"
    patch_file_ending = ".apygoddm"
    result_file_ending = ".gba"

    procedure = [
        ("patch_rom", ["patch_file.json"])
    ]

    def patch(self, target: str) -> None:
        file_name = target[:-4]
        if os.path.exists(file_name + ".gba"):
            os.unlink(file_name + ".gba")
        
        super().patch(target)
        os.rename(target, file_name + "patched" + ".gba")