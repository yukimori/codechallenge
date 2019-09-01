def spin_words(sentence):
    words = sentence.split()
    for i, word in enumerate(words):
        if len(word) >= 5:
            words[i] = word[::-1]
    return " ".join(words)

def spin_words_best():
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

def test_spin_words():
    print(spin_words("Hey fellow warriors"))
    print(spin_words("This is another test"))
    print(spin_words("in word in gnirts Write Just will Kata the"))
    print(spin_words("tsisnoc dessap only the Just all one tsisnoc Kata Write or all one will when a desrever"))

if __name__ == '__main__':
    test_spin_words()