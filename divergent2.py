import random
LT = [1, 2, 3, 1]
maxD = [0, 90, 20, 30, 40]  # delete full values except 0
minD = [0, 10, 10, 10]  # delete full values except 0
lL = [0, 20, 30, 10]  # delete full values
uL = [90, 60, 120, 80]  # delete full values
suL = []
pop_no = 4
chromosome = []
initial_pop = []
num_days = 3
demand = []
h = [1, 5, 2, 4]
b = [2, 4, 2, 5]
dict_new = {}
dict_main = {}


def init_pop():
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
    num = 0
    dem1 = []
    dem2 = []
    dem3 = []
    dem4 = []
    num_days = 3
    supp = ["Distributer", "Retailer 1", "Retailer 2", "Retailer 3"]

    # for i in range(4):
    #     if i > 0:
    #         maxD.insert(i, int(input("What is the maximum demand  for " + str(supp[i] + " "))))
    #         minD.insert(i, int(input("What is the minimum demand for " + str(supp[i] + " "))))
    #     LT.insert(i, int(input("Replenishment lead time for " + str(supp[i]) + " ")))
    # h.insert(i,int(input("Holding Cost for" + str(supp[i]) + " ")))
    # b.insert(i,int(input("Backlog Cost for" + str(supp[i]) + " ")))  # for insering remove this comment
    maxD.pop(0)
    # maxD.insert(0, sum(maxD))
    # print(maxD)
    # print(minD)
    # suL.insert(0, LT[0])
    # suL.insert(1, LT[1] + LT[0])
    # suL.insert(2, LT[2] + LT[0])
    # suL.insert(3, LT[3] + LT[0])
    # print(suL)

    # for i in range(4):
    #     lL.insert(i, LT[i] * minD[i])
    #     uL.insert(i, maxD[i] * suL[i])
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
    num_days = int(input("how many num of days "))
    # for i in range(0, num_days):
    #     dem1.append(int(random.randint(minD[1], maxD[1])))
    # for i in range(0, num_days):
    #     dem2.append(int(random.randint(minD[2], maxD[2])))
    # for i in range(0, num_days):
    #     dem3.append(int(random.randint(minD[3], maxD[3])))
    # with open("demand.doc", 'w', encoding='utf-8') as file:
    #      for i in range(0, num_days):
    #          file.write(str(dem[i]) + ", ")  file code
    print(str(initial_pop) + "initial_pop")
    # print(dem1)
    # print(dem2)
    # print(dem3)
    dem1 = [30, 40, 10]
    dem2 = [40, 60, 20]
    dem3 = [40, 30, 50]
    for i in range(num_days):
        dem4.insert(i, dem1[i] + dem2[i] + dem3[i])
    demand.append(dem3)
    demand.append(dem2)
    demand.append(dem1)
    demand.append(dem4)


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
        dummy = list(dict.fromkeys(dummy))
        # print("Ration" + str(Ration))
        print("dummy" + str(dummy))
        j = 0
        for i in dummy:

            o = [m for m, j in enumerate(Ration) if i == j]
            ind.extend(o)
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


init_pop()
l = tscc_calculation([50, 20, 30, 40])
print(l)
