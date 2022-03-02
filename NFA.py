with open("input.txt") as f:
    tranzitii = {}
    qfinal = set()
    n = int(f.readline())
    stari = [int(x) for x in f.readline().strip().split()]
    m = int(f.readline())

    for i in range(m):
        x, y, l = f.readline().strip().split()
        if (int(x), l) not in tranzitii:
            tranzitii[(int(x), l)] = [int(y), ]
        else:
            tranzitii[(int(x), l)].append(int(y))

    q0 = int(f.readline())
    nrF = int(f.readline())

    for final in f.readline().strip().split():
        qfinal.add(int(final))  # este mai util setul pentru a face operatie de intersectie

    nrcuv = int(f.readline())
    g = open("output.txt", 'w')
    for i in range(nrcuv):
        cuvant = f.readline().strip()

        if len(cuvant) == 0:   # izolez cazul in care lambda e solutie
            if q0 in qfinal:
                print("DA", file=g)
                continue
            else:
                print("NU", file=g)
                continue

        qpartial = set()
        qpartialAFTER = set()
        qpartial.add(q0)  # de data asta, starea in care se afla automatul nu este unica in orice moment
        for litera in cuvant:
            ok = 0
            for qposibil in qpartial:
                if (qposibil, litera) in tranzitii:
                    qpartialAFTER |= set(tranzitii[(qposibil, litera)])  # pastrez toate starile in care automatul se poate afla dupa ce adaugam o litera
                    ok = 1
            if ok == 0:
                break
            qpartial = qpartialAFTER.copy()
            qpartialAFTER.clear()

        if qpartial & qfinal and ok == 1:
            print("DA", file=g)
        else:
            print("NU", file=g)
    g.close()
