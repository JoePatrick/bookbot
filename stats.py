def get_word_count(text):
    num_words = text.split()
    return len(num_words)

def get_letter_count(text):
    letter_count = {}
    text_lower = text.lower()
    for i in text_lower:
        if i in letter_count:
            letter_count[i] += 1
        else:
            letter_count[i] = 1
    return letter_count

def get_sorted_dict(dict):
    letter_list = []
    for letter, count in dict.items():
        letter_list.append({"letter": letter, "count": count})
   # return letter_list
    return sorted(letter_list, key=lambda x: x["count"], reverse=True)
    