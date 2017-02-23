def anagram(word):
    file = open("file", "r")
    anagrams = []
    for line in file:
        line = line.strip()
        words = line.split(" ")
        for w in words:
            if len(w) == len(word):
                for i in xrange(len(w)):
                    if verify_anagram(w, word):
                        anagrams.append(w)
    return anagrams


def verify_anagram(w1, w2):
    if len(w1) != len(w2):
        return False
    while len(w1) > 0:
        c = w1[0]
        w1 = w1.replace(c, "")
        w2 = w2.replace(c, "")
        if len(w1) != len(w2):
            return False
    return True

print anagram("anagrama")