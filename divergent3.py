import random
LT = []
maxD = [0, ]  # delete full values except 0
minD = [0, ]  # delete full values except 0
lL = []  # delete full values
uL = []  # delete full values
suL = []

pop_no = 4
chromosome = []
initial_pop = []
num_days = 3
demand = []
h = []
b = []
dict_new = {}
dict_main = {}
initial_pop = []
cross_over_selection = []
cross_over_population = []
inter_pop = []
fk_dict = {}
mut_fk_dict = {}
dem1 = []
dem2 = []
dem3 = []
dem4 = []
pop_first = []
fk_value = []
mut_fk_value = []
sort_dict = {}
pop_first1 = []
gif = []
complete_fk = []
mut_fk_value = []
fk_value = []

sort_dict = []
sorted_dict = []
child_chr = []
cross_over_selection = []
cross_over_population = []
pop_first = []
supp = ["Distributer", "Retailer 1", "Retailer 2", "Retailer 3"]
for i in range(4):
    if i > 0:
        maxD.insert(i, int(input("What is the maximum demand  for " + str(supp[i] + " "))))
        minD.insert(i, int(input("What is the minimum demand for " + str(supp[i] + " "))))
    LT.insert(i, int(input("Replenishment lead time for " + str(supp[i]) + " ")))
    h.insert(i, int(input("Holding Cost for" + str(supp[i]) + " ")))
    b.insert(i, int(input("Backlog Cost for" + str(supp[i]) + " ")))
num_days = int(input("how many num of days "))

for i in range(0, num_days):
    dem1.append(int(random.randint(minD[1], maxD[1])))
for i in range(0, num_days):
    dem2.append(int(random.randint(minD[2], maxD[2])))
for i in range(0, num_days):
    dem3.append(int(random.randint(minD[3], maxD[3])))

for i in range(num_days):
    dem4.insert(i, dem1[i] + dem2[i] + dem3[i])
demand.append(dem3)
demand.append(dem2)
demand.append(dem1)
demand.append(dem4)


def init_pop():
    global dem1
    global dem2
    global dem3
    global dem4
    global maxD
    global minD
    global LT
    global suL
    global b
    global h
    global lL
    global uL
    global suL
    global demand
    global num_days
    num = 0

    # for insering remove this comment
    maxD.pop(0)
    maxD.insert(0, sum(maxD))
    # print(maxD)
    # print(minD)
    suL.insert(0, LT[0])
    suL.insert(1, LT[1] + LT[0])
    suL.insert(2, LT[2] + LT[0])
    suL.insert(3, LT[3] + LT[0])
    # print(suL)

    for i in range(4):
        lL.insert(i, LT[i] * minD[i])
        uL.insert(i, maxD[i] * suL[i])
    # print(str(lL) + "lower limit")
    # print(str(uL) + "upper limit")

    for j in range(pop_no):
        chromosome = []

        for i in range(0, 4):

            # random.seed(num)
            chromosome.append(int(random.randint(lL[i], uL[i])))
            num = num + 1
            # print(chromosome)
        initial_pop.insert(j, chromosome)
    print(str(initial_pop) + "initial_pop")

    # with open("demand.doc", 'w', encoding='utf-8') as file:
    #     for i in range(0, num_days):
    #         file.write(str(dem[i]) + ", ")  # file code
    print(str(initial_pop) + "initial_pop")
    # print(dem1)
    # print(dem2)
    # print(dem3)
    # dem1 = [30, 40, 10]
    # dem2 = [40, 60, 20]
    # dem3 = [40, 30, 50]


def tscc_calculation(s):

    Ie = [[], [], [], []]
    global demand
    global num_days
    global dem
    global h
    global b
    global dict_main
    global new_fk
    global dict_new
    global LT
    Ration = []
    Ration2 = []
    ind = []
    ind2 = []
    dummy = []
    dummy2 = []
    RationOIe = []
    QS1 = [[], [], [], []]
    demand2 = [[], [], [], []]
    # print(dem)
    new_fk = 0
    for i in range(0, 4):
        Ie[i].insert(0, int(s[3 - i]))
    # for i in range(0, num_days):
    #     demand[0].insert(i, int(dem[i]))

    OIe = [[0], [0], [0], [0]]
    B = [[0], [0], [0], [0]]
    # Ie = [[60], [50], [40], [30]]
    QS2 = [[], [], [], []]
    QS1 = [[0], [0], [0], [0]]
    Ib = [[], [], [], []]
    OIb = [[], [], [], []]
    j = 0

    # demand = [[70, 60, 40, 80], [], [], [], []]
    for t in range(0, int(num_days)):
        for i in range(0, 4):
            k = t + 1 - LT[i]
            if k <= 0:
                temp = 0

            else:
                temp = abs(k)

            OIb[i].insert(t, int(OIe[i][t]) - int(QS1[i][temp]))

            Ib[i].insert(t, int((Ie[i][t]) + int(QS1[i][temp])))
            if (int(Ib[i][t]) - int(B[i][t]) - int(demand[i][t])) > 0:
                Ie[i].insert(t + 1, int(Ib[i][t] - int(B[i][t]) - int(demand[i][t])))
                B[i].insert(t + 1, 0)
            else:
                B[i].insert(t + 1, abs(int(Ib[i][t] - int(B[i][t]) - int(demand[i][t]))))
                Ie[i].insert(t + 1, 0)
            QS2[i].insert(t, int(Ib[i][t]) - int(Ie[i][t + 1]))
            demand2[i].insert(t, max(0, int(s[3 - i]) + int(B[i][t + 1]) - int(Ie[i][t + 1]) - int(OIb[i][t])))
            OIe[i].insert(t + 1, int(OIb[i][t]) + int(demand2[i][t]))
            RationOIe.insert(i, int(OIe[i][t + 1]))
        print("OIe" + str(OIe))
        print("demand2" + str(demand2))
        print("OIb" + str(OIb))
        print("B" + str(B))
        print("Ie" + str(Ie))
        print("Ib" + str(Ib))
        print(RationOIe)
        RationOIe.pop(3)
        sumOI = OIe[0][t + 1] + OIe[1][t + 1] + OIe[2][t + 1]
        for i in range(3):
            Ration.insert(i, OIe[i][t + 1] / sumOI)
        print("Ration" + str(Ration))
        dummy = Ration

        dummy = sorted(Ration)
        dummy.reverse()
        # print("Ration" + str(Ration))
        print("dummy" + str(dummy))
        j = 0
        dummy = list(dict.fromkeys(dummy))

        for i in dummy:

            o = [m for m, j in enumerate(Ration) if i == j]
            ind.extend(o)
        print(ind)

        f = ind[0]
        print("ind" + str(ind))

        print((dummy[0]) * (Ib[3][t]))
        print((OIe[f][t + 1]))
        g = round(min(((dummy[0]) * (Ib[3][t])), int(OIe[f][t + 1])))
        print(g)

        QS1[int(ind[0])].insert(t + 1, g)
        RationOIe.pop(ind[0])

        for i in range(2):
            Ration2.insert(i, RationOIe[i] / sum(RationOIe))
        dummy2 = Ration2
        dummy2.sort()
        j = 0
        dummy2.reverse()
        print(dummy2)
        print(Ration2)
        for i in dummy2:
            ind2.insert(j, Ration2.index(i))
            j = j + 1
        f2 = ind[1]
        f3 = ind[2]
        QS1[f2].insert(t + 1, round(min(dummy2[0] * (Ib[3][t] - QS1[f][t + 1]), OIe[f][t + 1])))
        RationOIe.pop(ind2[0])
        print(ind[0])
        print(dummy)
        print(str(Ib) + "IB")
        print(OIe)
        print(OIe[f][t + 1])
        print(t)
        QS1[f3].insert(t + 1, round(min(Ib[3][t] - (QS1[f2][t + 1] + QS1[f][t + 1]), OIe[f3][t + 1])))
        QS1[3].insert(t + 1, demand2[3][t])
        Ration2 = []
        Ration = []
        RationOIe = []
        ind = []
        print("QS1" + str(QS1))
    THC = 0
    TSC = 0

    for i in range(0, 4):
        for j in range(0, num_days):

            THC = THC + h[i] * Ie[i][j + 1]
    for i in range(0, 4):
        for j in range(0, num_days):

            TSC = TSC + b[i] * B[i][j + 1]

    TSCC = THC + TSC
    print("TSCC " + str(TSCC))
    fk = 1 / (1 + TSCC)
    new_fk = fk
    # print(str(fk) + "fk")
    OIe = []
    B = []
    QS2 = []
    QS1 = []
    Ib = []
    OIb = []
    LT = [2, 3, 1, 1]
    OIe = [[0], [0], [0], [0]]
    B = [[0], [0], [0], [0]]
    # Ie = [[60], [50], [40], [30]]
    QS2 = [[], [], [], [], []]
    QS1 = [[0], [0], [0], [0], [0]]
    Ib = [[], [], [], []]
    OIb = [[], [], [], []]
    # print(str(s) + "str")
    # print(str(fk) + "fk")

    dict_new = {new_fk: s}
    dict_main.update(dict_new)
    # print(str(dict_main) + "main dict")
    dict_new = {}
    s = []
    TSC = 0
    THC = 0
    TSCC = 0

    return fk


def selection(fk):
    global fk_value
    p = []
    pc = [0]
    temp = 0
    x = sum(fk_value)
    # print(x)
# print(0.01 / x)
    for i in range(0, 4):
        p.insert(i, round(fk_value[i] / x, 8))
    # print(p)
    for j in range(0, 4):
        pc.insert(j + 1, round(temp + p[j], 8))
        temp = pc[j + 1]
    # print(pc)

    l = random.uniform(0, 1)
    # print(l)
    for j in range(0, 4):
        if pc[j] < l <= pc[j + 1]:
            return initial_pop[j]


def cross_over(chromosome5, chromosome6):

    # global chromosome20
    # global chromosome30
    # chromosome20 = chromosome5
    # chromosome30 = chromosome6

    # cr = random.randint(1, 3)
    # print(str(cr) + "cr")
    # temp1 = (chromosome20[4 - cr:4])
    # temp2 = (chromosome30[4 - cr:4])
    # # print(temp2)
    # # print(temp1)
    # del (chromosome20[4 - cr:4])
    # del(chromosome30[4 - cr:4])
    # # print(chromosome5)
    # # print(chromosome6)
    # chromosome20.extend(temp2)
    # chromosome30.extend(temp1)
    # global gif
    # print(str(chromosome20) + "chromosome5")
    # print(str(chromosome30) + "chromosome6")
    # gif.append(chromosome20)
    # gif.append(chromosome30)
    # temp1 = []
    # temp2 = []
    # chromosome20 = []
    # chromosome30 = []
    # print(str(gif) + "gif")
    # return gif
    global chromosome20
    global chromosome30

    chromosome20 = []
    chromosome30 = []
    temp1 = []
    temp2 = []
    cr = random.randint(1, 3)

    print(cr)

    for i in range(0, cr):
        chromosome20.insert(i, chromosome5[i])

        chromosome30.insert(i, chromosome6[i])

    for i in range(cr, 4):

        temp1.insert(i - cr, chromosome5[i])
        temp2.insert(i - cr, chromosome6[i])

        chromosome20.insert(i, temp2[i - cr])
        chromosome30.insert(i, temp1[i - cr])
    global gif
    gif.append(chromosome20)
    gif.append(chromosome30)
    print(str(gif) + "gif")
    return gif


def mutation(chromosome100):

    for i in range(4):
        un = random.uniform(0, 1)
        u = random.uniform(0, 1)
        print(str(u) + "u")
        print(str(un) + "un")
        if u <= 0.05:

            z = chromosome100[i] * 0.8 + chromosome100[i] * 2 * 0.2 * un
            z = z // 1
            chromosome100.pop(i)
            chromosome100.insert(i, int(z))

        else:
            pass
    return chromosome100


def generation(chr_gen):
    global complete_fk
    global fk_value
    global cross_over_population
    global inter_pop
    global o
    global sort_dict
    global sorted_dict
    global cross_over_selection
    global final_population
    global pop_first
    global pop_first1
    global mut_fk_value
    global man
    global gif
    mut_fk_value = []
    fk_value = []
    inter_pop = []
    sort_dict = []
    sorted_dict = []
    child_chr = []
    cross_over_selection = []
    cross_over_population = []

    pop_first = []
    # pdb.set_trace()
    #
    #
    #
    #
    for i in range(0, 4):

        fk_value.append(tscc_calculation(pop_first1[i]))
        print(str(fk_value) + "fk_value")

    selected = False
    i = 0
    while not selected:

        child_chr = selection(fk_value)

        cross_over_selection.insert(i, child_chr)
        if i > 0:

            if cross_over_selection[i - 1] == cross_over_selection[i]:
                cross_over_selection.pop(i)

            else:
                i = i + 1
        if i == 0:
            i = i + 1
        if len(cross_over_selection) == 4:
            selected = True
        print(i)
    print("cross_over_selection" + str(cross_over_selection))
    for i in range(4):
        if i % 2 == 0:
            p = random.uniform(0, 1)

            cross_over_rate = 0.7
            # changed cross over rate
            if p <= cross_over_rate:

                man = (cross_over(cross_over_selection[i], cross_over_selection[i + 1]))

                cross_over_population.append(man[0])
                cross_over_population.append(man[1])
                man = 0
                gif = []
                print(man)

            else:
                cross_over_population.append(cross_over_selection[i])
                cross_over_population.append(cross_over_selection[i + 1])
        else:
            pass
    print(str(cross_over_population) + "cross_over_population")
    # pdb.set_trace()
    for i in range(0, 4):
        o = mutation(cross_over_population[i])
        print(o)
        inter_pop.insert(i, o)
    print(str(inter_pop) + "inter_pop")
    for i in range(0, 4):

        mut_fk_value.insert(i, tscc_calculation(inter_pop[i]))
    print(str(mut_fk_value) + "mut_fk_value")

    complete_fk.extend(fk_value)
    complete_fk.extend(mut_fk_value)
    print(str(complete_fk) + "complete_fk")
    complete_fk.sort()
    print(str(complete_fk) + "complete_fk")

    for key in (complete_fk):
        pop_first.append(dict_main[key])

    complete_fk = []
    print(str(pop_first) + "pop_first")
    pop_first1 = []
    for i in range(7):
        if pop_first[i] == pop_first[i + 1]:
            pop_first.pop(i + 1)
        else:
            pass
    init_pop()
    i = 0
    while len(pop_first) != 4:
        pop_first.extend(initial_pop[i])
        i = i + 1
    initial_pop = []
    for i in range(4, 8):
        pop_first1.insert(4 - i, pop_first[i])
    print(str(pop_first1) + "pop_first1")
    print("2nd gen" + str(pop_first1))
    return pop_first1


def main():
    init_pop()
    global complete_fk
    global fk_value
    global cross_over_population
    global inter_pop
    global o
    global sort_dict
    global sorted_dict
    global cross_over_selection
    global final_population
    global pop_first
    global pop_first1
    global mut_fk_value
    global man
    global gif
    global initial_pop
    print("initial_pop" + str(initial_pop))
    for i in range(0, 4):

        fk_value.append(tscc_calculation(initial_pop[i]))
        print(fk_value)

    selected = False
    i = 0
    while not selected:

        child_chr = selection(fk_value)

        cross_over_selection.insert(i, child_chr)
        if i > 0:

            if cross_over_selection[i - 1] == cross_over_selection[i]:
                cross_over_selection.pop(i)

            else:
                i = i + 1
        if i == 0:
            i = i + 1
        if len(cross_over_selection) == 4:
            selected = True
        print(i)
    print("cross_over_selection" + str(cross_over_selection))
    for i in range(4):
        if i % 2 == 0:
            p = random.uniform(0, 1)

            cross_over_rate = 0.7
            # changed cross over rate
            if p <= cross_over_rate:

                man = (cross_over(cross_over_selection[i], cross_over_selection[i + 1]))
                cross_over_population.append(man[0])
                cross_over_population.append(man[1])
                man = 0
                gif = []
                print(str(man) + "man")

            else:
                cross_over_population.append(cross_over_selection[i])
                cross_over_population.append(cross_over_selection[i + 1])
        else:
            pass
    print(str(cross_over_population) + "cross_over_population")
    # pdb.set_trace()
    for i in range(0, 4):
        o = mutation(cross_over_population[i])
        print(o)
        inter_pop.insert(i, o)
    print(str(inter_pop) + "inter_pop")
    for i in range(0, 4):
        # pdb.set_trace()
        mut_fk_value.insert(i, tscc_calculation(inter_pop[i]))
        print(mut_fk_value)

    complete_fk.extend(fk_value)
    complete_fk.extend(mut_fk_value)

    complete_fk.sort()

    for key in (complete_fk):
        pop_first.append(dict_main[key])
    print(str(pop_first) + "pop_first")
    init_pop()
    for i in range(7):
        if pop_first[i] == pop_first[i + 1]:
            pop_first.pop(i + 1)
        else:
            pass
    init_pop()
    i = 0
    while len(pop_first) != 4:
        pop_first.extend(initial_pop[i])
        i = i + 1
    chromosome = []
    for i in range(4, 8):
        pop_first1.insert(4 - i, pop_first[i])
    print(str(pop_first1) + "pop_first1")
    # from here
    complete_fk = []
    mut_fk_value = []
    fk_value = []
    inter_pop = []
    sort_dict = []
    sorted_dict = []
    child_chr = []
    cross_over_selection = []
    cross_over_population = []
    pop_first = []

    for i in range(10):
        generation(pop_first1)
        print("gen no = " + str(3 + i))
    print(pop_first1[0])


main()
