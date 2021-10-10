

import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")


phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

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
