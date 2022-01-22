def convert_ascii_dvorak(string):
    conversion = {
        "a": "a",
        "o": "s",
        "e": "d",
        "u": "f",
        "i": "g",
        "d": "h",
        "h": "j",
        "t": "k",
        "n": "l",
        "s": "ö", 
        "ü": "q",
        ",": "w",
        ".": "e",
        "p": "r",
        "y": "t",
        "f": "z",
        "g": "u",
        "c": "i",
        "r": "o",
        "l": "p",
        "#": "ü",
        "<": "+",
        "ä": "^",
        "ö": "y",
        "q": "x",
        "j": "c",
        "k": "v",
        "x": "b",
        "b": "n",
        "m": "m",
        "w": ",",
        "v": ".",
        "z": "-"
    }
    stringConverted = ""
    for char in string:
        if char in conversion:
            stringConverted += conversion[char]
        else:
            stringConverted += char
    return stringConverted
