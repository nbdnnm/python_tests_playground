def linear(array):
    if not array:
        return None
    else:
        min = array[0]
        counter = 0
        for i in array:
            counter += 1
        if i < min:
            min = i
        return (min, counter)


def quad(array):
    if not array:
        return None
    else:
        min = array[0]
        counter = 0
        for i in array:
            for j in array:
                counter += 1
            if min > j:
                min = j
        return (min, counter)


def test_big_o():
    arr1 = [1, 2]
    arr2 = [1]
    arr3 = [1, 2, 3]
    arr4 = [3, 2, 1]
    arr5 = []
    arr6 = [1, 1]
    arr7 = [x for x in range(100)]

    assert linear(arr1) == (1, 2)
    assert linear(arr2) == (1, 1)
    assert linear(arr3) == (1, 3)
    assert linear(arr4) == (1, 3)
    assert linear(arr5) == None
    assert linear(arr6) == (1, 2)
    assert linear(arr7) == (min(arr7), 100)

    assert quad(arr1) == (1, 4)
    assert quad(arr2) == (1, 1)
    assert quad(arr3) == (1, 9)
    assert quad(arr4) == (1, 9)
    assert quad(arr5) == None
    assert quad(arr6) == (1, 4)
    assert quad(arr7) == (min(arr7), 10000)
