import numpy as np
import webbrowser


def generate(mapping, nchars=100):
    """
    Generate a sentence in a language

    Parameters
    ----------
    mapping : dict[tuple[str, int, str]]
        Language mapping the format {ipa: (type, proportion, character)}
    nchars : int, optional
        Number of characters to generate, by default 100

    Returns
    -------
    str
        Randomly generated sentence
    """

    # string to store script
    script = ""
    # string to store previous types
    history = "n"

    # calculate weights for each character
    weights = [val[1] for val in mapping.values()]
    nweights = [val / sum(weights) for val in weights]

    for n in range(nchars):
        # choose an index, with choice weighted by specified probabilities
        phoneme = np.random.choice(
            list(mapping), p=nweights
        )
        # get values from mapping array
        categ, _, char = mapping[phoneme]

        # no double chars
        if script and char == script[-1]:
            continue
        # max of two successive vowels
        if categ == history[-1] == history[-2] == "v":
            continue
        # max of 3 successive consonants
        if categ == history[-1] == history[-2] == history[-3] == "c":
            continue
        # append everything if we got this far
        script += phoneme
        history += categ
    
    return script


def translate(mapping, ipa):
    """
    Translate IPA into a language

    Parameters
    ----------
    mapping : dict[tuple[str, int, str]]
        Language mapping the format {ipa: (type, proportion, character)}
    ipa : str
        IPA characters to translate
    """

    # start off with nothing
    script = ""
    # translate each letter
    for phoneme in ipa:
        # get character (or ?) from mappings
        if phoneme in mapping:
            _, _, char = mapping[phoneme]
        else:
            char = "?"
        # add it to string
        script += char
    
    return script

# --- Define languages ---
# values in the format:
# (type, IPA phoneme, probability, character)

tabaxan = {
    ' ': ("p", 28, " 𐎟 "),
    # consonants
    'l': ("c", 12, "𐎚"),
    'ɽ̊': ("c", 13, "𐎀"),
    'ɾ': ("c", 10, "𐎔"),
    "r": ("c", 15, "𐎅"),
    'ʀ̥': ("c", 12, "𐎛"),
    'm': ("c", 8,  "𐎗"),
    'n': ("c", 6,  "𐎋"),
    'ɲ': ("c", 12, "𐎆"),
    's': ("c", 10, "𐎂"),
    'θ': ("c", 8,  "𐎕"),
    'ʃ': ("c", 12, "𐎍"),
    # vowels
    'e': ("v", 9,  "𐎖"),
    'u': ("v", 8,  "𐎉"),
    'ʊ': ("v", 10, "𐎘"),
    'i': ("v", 12, "𐎑"),
    'a': ("v", 10, "𐎓"),
}

loxan = {
    ' ': ("p", 48, " ૉ "),
    # consonants
    'ʒ': ("c", 8, "હ"),
    'b': ("c", 12, "જ"),
    'ʈ': ("c", 10, "ય"),
    'p': ("c", 12, "ર"),
    'ɖ': ("c", 8, "પ"),
    'ʃ': ("c", 8, "ત"),
    'v': ("c", 14, "ટ"),
    'b': ("c", 16, "ળ"),
    # vowels
    'ə': ("v", 14,  "ઇ"),
    'ʋ': ("v", 16, "ઉ"),
    'ä': ("v", 16, "ઘ"),
    'i': ("v", 10, "ખ")
}


if __name__ == "__main__":
    current_mapping = loxan
    # generate sentence
    ipa = generate(current_mapping)
    # translate chars
    script = translate(current_mapping, ipa)
    # open IPA link in browser
    webbrowser.open("http://ipa-reader.xyz/?text=" + ipa)
    # print words next to pronunciation
    for t, p in zip(ipa.split(" "), script.split(current_mapping[" "][-1])):
        print(t, p)
