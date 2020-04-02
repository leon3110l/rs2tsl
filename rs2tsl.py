import json
from rsrtools.files.welder import Welder
from pathlib import Path
import re

def create_tsl(dlc_json):

    for key, song in dlc_json['Entries'].items():
        attr = song['Attributes']
        tones = attr['Tones']

        for tone in tones:
            if(tone is None):
                continue

            tone_name = tone['Name']
            tone_desc = tone['ToneDescriptors']

            with open('clean_patch.tsl') as clean_patch:
                tsl = json.load(clean_patch)

                print()
                print()
                print(tone_name)
                print("-------------")

                params = tsl['patchList']['params']

                

                for key, item in tone["GearList"].items():
                    print(item['Type'] + " - " + item['Key'])

def create_tsl_from_psarc(psarc: Path):
    welder = Welder(path, "r")
    for index in welder:
        file_name = welder.arc_name(index)
        if("manifest" in file_name and file_name.endswith(".json") and not file_name.endswith("vocals.json")):
            print()
            print(file_name)
            dlc = json.loads(welder.arc_data(index).decode())
            create_tsl(dlc)



if __name__ == "__main__":
    # load all psarc files in my folder, rglob for recursive
    for path in Path('D:/rocksmith dlc backup/').glob("*p.psarc"):
        create_tsl_from_psarc(path)