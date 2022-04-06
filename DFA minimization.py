with open("input.txt") as f:
    tranzitii = {}
    qfinal = set()
    n = int(f.readline()) #nr de stari
    stari = [int(x) for x in f.readline().strip().split()] #starile
    alfabet = [x for x in f.readline().strip().split()] #literele din alfabet
    m = int(f.readline()) #nr de tranzitii

    for i in range(m):
        x, y, l = f.readline().strip().split() # stare stare litera
        tranzitii[(int(x), l)] = int(y)


    q0 = int(f.readline()) #starea initiala
    nrF = int(f.readline()) #nr de stari finale

    for final in f.readline().strip().split():
        qfinal.add(int(final)) #starile finale
P = []
Pfinal = []
Pfinal.append(list(qfinal))
Pfinal.append(list(set(stari) - qfinal))
partial1 = []
partial2 = []
while P != Pfinal:
    P = Pfinal.copy()
    Pfinal.clear()
    for partitie in P:
        if len(partitie) == 1:
            Pfinal.append(partitie.copy())
            continue
        stare1 = partitie[0]
        partial1 = [stare1]
        partial2.clear()
        for i in range(1, len(partitie)):
            stare2 = partitie[i]
            ok = 1
            for litera in alfabet:
                for multime in P:
                    # print(litera,stare1,tranzitii[(stare1, litera)],stare2,tranzitii[(stare2, litera)])
                    if tranzitii[(stare1, litera)] in multime and tranzitii[(stare2, litera)] not in multime:
                        ok = 0
            if ok == 1:
                partial1.append(stare2)
            else:
                partial2.append(stare2)
        if partial1:
            Pfinal.append(partial1.copy())
        if partial2:
            Pfinal.append(partial2.copy())


nDFA = len(P)
stariDFA = [''.join(str(x) for x in y) for y in P]
alfabetDFA = alfabet.copy()
qfinalDFA = set()
for stare in stariDFA:
    for singular in stare:
        if int(singular) == q0:
            q0DFA = stare
        if int(singular) in qfinal:
            qfinalDFA.add(stare)
nrFDFA = len(qfinalDFA)

tranzitiiDFA = {}
for partitie in P:
    ales = partitie[0]
    for litera in alfabet:
        rezultat = tranzitii[(ales, litera)]
        for partitie2 in P:
            if rezultat in partitie2:
                tranzitiiDFA[(''.join(str(x) for x in partitie), litera)] = ''.join(str(x) for x in partitie2)
mDFA = len(tranzitiiDFA)


with open("output.txt", 'w') as g:
    print("Numarul de stari este:", nDFA, file=g)
    print("Starile sunt:", *stariDFA, file=g)
    print("Alfabetul este:", *alfabetDFA, file=g)
    print(f"Exista {mDFA} tranzitii:", file=g)
    for cheie in tranzitiiDFA:
        print(*cheie, tranzitiiDFA[cheie], file=g)
    print("Starea initiala este:", q0DFA, file=g)
    print(f"Exista {nrFDFA} stari finale:", file=g)
    for final in qfinalDFA:
        print(final, file=g)




