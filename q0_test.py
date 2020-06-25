def get_count(input_str):
    vowel = []
    for v_count in input_str:
        if v_count == 'a':
            vowel.append(v_count)
        elif v_count == 'e':
            vowel.append(v_count)
        elif v_count == 'i':
            vowel.append(v_count)
        elif v_count == 'o':
            vowel.append(v_count)
        elif v_count == 'u':
            vowel.append(v_count)
        else:
            pass
    return len(vowel)


# tester provided
def test_sample():
    assert get_count("abracadabra") == 5
    assert get_count("") == 0
    assert get_count("bcd,! ?") == 0
    assert get_count("pear tree") == 4
    assert get_count("o a kak ushakov lil vo kashu kakao") == 13
