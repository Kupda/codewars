def exp_sum(num):
    turns = [num]
    flag = True
    c = []
    index = 0
    while flag:
        try:
            if turns[index] > 1:
                turns[index] -= 1
                try:
                    turns[index+1] += 1
                    index += 1
                except:
                    turns.append(1)
                    index = 0
                if sorted(turns, reverse=True) not in c:
                    c.append(sorted(turns, reverse=True))
                    print(sorted(turns, reverse=True))
            else:
                check = 0
                for i in turns:
                    if i != 1:
                        check += 1
                if check == 0:
                    flag = False
        except:
            index = 0
    return len(c)+1


print(exp_sum(10))

