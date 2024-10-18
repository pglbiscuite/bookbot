def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        words = file_contents.split()
        total = 0
        for number in words:
            total += 1
    #print(total)
    return total


def get_num_letters():
    with open('books/frankenstein.txt') as f:
        alphabet = {
 'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 
 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 
 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 
 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 
 'y': 0, 'z': 0
}
        file_contents = f.read()
        lower_string = file_contents.lower()
        for letter in lower_string:
            if letter in alphabet:
                alphabet[letter] += 1
        return alphabet




def final_report():
        total_words = main()
        letter_counts = get_num_letters()

        print(f"--- Begin report of books/frankenstein.txt ---")
        print(f"{total_words} words found in the document\n")

        for character, count in sorted(letter_counts.items(), key=lambda item: item[1], reverse=True):
                print(f"The '{character}' character was found {count} times")
    
        print("--- End report ---")



final_report()
#       result = get_num_letters()
#       print(result)
#       words = main()
#       print(words)
# if __name__ == "__main__":
#       main()
        