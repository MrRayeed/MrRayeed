def test(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[1:]
    return result


students = [[1,'jean castro','V'], [2,'lula powell','V'], [3,'brian howell','VI'], [4,'lynne foster','VII']]
print("\noriginal list of lists")
print(students)
print("\nconverted list to a dictionary")
print(test(students))