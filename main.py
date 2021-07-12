import math
def merging(left, right):
    """this is will combine the two list"""
    new_list = []
    while (min(len(left), len(right))):
        if (left[0] > right[0]):
            to_insert = right.pop(0)
            new_list.append(to_insert)
        elif (left[0] <= right[0]):
            to_insert = left.pop(0)
            new_list.append(to_insert)
    if (len(left) > 0):
        for i in left:
            new_list.append(i)
    if (len(right) > 0):
        for i in right:
            new_list.append(i)
    return (new_list)


def MergeSort(data):
    """this is where the recursive decsions will happen"""
    new_list = []
    if (len(data) == 1):
        new_list = data
    else:
        left = MergeSort(data[:math.floor(len(data) / 2)])
        right = MergeSort(data[math.floor(len(data) / 2):])
        new_list = merging(left, right)

    return (new_list)


if __name__ == '__main__':
    array = [3,2,8,3,6,1,5]
    new_list = MergeSort(array)
    print(new_list)