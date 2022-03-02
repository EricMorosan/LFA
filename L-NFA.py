def lambdaStari(q0):  # sunt nevoit sa aflu toate starile in care se poate afla automatul prin lambda miscari de la starea data
    global tranzitii    # totusi, aceasta functie nu rezolva problema unui ciclu lambda, acestea trebuie eliminate inainte de apelara functiei
    final = set()
    final.add(q0)
    if (q0, 'll') in tranzitii:
        for q in tranzitii[(q0, 'll')]:
            final |= lambdaStari(q)
    return final


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
        qfinal.add(int(final))

    nrcuv = int(f.readline())
    g = open("output.txt", 'w')



    for i in range(nrcuv):
        cuvant = f.readline().strip()

        if len(cuvant) == 0:
            if lambdaStari(q0) & qfinal:
                print("DA", file=g)
                continue
            else:
                print("NU", file=g)
                continue

        qpartial = lambdaStari(q0)
        qpartialAFTER = set()


        for litera in cuvant:
            ok = 0
            for qposibil in qpartial:
                if (qposibil, litera) in tranzitii:
                    qpartialAFTER |= set(tranzitii[(qposibil, litera)])
                    ok = 1
            if ok == 0:
                break
            qpartial.clear()
            for q in qpartialAFTER:
                qpartial |= lambdaStari(q)
            qpartialAFTER.clear()

        if qpartial & qfinal and ok == 1:
            print("DA", file=g)
        else:
            print("NU", file=g)
    g.close()
