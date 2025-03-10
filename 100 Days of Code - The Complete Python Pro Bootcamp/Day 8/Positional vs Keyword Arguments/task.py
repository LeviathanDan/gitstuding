
word_true = ['t', 'r', 'u', 'e']
word_love = ['l', 'o', 'v', 'e']



def calculate_love_score(name1, name2):
    listed_name = list(name1)
    listed_name2 = list(name2)


    count_letters_true = 0
    count_letters_love = 0

    for letter in word_true:
        count = listed_name.count(letter) + listed_name2.count(letter)
        count_letters_true += count
    for letter in word_love:
        count = listed_name2.count(letter) + listed_name.count(letter)
        count_letters_love += count


    print(f"{count_letters_true}"f"{count_letters_love}")







calculate_love_score("Kanye West", "Kim Kardashian")
