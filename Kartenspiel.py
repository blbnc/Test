import random
import os


card_Deck = ["Karo A", "Karo K", "Karo D", "Karo 10", "Karo 9", "Karo 8",
             "Karo 7", "Herz A", "Herz K", "Herz D", "Herz 10", "Herz 9",
             "Herz 8", "Herz 7", "Pik A", "Pik K", "Pik D", "Pik 10", "Pik 9",
             "Pik 8", "Pik 7", "Kreuz A", "Kreuz K", "Kreuz D", "Kreuz 10",
             "Kreuz 9", "Kreuz 8", "Kreuz 7"]

card_Deck = random.sample(card_Deck, len(card_Deck))
card_Top = ""
cards_Played = []

player_Matrix = []
player_Names = ["Player 1", "Player 2", "Player 3", "Player 4"]

cls = lambda: os.system('cls')


def drawcard(player_number):
    """Es wird eine Karte gezogen."""
    player_Matrix[player_number].append(card_Deck[0])
    card_Deck.remove(card_Deck[0])


def playcard(player_number, card):
    """Es wird eine Karte gespielt."""
    cards_Played.append(card_Top)
    player_Matrix[player_number].remove(card)


def gamerules(input_card):
    """Überprüfen der Spielregeln"""
    if input_card.startswith("Pik") or input_card.startswith("Kreuz"):
        if card_Top.startswith("Pik") or card_Top.startswith("Kreuz"):
            return True
    if input_card.startswith("Karo") or input_card.startswith("Herz"):
        if card_Top.startswith("Karo") or card_Top.startswith("Herz"):
            return True
    if input_card[-1] == card_Top[-1]:
        return True
    return False


while True:
    """Eingabe der Spieler mit Fehlerabfang"""
    try:
        player_Count = int(float(input("Geben Sie die Anzahl der Spieler ein."
                                 " (2-4)\n")))
        if(player_Count < 2) or (player_Count > 4):
            print("Die Zahl war nicht passend gewählt")
        else:
            break
    except ValueError:
        print("Das war keine Zahl.")

for i in range(0, player_Count):
    """Eingabe der Namen"""
    print("Wollen sie für", player_Names[i], "den Namen ändern? (Ja/Nein)")
    input_String = input()
    if input_String == "Ja":
        player_Names[i] = input("Geben Sie jetzt den Namen ein\n")
    else:
        print("Der Namer wurde nicht geändert.\n")

while True:
    """Eingabe der Kartenhand mit Fehlerabfang"""
    try:
        starting_Hand = int(float(input("Wie viele Karten soll man am Anfang"
                                        " auf der Hand haben? (3-5)\n")))
        if(starting_Hand < 3) or (starting_Hand > 5):
            print("Die Zahl war nicht passend gewählt.\n")
        else:
            break
    except ValueError:
        print("Das war keine Zahl.")

player_Matrix = [[] * 0 for i in range(player_Count)]

for i in range(0, starting_Hand):
    for j in range(0, player_Count):
        drawcard(j)
card_Top = card_Deck[0]
card_Deck.remove(card_Deck[0])

while True:
    for i in range(0, player_Count):
        cls()
        print(player_Names[i], "du bist dran.")

        print("Es liegt in der Mitte: ", card_Top, "\n")

        for j in range(0, player_Count):
            if i != j:
                print(player_Names[j], "hat noch ", len(player_Matrix[j]),
                      "Karten.")
            print("")

        while True:
            """Eingabe einer Karte"""
            print(player_Matrix[i])
            try:
                input_Card = input("Geben sie eine Karte ein.\n")

                if player_Matrix[i].index(input_Card) != -1 \
                        or card_Deck.index(input_Card) != -1 \
                        or cards_Played.index(input_Card) != -1:
                    ValueError

                if gamerules(input_Card):
                    print("Die Karte war spielbar\n")
                    playcard(i, input_Card)
                    card_Top = input_Card
                    break
                else:
                    print("Die Karte war nicht spielbar.\n")
                    input_Card = input("Geben sie eine Karte ein andere Karte"
                                       " ein oder ziehen Sie.\n")

                if input_Card == "ziehen":
                    drawcard(i)
                    print("Es wurde eine Karte gezogen.\n")
                    if gamerules(player_Matrix[i][-1]):
                        print("Die gezogene Karte war spielbar.\n")
                        input_Card = player_Matrix[i][-1]
                        playcard(i, player_Matrix[i][-1])
                        card_Top = input_Card
                    break
            except ValueError:
                print("Es wurde eine Falsche Eingabe gemacht")

        if not card_Deck:
            card_Deck = random.sample(cards_Played, len(cards_Played))
        if not player_Matrix[i]:
            cls()
            print("Mau-Mau")
            break
    if not player_Matrix[i]:
        break

n = len(player_Matrix)

for i in range(n):
    for j in range(0, n-i-1):
        if len(player_Matrix[j]) > len(player_Matrix[j+1]):
            player_Matrix[j], player_Matrix[j+1] = \
                player_Matrix[j+1], player_Matrix[j]
            player_Names[j], player_Names[j+1] = \
                player_Names[j+1], player_Names[j]

for i in range(0, player_Count):
    print("Platz", (i + 1), ":", player_Names[i])


input()
input()

"""
Zeitplan:
Erster Tag 21.11. Grundgerüsst des Programmes schreiben und Funktionalitäten
beschreiben.
Zweiter Tag 23.11. Ausarbeitung der Funktionalitäten

Tutorium: Klären von Fragen wie die Rangliste aussehen soll.


Wie können Sie die in der Konsole ausgegebenen Inhalte löschen und wie
betriebssystemunabhangig ist diese Funktionalitat in Python umgesetzt?
Python kann über den Import des OS eine Funktion ausführen die den Text in der
Konsole löscht

Gibt es Grenzen für Benutzereingaben oder Spielsituationen?
Nein, da ein Benutzter bei jeder Eingabe alles eingeben kann, das Programm
sollte nur nicht daraufhin abstürtzen wenn etwas falsches eingegeben wurde.
Hierbei ist die try: except: Funktion sehr hilfreich, da es möglich macht
Fehler einfach abzufangen.

12 Testfälle:
Eingabe der Spieleranzahl und der Anfangskarten:
1. Zu kleine Zahl
2. Zu große Zahl
3. Text
4. Eingeben einer Fließkommazahl
5. Eingeben einer richtigen Zahl
Um alle möglischen eingaben zu testen nehmen wir eine zu große und zu kleine
Zahl um zu sehen ob wir nur in dem Bereich sind in dem wir unsere Zahl wollen.
Text um zu sehen ob das Programm den Fehler abfangen kann.
Testen mit der richtigen Zahl ob der Code das richtige durchgehen lässt

6. Legen einer Falschen Karte
7. Legen einer richtigen Karte
8. Legen der Karte die in der Mitte ist

Jede mögliche Karte legen die man sieht oder nicht sieht oder die in der Mitte
liegt, da eine karte die nicht auf der Hand ist nicht gelegt werden darf

Zufall kann man durch mehreres ausführen des Codes Testen, da bei mehreren
Versuchen nicht das gleiche rauskommen darf

Illustrieren  und  beschreiben  Sie in  dem Benutzungshandbuch:
1. Eingabe der Anzahl der Spieler
2. Eingabe der Namen der Spieler wenn gewollt
3. Eingabe der Anzahl der Karten die jeder Spieler am Anfang besitzen soll
4. Alle Spieler weg gucken die nicht an der Reihe sind
5. Eine Karte auswählen, die man spielen möchte
6. Wenn nicht möglich ziehen
7. Weg gucken der nächste Spieler ist an der Reihe
"""
