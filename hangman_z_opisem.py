#główna funkcja
def hangman(word):
#zmienna przechowująca liczbę błędów
    wrong = 0
#zmienna przechowująca liste znaków potrzebnych do figurki wisielca
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
#zmienna zachowująca wszystkie litery słowa word
    rletters = list(word)
#lista łańcuchów znaków do wyświetlenia podpowiedzi (zank podkreślenia w zalężnośći od liczby znkaów)
    board = ["__"] * len(word)
#zmienna śledząca czy gracz już wygrał grę
    win = False
# komunikat wyświetlany na koniec funkcji
    print("Gra w Wisielca")
#pętla jest wykonywana tak długo jak wrong jest mniejsze od len(stages)
while wrong < len(stages) - 1:
    print("\n")
    msg = "Odgadnij literę: "
    #wprowadzenie litery przez gracza i zapisanie w zmiennej
    char = input(msg)
    #jeśli litera zapisana w zminnej zawiera się w rletters znaczy że gracz odgadł ta litere
    if char in rletters:
        cind = rletters.index(char)
        # dodajemy odgadniętą literę do zmiennej board
        board[cind] = char
        #zmieniamy prawidłowo odgadniętą litere znakiem $, by podczas następnej iteracji pętli metoda index mogła znaleźć kolejne wystąpienie tej samej litery
        rletters[cind] = '$'
    else:
        #jeśli nie udało się odgadnąć litery inkrementujemy wartość wrong
        wrong += 1
        #wyświetlamy plansze wisielca
    print((" ".join(board)))
    #w zależności od ilości błędów zostanie wyświetlona taka sama ilość znaków z stages
    e = wrong + 1
    print("\n".join(stages[0: e]))
    #na koniec sprawdzamy czy gracz wygrał
    if "__" not in board:
        print("Wygrałeś!")
        print(" ".join(board))
        win = True
        break
        #gdy gracz przegrywa zmienna win ma wartość false i wyświetla kompletną figurke wisielca
    if not win:
        print("\n".join(stages[0: wrong]))
        print("Przegrałeś! Miałeś odgadnąć: {}.".format(word))

hangman("kot")