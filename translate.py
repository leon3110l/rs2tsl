translation = {
    "mid": "middle"
}

def translate(key: str):
    if(key in translation):
        return translation[key]
    
    return key