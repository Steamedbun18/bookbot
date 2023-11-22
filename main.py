books_path = "Books/"


# open the file to read
def Open_book(bookfile):
    with open(books_path+bookfile) as file:
        return file.read()

# count number of alphabet chars in dictionary
def Char_count(book_string):
    char_dict = {}
    for char in book_string:
        if char.isalpha():
            character = char.lower()
            if character in char_dict:
                char_dict[character] += 1
            else:
                char_dict[character] = 1     
    return char_dict


# convert dictionary to sorted list
def dict_to_list(dict):
    new_list = [(key, value) for key, value in dict.items()]
    new_list.sort(reverse=True, key = lambda x: x[1])
    return new_list

def main():
    book_file = "frankenstein.txt"
    with open(books_path + book_file) as file:
        book = file.read()

    
    print(f"--- Begin reports of {book_file} ---")
    print(f"{len(book.split())} words found in document")
    print()

    character_dict = Char_count(book)
    sorted_list = dict_to_list(character_dict)
    for items in sorted_list:
        print(f"the '{items[0]}' character was found {items[1]} times")


   
    print("--- End report ---")



if __name__ == "__main__":
    main()