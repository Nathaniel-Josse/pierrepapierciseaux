from Lib.custom import printlbl as p

def choice(choicesKeys: list) -> str:
    p.print_lbl("Choisissez entre pierre, papier et ciseaux ! (Ou appuyez sur 'q' pour quitter)\n")
    while True:
        player = input("pi✊/pa✋/ci✌ : ")
        if player in choicesKeys:
            return player
        if player == "q":
            p.print_lbl("Merci d'avoir joué !👋\n")
            return "q"
        else:
            p.print_lbl("Veuillez sélectionner votre choix parmi les choix possibles. Seules les abréviations données sont acceptées.\n")