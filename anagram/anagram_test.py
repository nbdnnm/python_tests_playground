def anagram_detection_quad(set_of_strings):
    first = list(set_of_strings[0])
    second = list(set_of_strings[1])
    is_anagram = False
    count = 0
    if len(first) != len(second):
        count += 1
        return (is_anagram, count)
    else:
        for num1, char1 in enumerate(first):
            for num2, char2 in enumerate(second):
                count += 1
                if char1 == char2:
                    first[num1] = None
                    second[num2] = None
                    break

    if first == second:
        is_anagram = True
    return (is_anagram, count)


case1 = ("onef", "fneo")
case2 = ("npp", "npp")
case3 = ("on e", "neo")
case4 = ("on e", "n eo")
case5 = ("one", "ne")
case6 = ("one", "neoo")
case7 = ("one", "nee")
case8 = ("one", "neee")
case9 = ("one", "ne")


def test_quad_anagram():
    assert anagram_detection_quad(case1) == (True, 10)
    assert anagram_detection_quad(case2) == (True, 6)
    assert anagram_detection_quad(case3) == (False, 1)
    assert anagram_detection_quad(case4) == (True, 10)
    assert anagram_detection_quad(case5) == (False, 1)
    assert anagram_detection_quad(case6) == (False, 1)
    assert anagram_detection_quad(case7) == (False, 6)
    assert anagram_detection_quad(case8) == (False, 1)
    assert anagram_detection_quad(case9) == (False, 1)
