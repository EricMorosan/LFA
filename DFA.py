with open("input.txt") as f:
    tranzitii = {}
    qfinal = {}
    n = int(f.readline())
    stari = [int(x) for x in f.readline().strip().split()]
    m = int(f.readline())
    for i in range(m):
        x, y, l = f.readline().strip().split()
        tranzitii[(int(x), l)] = int(y) #rezultatul adaugarii literei l in starea x este y
    q0 = int(f.readline())
    nrF = int(f.readline())
    for final in f.readline().strip().split():
        qfinal[int(final)] = 1 #dictionar pentru starile finale, prefer cautarea in O(1) pentru memorie suplimentara
    nrcuv = int(f.readline())
    g = open("output.txt", 'w')
    for i in range(nrcuv):
        cuvant = f.readline().strip()
        qpartial = q0
        for litera in cuvant:
            if (qpartial, litera) not in tranzitii: #in cazul in care nu e complet
                qpartial = -1 #presupun ca -1 nu e stare pentru a fi consistent, se poate un caracter char daca e -1 stare
                break
            else:
                qpartial = tranzitii[(qpartial, litera)] #daca exista muchia, ajungem intr=o alta stare (unica)

        if qpartial in qfinal:
            print("DA", file=g)
        else:
            print("NU", file=g)
    g.close()
