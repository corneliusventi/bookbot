def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_counts = get_char_counts(text)
    print_report(book_path, word_count, char_counts)


def print_report(path, word_count, char_counts):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")

    new_char_counts = []
    for char, count in char_counts.items():
        if (char.isalpha()):
            new_char_counts.append({
                "char": char,
                "count": count
            })
    new_char_counts.sort(reverse=True, key=sort_by_count)
    for char_count in new_char_counts:
        char, count = char_count["char"], char_count["count"]
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")


def sort_by_count(dict):
    return dict["count"]


def get_char_counts(text):
    counts = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts


def get_word_count(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()