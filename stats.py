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

def sort_dic(c_dic):
    dic_list = []
    chars = {"char": "a"}
    nums = {"num": 0}
    for key in c_dic:

    