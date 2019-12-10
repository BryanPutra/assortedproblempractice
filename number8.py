def find_longest_word(words_list):
    words_len = []
    for i in words_list:
        words_len.append((len(i), i))
    words_len.sort()
    return words_len[-1][1]

print(find_longest_word([ "AAA","BBBB","CCCCC"]))