
def test_my_list():
    my_list = [1, 2, 3, 4, 5, 3, 5, 6, 7, 8, 9, 10]
    print("\nmy_list", my_list)
    my_list.append(11)
    print("my_list.append(11)", my_list)
    my_list.remove(11)
    print("my_list.remove(11)",my_list)
    my_list.pop()
    print("my_list.pop()", my_list)
    my_list.pop(3)
    print("my_list.pop(3)", my_list)
    my_list.insert(0, 11)
    print("my_list.insert(0,11)", my_list)
    del my_list[3]
    print("del my_list[3]", my_list)
    my_list.append(3)
    print("my_list.append[3]", my_list)
    my_list.reverse()
    print("my_list_reverse()", my_list)
    my_list.sort()
    print("my_list.sort()",my_list)
    my_list.sort(reverse=True)
    print("my_list.sort(reverse=True)", my_list)
    print("my_list.count(3)", my_list.count(3))
    print("my_list.index(2)", my_list.index(2))
    second_list = my_list.copy()
    print("second_list = my_list.copy()", second_list)
    my_list.clear()
    print("my_list.clear()", my_list)
