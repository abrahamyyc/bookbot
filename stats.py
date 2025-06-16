def count_words(whole_book):
    words_list = whole_book.split()
    num_words = len(words_list)
    print(f"Found {num_words} total words")

def count_characters(book_text):
    characters_counts_dict = {}
    
    for character in book_text:
        current_character = character.lower()
        if current_character in characters_counts_dict:
            characters_counts_dict[current_character] += 1
        else:
            characters_counts_dict[current_character] = 1

    return(characters_counts_dict)

def sort_character_counts(character_dictionary):
    char_num_list = []

    for character in character_dictionary:
        if character.isalpha()==True:
            char_num_dict ={}
            char_num_dict["char"]=character
            char_num_dict["num"]=character_dictionary[character]
            char_num_list.append(char_num_dict)
        else:
            pass
    
    def sort_on(character_dictionary):
        return character_dictionary["num"]

    char_num_list.sort(reverse=True, key=sort_on)

    for char_num in char_num_list:
        print(f"{char_num['char']}: {char_num['num']}")