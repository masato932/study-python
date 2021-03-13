l1 = ['大山', '佐藤', '大山', '佐藤', '山下', '平野', '山下', '平野']
l2 = ['大山', '佐藤']
result = list(set(l1) - set(l2))
print(result)

l1 = ['大山', '佐藤', '大山', '佐藤', '山下', '平野', '山下', '平野']
l2 = ['大山', '佐藤']
result = list(filter(lambda x: x not in l2, l1))
print(result)

def list_difference(list1, list2):
    result = list1.copy()
    for value in list2:
        if value in result:
            result.remove(value)

    return result

l1 = ['大山', '佐藤', '大山', '佐藤', '山下', '平野', '山下', '平野']
l2 = ['大山', '佐藤']
result = list_difference(l1, l2)
print(result)