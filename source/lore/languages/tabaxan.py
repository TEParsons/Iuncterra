import numpy as np
import webbrowser

# number of chars to do
nChars = 100

# values in the format:
# (type, IPA phoneme, probability, tabaxan character)
mapping = [
    ("p", " ", 28, "𐎟"),
    # consonants
    ("c", "l", 12, "𐎚"),
    ("c", "ɽ̊", 13, "𐎀"),
    ("c", "ɾ", 10, "𐎔"),
    ("c", "r", 15, "𐎅"),
    ("c", "ʀ̥", 12, "𐎛"),
    ("c", "m", 8, "𐎗"),
    ("c", "n", 6, "𐎋"),
    ("c", "ɲ", 12, "𐎆"),
    ("c", "s", 10, "𐎂"),
    ("c", "θ", 8, "𐎕"),
    ("c", "ʃ", 12, "𐎍"),
    # vowels
    ("v", "e", 9, "𐎖"),
    ("v", "u", 8, "𐎉"),
    ("v", "ʊ", 10, "𐎘"),
    ("v", "i", 12, "𐎑"),
    ("v", "a", 10, "𐎓"),
]
# string to store IPA reader link
ipa = "http://ipa-reader.xyz/?text="
# string to store tabaxan script
script = ""
# string to store previous types
history = "n"

# calculate weights for each character
weights = [val[2] for val in mapping]
nweights = [val / sum(weights) for val in weights]

for n in range(nChars):
    # choose an index, with choice weighted by specified probabilities
    i = np.random.choice(
        range(len(mapping)), p=nweights
    )
    # get values from mapping array
    categ, phoneme, weight, char = mapping[i]

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
    ipa += phoneme
    script += char
    history += categ

# open IPA link in browser
webbrowser.open(ipa)
# print tabaxan script
print(script)
