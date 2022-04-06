with open("input.txt") as f:
    tranzitii = {}
    qfinal = set()
    n = int(f.readline()) #nr de stari
    stari = [int(x) for x in f.readline().strip().split()] #starile
    alfabet = [x for x in f.readline().strip().split()] #literele din alfabet
    m = int(f.readline()) #nr de tranzitii

    for i in range(m):
        x, y, l = f.readline().strip().split() # stare stare litera
        if (int(x), l) not in tranzitii:
            tranzitii[(int(x), l)] = [int(y), ]
        else:
            tranzitii[(int(x), l)].append(int(y))

    q0 = int(f.readline()) #starea initiala
    nrF = int(f.readline()) #nr de stari finale

    for final in f.readline().strip().split():
        qfinal.add(int(final)) #starile finale

tranzitiiDFA = {}
qfinalDFA = set()
nDFA = 0
alfabetDFA = alfabet.copy()
mDFA = 0
q0DFA = str(q0)
nrFDFA = 0

staripartiale = [str(x) for x in stari]
starirezolvate = set(staripartiale.copy())
starepartiala = set()

stariDFA = set(staripartiale)

i = 0

while i < len(staripartiale):
    stare = staripartiale[i]
    for litera in alfabet:
        starepartiala.clear()
        for staresingulara in str(stare):
            if (int(staresingulara), litera) not in tranzitii:
                continue
            else:
                starepartiala |= set(tranzitii[int(staresingulara), litera])
        stareDFA = ''.join(str(elem) for elem in sorted(list(starepartiala)))
        if len(stareDFA) == 0:
            continue
        if (str(stare), litera) not in tranzitiiDFA:
            tranzitiiDFA[(str(stare), litera)] = stareDFA
        starirezolvate.add(str(stare))
        stariDFA.add(stareDFA)
        if stareDFA not in starirezolvate:
            staripartiale.append(stareDFA)
        if str(stare) not in starirezolvate:
            staripartiale.append(str(stare))
    i += 1

nDFA = len(stariDFA)
mDFA = len(tranzitiiDFA)
for stare in stariDFA:
    for singular in stare:
        if int(singular) in qfinal:
            qfinalDFA.add(stare)
            break
nrFDFA = len(qfinalDFA)

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






