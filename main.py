

import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")


# TODO 1. Create a dictionary in this format
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def phonetic():
    word = input("enter word: ").upper()

    try:
        output_list = [phonetic_dict[letters] for letters in word]
    except KeyError:
        print("Only letters from the alphabet")
        phonetic()
    else:
        print(output_list)


phonetic()
