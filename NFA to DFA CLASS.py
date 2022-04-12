class FA:
    qfinal = None
    tranzitii = None
    n = None
    stari = None
    alfabet = None
    m = None
    q0 = None
    nrF = None

    def citire(self):
        with open("input.txt") as f:
            self.tranzitii = {}
            self.qfinal = set()
            self.n = int(f.readline()) #nr de stari
            self.stari = [int(x) for x in f.readline().strip().split()] #starile
            self.alfabet = [x for x in f.readline().strip().split()] #literele din alfabet
            self.m = int(f.readline()) #nr de tranzitii

            for i in range(self.m):
                x, y, l = f.readline().strip().split()  # stare stare litera
                if (int(x), l) not in self.tranzitii:
                    self.tranzitii[(int(x), l)] = [int(y), ]
                else:
                    self.tranzitii[(int(x), l)].append(int(y))


            self.q0 = int(f.readline()) #starea initiala
            self.nrF = int(f.readline()) #nr de stari finale

            for final in f.readline().strip().split():
                self.qfinal.add(int(final)) #starile finale


    def NFAtoDFA(self, DFA):

        DFA.tranzitii = {}
        DFA.qfinal = set()
        DFA.n = 0
        DFA.alfabet = self.alfabet.copy()
        DFA.m = 0
        DFA.q0 = str(self.q0)
        DFA.nrF = 0

        staripartiale = [str(x) for x in self.stari]
        starirezolvate = set(staripartiale.copy())
        starepartiala = set()

        DFA.stari = set(staripartiale)

        i = 0

        while i < len(staripartiale):
            stare = staripartiale[i]
            for litera in self.alfabet:
                starepartiala.clear()
                for staresingulara in str(stare):
                    if (int(staresingulara), litera) not in self.tranzitii:
                        continue
                    else:
                        starepartiala |= set(self.tranzitii[int(staresingulara), litera],)
                stareDFA = ''.join(str(elem) for elem in sorted(list(starepartiala)))
                if len(stareDFA) == 0:
                    continue
                if (str(stare), litera) not in DFA.tranzitii:
                    DFA.tranzitii[(str(stare), litera)] = stareDFA
                starirezolvate.add(str(stare))
                DFA.stari.add(stareDFA)
                if stareDFA not in starirezolvate:
                    staripartiale.append(stareDFA)
                if str(stare) not in starirezolvate:
                    staripartiale.append(str(stare))
            i += 1

        DFA.n = len(DFA.stari)
        DFA.m = len(DFA.tranzitii)
        for stare in DFA.stari:
            for singular in stare:
                if int(singular) in self.qfinal:
                    DFA.qfinal.add(stare)
                    break
        DFA.nrF = len(DFA.qfinal)


    def afisare(self):
        with open("output.txt", 'w') as g:
            print("Numarul de stari este:", self.n, file=g)
            print("Starile sunt:", *self.stari, file=g)
            print("Alfabetul este:", *self.alfabet, file=g)
            print(f"Exista {self.m} tranzitii:", file=g)
            for cheie in self.tranzitii:
                print(*cheie, self.tranzitii[cheie], file=g)
            print("Starea initiala este:", self.q0, file=g)
            print(f"Exista {self.nrF} stari finale:", file=g)
            for final in self.qfinal:
                print(final, file=g)


NFA = FA()
DFA = FA()
NFA.citire()
NFA.NFAtoDFA(DFA)
DFA.afisare()


