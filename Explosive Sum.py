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
        last_num = diagram[0]  # 4
        if last_num != 1:
            diagram.pop(0)
            diagram.append(last_num - 1)
            diagram.append(1)
            c += 1
            print(diagram)
            for index in range(0, len(diagram)):
                if diagram[index] > 1:
                    diagram[index] -= 1
                    try:
                        diagram[index+1] += 1
                    except:
                        diagram.append(1)
                    print(diagram)
                    c += 1
                    diagram = sorted(diagram, reverse=True)
                    print(diagram, "сортировка")

        else:
            flag = False

    return c

print(exp_sum(10))

