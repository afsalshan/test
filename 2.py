import random
import pdb
final_population = []
sorted_dict = []
dict_main = {}
f = []
global maxD
global minD
global LT
global sLT
global b
global h
o = 0
new_fk = 0
man = 0
gif = []
h = []
b = []
fk_dict = {}
mut_fk_dict = {}
complete_fk = []
chromosome30 = []
chromosome20 = []

pop_first = []
dem = []
demand = [[], [], [], [], []]
num_days = 0
chromosome1 = []
cross_over_selection = []
cross_over_population = []
inter_pop = []

fk_value = []
mut_fk_value = []
sort_dict = {}
pop_first1 = []
uL = []
lL = []
LT = []
sLT = []


def init_pop():
    global maxD
    global minD
    global LT
    global sLT
    global b
    global h
    num = 0
    maxD = int(input("What is the maximum demand "))
    minD = int(input("What is the minimum demand "))

    supp = ["Supplier", "Manufacturer", "Distributer", "Retailer"]
    for i in range(4):
        LT.append(int(input("Replenishment lead time for " + str(supp[i]) + " ")))  # for insering
    for i in range(4, 0, -1):  # sum of lead time
        sum = 0
        for j in range(i, 5, 1):
            sum = sum + int(LT[4 - j])
        sLT.append(int(sum))
    for i in range(4):  # holding and backlog cost
        h.append(int(input("Holding Cost for" + str(supp[3 - i]) + " ")))
        b.append(int(input("Backlog Cost for" + str(supp[3 - i]) + " ")))

    global chromosome1
    global dem
    global num_days
    for i in range(0, 4):
        uL.append(int(maxD * sLT[i]))
        lL.append(int(minD * LT[i]))

    for j in range(0, 4):
        chromosome = []

        for i in range(0, 4):

            # random.seed(num)
            chromosome.append(int(random.randint(lL[i], uL[i])))
            num = num + 1
        # print(chromosome)
        chromosome1.insert(j, chromosome)
    num_days = int(input("how many num of days "))
    # print(chromosome1)
    for i in range(0, num_days):
        dem.append(int(random.randint(minD, maxD)))
    # print(dem)
    with open("demand.doc", 'w', encoding='utf-8') as file:
        for i in range(0, num_days):
            file.write(str(dem[i]) + ", ")
    for i in range(0, num_days):
        demand[0].insert(i, int(dem[i]))


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
    # print(dem)
    new_fk = 0
    for i in range(0, 4):
        Ie[i].insert(0, int(s[3 - i]))
    # for i in range(0, num_days):
    #     demand[0].insert(i, int(dem[i]))

    OIe = [[0], [0], [0], [0]]
    B = [[0], [0], [0], [0]]
    # Ie = [[60], [50], [40], [30]]
    QS2 = [[], [], [], [], []]
    QS1 = [[0], [0], [0], [0], [0]]
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
            demand[i + 1].insert(t, max(0, int(s[3 - i]) + int(B[i][t + 1]) - int(Ie[i][t + 1]) - int(OIb[i][t])))
            OIe[i].insert(t + 1, int(OIb[i][t]) + int(demand[i + 1][t]))
            if i == 3:

                QS2[4].insert(t, int(demand[4][t]))
        for j in range(0, 4):

            QS1[j].insert(t + 1, int(QS2[j + 1][t]))

    THC = 0
    TSC = 0

    for i in range(0, 4):
        for j in range(0, num_days):

            THC = THC + h[i] * Ie[i][j + 1]
    for i in range(0, 4):
        for j in range(0, num_days):

            TSC = TSC + b[i] * B[i][j + 1]

    TSCC = THC + TSC
    # print(TSCC)
    fk = 1 / (1 + TSCC)
    new_fk = fk
    # print(str(fk) + "fk")
    OIe = []
    B = []
    QS2 = []
    QS1 = []
    Ib = []
    OIb = []
    LT = [2, 2, 2, 2]
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
            return chromosome1[j]


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

    # print(cr)

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
    # print(str(gif) + "gif")
    return gif


def mutation(chromosome100):

    for i in range(4):
        un = random.uniform(0, 1)
        u = random.uniform(0, 1)
        # print(str(u) + "u")
        # print(str(un)+"un")
        if u <= 0.05:

            z = chromosome100[i] * 0.8 + chromosome100[i] * 2 * 0.2 * un
            z = z // 1
            chromosome100.pop(i)
            chromosome100.insert(i, int(z))

        else:
            pass
    return chromosome100


def generation(chr_gen):
    chromosome98 = []
    chromosome123 = []
    global lL
    global uL
    global maxD
    global minD
    global LT
    global sLT
    global b
    global h
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
        # print(str(fk_value) + "fk_value")

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
        # print(i)
    # print("cross_over_selection" + str(cross_over_selection))
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
                # print(man)

            else:
                cross_over_population.append(cross_over_selection[i])
                cross_over_population.append(cross_over_selection[i + 1])
        else:
            pass
    # print(str(cross_over_population) + "cross_over_population")
    # pdb.set_trace()
    for i in range(0, 4):
        o = mutation(cross_over_population[i])
        # print(o)
        inter_pop.insert(i, o)
    # print(str(inter_pop) + "inter_pop")
    for i in range(0, 4):

        mut_fk_value.insert(i, tscc_calculation(inter_pop[i]))
    # print(str(mut_fk_value) + "mut_fk_value")

    complete_fk.extend(fk_value)
    complete_fk.extend(mut_fk_value)
    # print(str(complete_fk) + "complete_fk")
    complete_fk.sort()
    # print(str(complete_fk) + "complete_fk")

    for key in (complete_fk):
        pop_first.append(dict_main[key])

    complete_fk = []
    # print(str(pop_first) + "pop_first")
    pop_first1 = []
    dup = True
    i = 0
    while dup:
        if pop_first[i] == pop_first[i + 1]:
            pop_first.pop(i + 1)
        else:
            i = i + 1
            pass
        if i + 1 == len(pop_first):
            dup = False

    # print(len(pop_first))

    i = 0
    while len(pop_first) < 4:
        for j in range(0, 4):
            chromosome123 = []
        for i in range(0, 4):

            # random.seed(num)
            chromosome123.append(int(random.randint(lL[i], uL[i])))
            # num = num + 1
        # print(chromosome124)
        chromosome98.insert(j, chromosome123)
        pop_first.append(chromosome98[i])

        print("added here")
        i = i + 1
    chromosome123 = []
    chromosome98 = []
    pop_first.reverse()
    for i in range(0, 4):
        pop_first1.insert(i, pop_first[i])
    # print(str(pop_first1) + "pop_first1")
    # print("2nd gen" + str(pop_first1))
    pop_first = []
    return pop_first1


def main():
    global lL
    global uL
    global maxD
    global minD
    global LT
    global sLT
    global b
    global h
    chromosome99 = []
    chromosome124 = []
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
    # print("chromosome1" + str(chromosome1))
    for i in range(0, 4):

        fk_value.append(tscc_calculation(chromosome1[i]))
        # print(fk_value)

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
        # print(i)
    # print("cross_over_selection" + str(cross_over_selection))
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
                # print(str(man) + "man")

            else:
                cross_over_population.append(cross_over_selection[i])
                cross_over_population.append(cross_over_selection[i + 1])
        else:
            pass
    # print(str(cross_over_population) + "cross_over_population")
    # pdb.set_trace()
    for i in range(0, 4):
        o = mutation(cross_over_population[i])
        # print(o)
        inter_pop.insert(i, o)
    # print(str(inter_pop) + "inter_pop")
    for i in range(0, 4):
        # pdb.set_trace()
        mut_fk_value.insert(i, tscc_calculation(inter_pop[i]))
        # print(mut_fk_value)

    complete_fk.extend(fk_value)
    complete_fk.extend(mut_fk_value)

    complete_fk.sort()

    for key in (complete_fk):
        pop_first.append(dict_main[key])
    # print(str(pop_first) + "pop_first")
    num = 0

    # print(str(chromosome99) + "chr 99")
    # print(len(pop_first))
    dup = True
    i = 0
    while dup:
        if pop_first[i] == pop_first[i + 1]:
            pop_first.pop(i + 1)
            # print(str(pop_first) + "pop_first")
        else:
            # print(str(pop_first) + "pop_first")
            i = i + 1
        if i + 1 == len(pop_first):
            dup = False

    # print(str(pop_first1) + "pop_first1")
    # from here
    i = 0
    while len(pop_first) < 4:
        for j in range(0, 4):
            chromosome124 = []
        for i in range(0, 4):

            # random.seed(num)
            chromosome124.append(int(random.randint(lL[i], uL[i])))
            # num = num + 1
        # print(chromosome124)
        chromosome99.insert(j, chromosome124)
        pop_first.append(chromosome99[i])

        print("added here")
        i = i + 1
    pop_first.reverse()
    for i in range(0, 4):
        pop_first1.insert(i, pop_first[i])
    chromosome99 = []
    chromosome124 = []

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

    for i in range(350):
        generation(pop_first1)
        print("gen no = " + str(2 + i))
    print(pop_first1[0])


main()
# print(dict_main)
# tscc_calculation(chromosome2)
