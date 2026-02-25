import domanda as d
import game as g
import player as p

input_dom = "domande.txt"
output_risp = "punti.txt"

def livello_max(lista_domande):
    massimo = 0
    for domanda in lista_domande:
        if massimo < int(domanda.livello):
            massimo = int(domanda.livello)
    return massimo

def main():
    lista_domande = []
    lista_partite = []
    lista_giocatori = []
    try:
        file = open(input_dom, "r")
        attributi = []
        for line in file:
            if line == "\n":
                continue
            attributi.append(line)
        i = 0
        while i != len(attributi):
            domanda = d.Domanda(attributi[i], attributi[i+1], attributi[i+2], attributi[i+3], attributi[i+4], attributi[i+5])
            i += 6
            lista_domande.append(domanda)
        file.close()
    finally:
        pass
    partita = g.Game(lista_domande,livello_max(lista_domande))
    lista_partite.append(partita)
    partita.partita()
    punteggio_partita = partita.punteggio
    nickname = input("Inserisci il tuo nickname per salvare il punteggio: ")
    giocatore = p.Player(nickname, punteggio_partita)
    lista_giocatori.append(giocatore)
    nicknames = {}
    try:
        file = open(output_risp, "r")
        for line in file:
            campi = line.split(" ")
            nicknames[campi[0]] = int(campi[1])
        file.close()
    finally:
        pass
    nicknames[nickname] = punteggio_partita
    nicknames_sorted = sorted(nicknames.items(), key=lambda item: item[1], reverse=True)
    try:
        file = open(output_risp, "w")
        for nick in nicknames_sorted:
            file.write(nick[0] + " " + str(nick[1]) + "\n")
        file.close()
    finally:
        pass
main()
