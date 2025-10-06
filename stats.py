def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    char_dic = {}
    for c in text:
        char = c.lower()
        if char in char_dic:
            char_dic[char] += 1
        else:
            char_dic[char] = 1
    return char_dic

def sort_on(value):
    return value["num"]

def sort_dic(c_dic):
    dic_list = []
    for k in c_dic:
        new_dict = {}
        new_dict["char"] = k
        new_dict["num"] = c_dic[k]
        dic_list.append(new_dict)

    dic_list.sort(reverse=True, key=sort_on)
    for char in dic_list:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
        else:
            continue
