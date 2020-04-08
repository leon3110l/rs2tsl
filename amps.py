from katana_tsl_patch.katana.pedals.amp import Amp, AmpType

import json

from translate import translate

def create_amp(amp_type: AmpType):
    def _create(knobs):
        return Amp(
            amp_type,
            **knobs
        )

    return _create


amps = {
    "DEFAULT": create_amp(AmpType.CLEAN),
    "Amp_AT120": create_amp(AmpType.CLEAN),
    "Amp_AT20": create_amp(AmpType.CLEAN),
    "Amp_BT15": create_amp(AmpType.CLEAN),
    "Amp_BT30": create_amp(AmpType.CLEAN),
    "Amp_BT45": create_amp(AmpType.CLEAN),
    "Amp_CA100": create_amp(AmpType.CLEAN),
    "Amp_CA38": create_amp(AmpType.CLEAN),
    "Amp_CA85": create_amp(AmpType.CLEAN),
    "Amp_CS100": create_amp(AmpType.CLEAN),
    "Amp_CS120": create_amp(AmpType.CLEAN),
    "Amp_CS90": create_amp(AmpType.CLEAN),
    "Amp_EN30": create_amp(AmpType.CLEAN),
    "Amp_EN50": create_amp(AmpType.CLEAN),
    "Amp_GB100": create_amp(AmpType.CLEAN),
    "Amp_GB38": create_amp(AmpType.CLEAN),
    "Amp_GB50": create_amp(AmpType.CLEAN),
    "Amp_GibsonGA88": create_amp(AmpType.CLEAN),
    "Amp_HG100": create_amp(AmpType.CLEAN),
    "Amp_HG180": create_amp(AmpType.CLEAN),
    "Amp_HG500": create_amp(AmpType.CLEAN),
    "Amp_Marshall1962Bluesbreaker": create_amp(AmpType.CLEAN),
    "Amp_MarshallDSL100H": create_amp(AmpType.CLEAN),
    "Amp_MarshallDSL15H": create_amp(AmpType.CLEAN),
    "Amp_MarshallJCM800": create_amp(AmpType.CLEAN),
    "Amp_MarshallJTM45": create_amp(AmpType.CLEAN),
    "Amp_MarshallJVM410H": create_amp(AmpType.CLEAN),
    "Amp_MarshallPlexi": create_amp(AmpType.CLEAN),
    "Amp_OrangeAD50": create_amp(AmpType.CLEAN),
    "Amp_OrangeJimmyBean": create_amp(AmpType.CLEAN),
    "Amp_OrangeOR100": create_amp(AmpType.CLEAN),
    "Amp_OrangeOR50H": create_amp(AmpType.CLEAN),
    "Amp_OrangeRockerverb": create_amp(AmpType.CLEAN),
    "Amp_OrangeTinyTerror": create_amp(AmpType.CLEAN),
    "Amp_TW22": create_amp(AmpType.CLEAN),
    "Amp_TW26": create_amp(AmpType.CLEAN),
    "Amp_TW40": create_amp(AmpType.CLEAN),
    "Bass_Amp_BT600B": create_amp(AmpType.CLEAN),
    "Bass_Amp_BT880B": create_amp(AmpType.CLEAN),
    "Bass_Amp_BT975B": create_amp(AmpType.CLEAN),
    "Bass_Amp_CH300B": create_amp(AmpType.CLEAN),
    "Bass_Amp_CH350B": create_amp(AmpType.CLEAN),
    "Bass_Amp_CH600B": create_amp(AmpType.CLEAN),
    "Bass_Amp_CS240B": create_amp(AmpType.CLEAN),
    "Bass_Amp_CS300B": create_amp(AmpType.CLEAN),
    "Bass_Amp_CS75B": create_amp(AmpType.CLEAN),
    "Bass_Amp_EdenE300": create_amp(AmpType.CLEAN),
    "Bass_Amp_EdenWT550": create_amp(AmpType.CLEAN),
    "Bass_Amp_EdenWT800": create_amp(AmpType.CLEAN),
    "Bass_Amp_HT100B": create_amp(AmpType.CLEAN),
    "Bass_Amp_HT300B": create_amp(AmpType.CLEAN),
    "Bass_Amp_HT400B": create_amp(AmpType.CLEAN),
    "Bass_Amp_LT25B": create_amp(AmpType.CLEAN),
    "Bass_Amp_LT85B": create_amp(AmpType.CLEAN),
    "Bass_Amp_OrangeAD200B": create_amp(AmpType.CLEAN),
    "DI_Amp_BassDriver": create_amp(AmpType.CLEAN),
    "DI_Amp_MixerPre": create_amp(AmpType.CLEAN),
    "DI_Amp_TubePre": create_amp(AmpType.CLEAN),
}

def get_amp(amp_key: str, knob_values):
    
    knobs = {}

    for key, value in knob_values.items():
        key = key.replace(amp_key + "_", "").lower()
        if(key in ['gain', 'bass', 'mid', 'treble']):
            knobs[translate(key)] = value

    if(amp_key not in amps):
        amp_key = "DEFAULT"

    return amps[amp_key](knobs)

if __name__ == "__main__":

    with open('bob_redemption.json') as file:
        bob = json.load(file)
        for key, song in bob['Entries'].items():
            tones = song['Attributes']['Tones']
            for tone in tones:
                tone_name = tone['Name']
                print(tone_name)
                get_amp(tone['GearList']['Amp']['Key'], tone['GearList']['Amp']['KnobValues'])
