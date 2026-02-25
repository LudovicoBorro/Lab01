import random

from domanda import Domanda

class Game:
    def __init__(self, domande: list[Domanda], livello_max: int):
        self.domande = domande
        self.livello_max = livello_max
        self.punteggio = 0

    def partita(self):
        livello = 0
        punteggio = 0
        while livello <= self.livello_max:
            domande_liv_corrente = []
            for domanda in self.domande:
                if livello == int(domanda.livello):
                    domande_liv_corrente.append(domanda)
            domanda_proposta = random.choice(domande_liv_corrente)
            array_risp = [domanda_proposta.risp1, domanda_proposta.risp2, domanda_proposta.risp3, domanda_proposta.risp4]
            random.shuffle(array_risp)
            print(f"Livello {livello}) {domanda_proposta.testo}")
            i = 1
            for risp in array_risp:
                print(f"{i}. {risp}")
                i += 1
            num_risp = int(input("Inserisci la risposta: "))
            risposta = array_risp[num_risp-1]
            if risposta == domanda_proposta.risp_corr:
                punteggio += 1
                livello += 1
                print("Risposta corretta!\n")
            else:
                print(f"Risposta sbagliata! La risposta corretta era: {array_risp.index(domanda_proposta.risp_corr)+1}")
                break
        self.punteggio = punteggio
        print("\n")
        print(f"Hai totalizzato {punteggio} punti!")
        return
