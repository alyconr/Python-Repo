def add_one_at_a_time(lst, elem):
    try:
        if elem not in lst:
            lst.append(elem)
            return lst
        else:
            raise ValueError("Element already exists in the list.")
    except Exception as e:
        return e

try:
    print(add_one_at_a_time([1, 2, 3], 3))
except Exception as e:
    print(e)






