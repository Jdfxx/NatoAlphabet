import pandas

with open("nato_phonetic_alphabet.csv") as nato_file:
    file_content = pandas.read_csv(nato_file)
    nato_dict = {row.letter: row.code for (index, row) in file_content.iterrows()}
    print(nato_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
output_list = [nato_dict[letter] for letter in word]
print(output_list)
