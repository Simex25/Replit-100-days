def addTwoNums(list1, list2):
    carry_over = 0
    empty = []
    for i in range(0, len(list1)):
        new_num = list1[i] + list2[i]
        if new_num > 9:
            num = new_num + carry_over
            carry_over = num - 9
            rem = new_num % 2
            if rem == 0:
                empty.append(rem)
        elif carry_over < 0 and carry_over <= 9:
            empty.append(new_num)
        else:
            num = new_num + carry_over
            empty.append(num)
    return empty, carry_over


print(addTwoNums([2, 4, 3], [5, 6, 4]))
