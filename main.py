import pandas

with open("nato_phonetic_alphabet.csv") as nato_file:
    file_content = pandas.read_csv(nato_file)
    nato_dict = {row.letter: row.code for (index, row) in file_content.iterrows()}
    print(nato_dict)


word = input("Enter a word: ").upper()
try:
    output_list = [nato_dict[letter] for letter in word]
except KeyError:
    print("Sorry, only letters in the alphabet please.")
else:
    print(output_list)
