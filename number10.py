def check_pangram(str):
    alphabet = "qwertyuiopasdfghjklzxcvbnm"
    for i in alphabet:
        if i not in str.lower():
            return False
    return True

example = "the quick brown fox jumps over the lazy dog"
if check_pangram(example) == True:
    print("true")
else : print("false")