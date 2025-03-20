def exp_sum(num):
    c = [[num]]
    fitst_combs = []
    if num % 2 == 0:
        for n in range(num-1, int(num/2)-1, -1):
            fitst_combs.append([n, num-n])
    else:
        for n in range(num-1, int(num//2), -1):
            fitst_combs.append([n, num-n])
    for comb in fitst_combs:
        c.append(comb)

    for comb in fitst_combs:
        comb1 = sorted(comb, reverse=True)
        for i in range(0, len(comb1)):
            if comb1[i] != 1:
                comb1[i] -= 1
                comb1.append(1)
                c.append(comb1)


    return c

print(exp_sum(6))

