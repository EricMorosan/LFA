class DFA:
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
                x, y, l = f.readline().strip().split() # stare stare litera
                self.tranzitii[(int(x), l)] = int(y)


            self.q0 = int(f.readline()) #starea initiala
            self.nrF = int(f.readline()) #nr de stari finale

            for final in f.readline().strip().split():
                self.qfinal.add(int(final)) #starile finale



    def minimizare(self, initial):
        P = []
        Pfinal = []
        Pfinal.append(list(initial.qfinal))
        Pfinal.append(list(set(initial.stari) - initial.qfinal))
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
                    for litera in initial.alfabet:
                        for multime in P:
                            # print(litera,stare1,tranzitii[(stare1, litera)],stare2,tranzitii[(stare2, litera)])
                            if initial.tranzitii[(stare1, litera)] in multime and initial.tranzitii[(stare2, litera)] not in multime:
                                ok = 0
                    if ok == 1:
                        partial1.append(stare2)
                    else:
                        partial2.append(stare2)
                if partial1:
                    Pfinal.append(partial1.copy())
                if partial2:
                    Pfinal.append(partial2.copy())

        self.n = len(P)
        self.stari = [''.join(str(x) for x in y) for y in P]
        self.alfabet = initial.alfabet.copy()
        self.qfinal = set()
        for stare in self.stari:
            for singular in stare:
                if int(singular) == initial.q0:
                    self.q0 = stare
                if int(singular) in initial.qfinal:
                    self.qfinal.add(stare)
        self.nrF = len(final.qfinal)

        self.tranzitii = {}
        for partitie in P:
            ales = partitie[0]
            for litera in initial.alfabet:
                rezultat = initial.tranzitii[(ales, litera)]
                for partitie2 in P:
                    if rezultat in partitie2:
                        self.tranzitii[(''.join(str(x) for x in partitie), litera)] = ''.join(str(x) for x in partitie2)
        self.m = len(final.tranzitii)


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


initial = DFA()
final = DFA()
initial.citire()
final.minimizare(initial)
final.afisare()

