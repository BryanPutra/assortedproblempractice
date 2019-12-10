def filter_long_words(words_list,n : int):
    words_len = []
    for i in words_list:
        if len(i) > n:
            words_len.append(i)
    return words_len

print(filter_long_words(["AAAA","BBBBBBBBBBB","SSSSSSSSSSSSSSSSSSSS"],12 ))

