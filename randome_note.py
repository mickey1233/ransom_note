from collections import Counter


def canconstruct(ransomNote, magazine):
    a = Counter(ransomNote)
    b = Counter(magazine)
    for i in a:
        if a[i] > b[i]:
            return False
    return True


if __name__ == "__main__":
    print(canconstruct("a", "b"))
    print(canconstruct("aa", "ab"))
    print(canconstruct("aa", "aab"))
