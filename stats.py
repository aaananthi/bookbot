def get_num_words(file_contents):
    print("----------- Word Count ----------")
    file_contents_list = file_contents.split()
    words_count = len(file_contents_list)

    print(f"Found {words_count} total words")

def get_character_count(file_contents):
    print("--------- Character Count -------")
    character_dict = {}

    for i in file_contents:
        i = i.lower()
        if i not in character_dict:
            character_dict[i] = 1
        else:
            character_dict[i] += 1
        
    def sort_on(items):
        return items["num"]
    
    character_list = []

    for key in character_dict:
        character = {"char": key, "num": character_dict[key]}
        character_list.append(character)

    character_list.sort(reverse = True, key = sort_on)
    
    for i in character_list:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")

    return
