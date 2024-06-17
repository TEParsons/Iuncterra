import numpy as np
import webbrowser


def generate(mapping, nchars=100):
    """
    Generate a sentence in tabaxan.

    Parameters
    ----------
    mapping : dict[tuple[str, int, str]]
        Language mapping the format {ipa: (type, proportion, character)}
    nchars : int, optional
        Number of characters to generate, by default 100

    Returns
    -------
    str
        Randomly generated tabaxan sentence
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
    Translate IPA into tabaxan

    Parameters
    ----------
    mapping : dict[tuple[str, int, str]]
        Language mapping the format {ipa: (type, proportion, character)}
    ipa : str
        IPA characters to translate
    """

    # start off with nothing
    tabaxan = ""
    # translate each letter
    for phoneme in ipa:
        # get character (or ?) from mappings
        if phoneme in mapping:
            _, _, char = mapping[phoneme]
        else:
            char = "?"
        # add it to string
        tabaxan += char
    
    return tabaxan

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

if __name__ == "__main__":
    mapping = tabaxan
    # generate sentence
    # ipa = generate(mapping)
    ipa = "ʀ̥isʃir nʊrɲ rɾiʃ  ʀ̥isʃaʊ lʀ̥s ɲmʊɾiʀ̥"
    # translate chars
    script = translate(mapping, ipa)
    # open IPA link in browser
    # webbrowser.open("http://ipa-reader.xyz/?text=" + ipa)
    # print words next to pronunciation
    for t, p in zip(ipa.split(" "), script.split(mapping[" "][-1])):
        print(t, p)
