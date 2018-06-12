def array_search(A: list, N: int, x: int):
    """ Find element x in list A
    take: A - list, N - len(list), x - necessary element
    return element's index
    or -1
    """
    for i in range(N):
        if A[i] == x:
            print(i)
            return i
        else:
            print(-1)
            return -1


def test_array_search():
    A1 = [i for i in range(10)]
    m = array_search(A1, len(A1), 12)
    if m == -1:
        print("Test1 - passed")
    else:
        print("Test2 - failed")


array_search([1, 2, 3, 4, 5], 5, 3)
test_array_search()