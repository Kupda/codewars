def exp_sum(num):
    diagram = [num]  # [4]
    c = 1
    print([10], c)
    flag = True
    while flag:
        last_num = diagram[0]  # 4
        if last_num != 1:
            diagram.pop(0)
            diagram.insert(0, last_num - 1)
            diagram.append(1)
            c += 1
            print(diagram, c)
            flag1 = True
            index = -1
            while flag1:
                try:
                    if diagram[index] > 1:
                        diagram[index] -= 1
                        try:
                            diagram[index+1] += 1
                        except:
                            diagram.append(1)
                        c += 1
                        print(diagram, c)
                except:
                    pass
                index += 1
                if len(diagram) > index:
                    index = 0
        else:
            flag = False

    return c

print(exp_sum(5))

# переделать крч надо все =(
