import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter:row.code for (index,row) in data.iterrows()}
is_on = True
while is_on:
    name = input("Enter your name: ").upper()
    try:
        if name == "EXIT":
            is_on = False
        else:
            l = [x for x in name]
            final_list = [data_dict[x] for x in name]
    except KeyError:
        print("Sorry, only letters in the alphabets please.")
    else:
        print(final_list)

