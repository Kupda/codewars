# https://www.codewars.com/kata/52ec24228a515e620b0005ef

# def exp_sum(num):
#     terms = []
#     flag = True
#     c = 1
#     while flag:
#         if num > 1:
#             terms = [1, num-1]
#             c += 1
#             print(terms)
#             while flag:
#                 if terms[-1] > 1:
#                     last_num = terms[-1]
#                     terms.pop(-1)
#                     terms.append(1)
#                     terms.append(last_num-1)
#                     c += 1
#                     print(terms)
#                 else:
#                     flag = False
#         else:
#             flag = False
#     return c
#
# number = 5
# print([number])
# print(exp_sum(number))


def exp_sum(num):
    diagram = [num]  # [4]
    c = 1
    flag = True
    while flag:
        last_num = diagram[-1]  # 4
        if last_num != 1:
            diagram.pop(-1)
            diagram.append(1)
            diagram.append(last_num-1)
            c += 1
            print(diagram)
            for index in range(len(diagram)-1, 0-1, -1):
                if diagram[index] > 1:
                    # [1, 3]
                    last_num = diagram[-1]  # 3
                    diagram[-2] += 1
                    last_num -= 1



        else:
            flag = False

    return c

print(exp_sum(4))

